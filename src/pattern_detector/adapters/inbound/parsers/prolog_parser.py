import os
import re
from pathlib import Path
from typing import List, Union, Dict
from ....domain.code_model import CodeModel, PrologFile, PrologModule, PrologPredicate, PrologClause, PrologDirective
from ....ports.inbound.parser_port import ParserPort


class RegexPrologParser(ParserPort):
    PROLOG_EXTENSIONS = {".pl", ".pro", ".prolog", ".plt", ".dcg", ".chr"}

    def parse_file(self, file_path: str, content: str) -> PrologFile:
        prolog_file = PrologFile(
            file_path=file_path,
            raw_content=content,
            modules=[],
            predicates=[],
            directives=[],
        )

        lines = content.splitlines()
        current_module: PrologFile | PrologModule = None
        predicate_map: Dict[str, PrologPredicate] = {}

        # 1. Parse Directives & Module Declarations
        module_pattern = re.compile(r':-\s*module\s*\(\s*([a-zA-Z0-9_]+)\s*,\s*\[(.*?)\]\s*\)\.', re.DOTALL)
        for m in module_pattern.finditer(content):
            mod_name = m.group(1)
            raw_exports = m.group(2)
            exports = [e.strip() for e in raw_exports.split(",") if "/" in e]
            line_num = content.count("\n", 0, m.start()) + 1
            pm = PrologModule(
                name=mod_name,
                exported_predicates=exports,
                predicates=[],
                directives=[],
                raw_body=m.group(0),
                line_number=line_num,
            )
            prolog_file.modules.append(pm)
            current_module = pm

        dir_pattern = re.compile(r'^\s*:-\s*([a-zA-Z0-9_]+)\b\s*(.*?)\s*\.', re.MULTILINE | re.DOTALL)
        for m in dir_pattern.finditer(content):
            d_name = m.group(1)
            d_args = (m.group(2) or "").strip()
            if d_args.startswith("(") and d_args.endswith(")"):
                d_args = d_args[1:-1].strip()
            line_num = content.count("\n", 0, m.start()) + 1
            directive = PrologDirective(
                name=d_name,
                args=d_args,
                raw_text=m.group(0),
                line_number=line_num,
            )
            prolog_file.directives.append(directive)
            if current_module:
                current_module.directives.append(directive)

        # 2. Parse Horn Clauses & Facts
        # Tokenize by clause terminator (period followed by whitespace/newline)
        clause_pattern = re.compile(
            r'^\s*([a-zA-Z0-9_]+)(?:\s*\((.*?)\))?\s*(:-|-->)?\s*(.*?)\.',
            re.MULTILINE | re.DOTALL
        )

        for m in clause_pattern.finditer(content):
            raw_clause = m.group(0).strip()
            if raw_clause.startswith(":-") or raw_clause.startswith("%") or raw_clause.startswith("/*"):
                continue

            pred_name = m.group(1)
            args_str = m.group(2) or ""
            neck = m.group(3) or ""
            body_str = m.group(4) or ""

            # Calculate arity
            arity = 0
            if args_str.strip():
                # Rough argument split ignoring nested parentheses
                depth = 0
                args_count = 1
                for ch in args_str:
                    if ch in "([{":
                        depth += 1
                    elif ch in ")]}":
                        depth -= 1
                    elif ch == "," and depth == 0:
                        args_count += 1
                arity = args_count

            is_rule = neck == ":-"
            is_dcg = neck == "-->"
            is_fact = not neck

            line_num = content.count("\n", 0, m.start()) + 1
            clause = PrologClause(
                head=f"{pred_name}({args_str})" if args_str else pred_name,
                body=body_str.strip() if (is_rule or is_dcg) else None,
                is_rule=is_rule,
                is_fact=is_fact,
                is_dcg=is_dcg,
                arity=arity,
                raw_text=raw_clause,
                line_number=line_num,
            )

            sig = f"{pred_name}/{arity}"
            if sig not in predicate_map:
                p = PrologPredicate(
                    name=pred_name,
                    arity=arity,
                    clauses=[clause],
                    line_number=line_num,
                )
                predicate_map[sig] = p
                prolog_file.predicates.append(p)
                if current_module:
                    current_module.predicates.append(p)
            else:
                predicate_map[sig].clauses.append(clause)

        return prolog_file

    def parse_code_model(self, paths: List[Union[str, Path]]) -> CodeModel:
        model = CodeModel()
        for p in paths:
            path_obj = Path(p)
            if path_obj.is_file():
                if path_obj.suffix in self.PROLOG_EXTENSIONS or path_obj.name.endswith(".pl"):
                    try:
                        with open(path_obj, "r", encoding="utf-8", errors="replace") as f:
                            content = f.read()
                        model.add_file(self.parse_file(str(path_obj), content))
                    except Exception:
                        pass
            elif path_obj.is_dir():
                for root, _, files in os.walk(path_obj):
                    for file in files:
                        ext = os.path.splitext(file)[1]
                        if ext in self.PROLOG_EXTENSIONS:
                            full_p = os.path.join(root, file)
                            try:
                                with open(full_p, "r", encoding="utf-8", errors="replace") as f:
                                    content = f.read()
                                model.add_file(self.parse_file(full_p, content))
                            except Exception:
                                pass
        return model
