import re
from typing import List
from .base import Rule
from ..code_model import CodeModel
from ..detection import Detection
from ..value_objects import PatternType, Confidence, SourceLocation, EvidenceItem


class DefiniteClauseGrammarRule(Rule):
    @property
    def name(self) -> str:
        return "DEFINITE_CLAUSE_GRAMMAR"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        dcg_pattern = re.compile(r'^\s*([a-zA-Z0-9_]+)(?:\(.*?\))?\s*-->\s*(.*)\.', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = dcg_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    rule_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_DCG_RULE",
                        weight=0.95,
                        description=f"Definite Clause Grammar (DCG) rule '{rule_name}': '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.DEFINITE_CLAUSE_GRAMMAR,
                            target_name=rule_name,
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class ClpfdConstraintReasoningRule(Rule):
    @property
    def name(self) -> str:
        return "CLPFD_CONSTRAINT_REASONING"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        clpfd_pattern = re.compile(r'library\s*\(\s*clpfd\s*\)|#=|#\\=|#<|#>|#<=|#>=|\bin\s+[0-9A-Za-z_\.]+\.\.|\blabeling\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                if clpfd_pattern.search(line) and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_CLPFD_CONSTRAINT",
                        weight=0.95,
                        description=f"CLP(FD) Finite Domain constraint reasoning: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.CLPFD_CONSTRAINT_REASONING,
                            target_name="CLP(FD)",
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class ClprRealConstraintSolvingRule(Rule):
    @property
    def name(self) -> str:
        return "CLPR_REAL_CONSTRAINT_SOLVING"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        clpr_pattern = re.compile(r'library\s*\(\s*clpr\s*\)|library\s*\(\s*clpq\s*\)|\{[^\{\}]*?[=<>][^\{\}]*?\}')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                if clpr_pattern.search(line) and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_CLPR_CONSTRAINT",
                        weight=0.92,
                        description=f"CLP(R/Q) Real/Rational constraint solving: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.CLPR_REAL_CONSTRAINT_SOLVING,
                            target_name="CLP(R/Q)",
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class ConstraintHandlingRulesRule(Rule):
    @property
    def name(self) -> str:
        return "CONSTRAINT_HANDLING_RULES"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        chr_pattern = re.compile(r'library\s*\(\s*chr\s*\)|<=>|==>|\bchr_constraint\b')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                if chr_pattern.search(line) and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_CHR_RULE",
                        weight=0.95,
                        description=f"Constraint Handling Rules (CHR) syntax: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.CONSTRAINT_HANDLING_RULES,
                            target_name="CHR",
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class TablingMemoizationSlgRule(Rule):
    @property
    def name(self) -> str:
        return "TABLING_MEMOIZATION_SLG"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        table_pattern = re.compile(r':-\s*table\s+([A-Za-z0-9_]+/[0-9]+)')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = table_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_sig = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_TABLING_SLG",
                        weight=0.95,
                        description=f"SLG Resolution tabling memoization directive for '{pred_sig}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.TABLING_MEMOIZATION_SLG,
                            target_name=pred_sig,
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class MetaInterpreterVanillaRule(Rule):
    @property
    def name(self) -> str:
        return "META_INTERPRETER_VANILLA"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        meta_pattern = re.compile(r'\b(?:solve|eval_goal|interpret)\s*\((.*?)\)\s*:-')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = meta_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_META_INTERPRETER",
                        weight=0.92,
                        description=f"Meta-circular clause evaluator / Vanilla meta-interpreter: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.META_INTERPRETER_VANILLA,
                            target_name="MetaInterpreter",
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections
