from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from .value_objects import SourceLocation


@dataclass
class PrologClause:
    head: str
    body: Optional[str] = None
    is_rule: bool = False
    is_fact: bool = False
    is_dcg: bool = False
    arity: int = 0
    raw_text: str = ""
    line_number: int = 1


@dataclass
class PrologDirective:
    name: str
    args: str = ""
    raw_text: str = ""
    line_number: int = 1


@dataclass
class PrologPredicate:
    name: str
    arity: int = 0
    clauses: List[PrologClause] = field(default_factory=list)
    is_dynamic: bool = False
    is_tabled: bool = False
    is_multifile: bool = False
    is_exported: bool = False
    line_number: int = 1

    @property
    def signature(self) -> str:
        return f"{self.name}/{self.arity}"


@dataclass
class PrologModule:
    name: str
    exported_predicates: List[str] = field(default_factory=list)
    predicates: List[PrologPredicate] = field(default_factory=list)
    directives: List[PrologDirective] = field(default_factory=list)
    raw_body: str = ""
    line_number: int = 1

    @property
    def total_exports(self) -> int:
        return len(self.exported_predicates)


@dataclass
class PrologFile:
    file_path: str
    raw_content: str
    modules: List[PrologModule] = field(default_factory=list)
    predicates: List[PrologPredicate] = field(default_factory=list)
    directives: List[PrologDirective] = field(default_factory=list)

    @property
    def lines_count(self) -> int:
        return len(self.raw_content.splitlines())


@dataclass
class CodeModel:
    files: List[PrologFile] = field(default_factory=list)
    module_index: Dict[str, PrologModule] = field(default_factory=dict)
    predicate_index: Dict[str, PrologPredicate] = field(default_factory=dict)

    def add_file(self, file: PrologFile) -> None:
        self.files.append(file)
        for mod in file.modules:
            self.module_index[mod.name.lower()] = mod
        for pred in file.predicates:
            self.predicate_index[pred.signature.lower()] = pred

    def get_module(self, name: str) -> Optional[PrologModule]:
        return self.module_index.get(name.lower())

    def get_predicate(self, signature: str) -> Optional[PrologPredicate]:
        return self.predicate_index.get(signature.lower())
