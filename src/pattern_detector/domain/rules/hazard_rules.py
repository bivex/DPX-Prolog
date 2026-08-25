import re
from typing import List
from .base import Rule
from ..code_model import CodeModel
from ..detection import Detection
from ..value_objects import PatternType, Confidence, SourceLocation, EvidenceItem


class UnsafeCutRedCutHazardRule(Rule):
    @property
    def name(self) -> str:
        return "UNSAFE_CUT_RED_CUT_HAZARD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        cut_pattern = re.compile(r':-.*?(?:^|[\s,\(;])!(?:[\s,;\.]|$)')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                if cut_pattern.search(line) and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_RED_CUT_HAZARD",
                        weight=0.95,
                        description=f"Procedural cut (!) alters declarative semantics and breaks commutativity: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.UNSAFE_CUT_RED_CUT_HAZARD,
                            target_name="!",
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class UnsafeTermEvaluationHazardRule(Rule):
    @property
    def name(self) -> str:
        return "UNSAFE_TERM_EVALUATION_HAZARD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        eval_pattern = re.compile(r'\b(atom_to_term|read_term_from_atom|call\s*\(\s*[A-Z][a-zA-Z0-9_]*\s*\))\b')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = eval_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_ARBITRARY_GOAL_EXECUTION",
                        weight=0.95,
                        description=f"Dynamic goal evaluation risks arbitrary code execution: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.UNSAFE_TERM_EVALUATION_HAZARD,
                            target_name="DynamicGoalExecution",
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class UnsafeDynamicAssertHazardRule(Rule):
    @property
    def name(self) -> str:
        return "UNSAFE_DYNAMIC_ASSERT_HAZARD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        assert_pattern = re.compile(r'\b(assertz|asserta|assert)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = assert_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_DYNAMIC_ASSERT_HAZARD",
                        weight=0.92,
                        description=f"Unsafe dynamic assertion '{fn_name}' risks global state leakage and database pollution",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.UNSAFE_DYNAMIC_ASSERT_HAZARD,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class UnsafeIoSystemHazardRule(Rule):
    @property
    def name(self) -> str:
        return "UNSAFE_IO_SYSTEM_HAZARD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        cmd_pattern = re.compile(r'\b(shell|process_create|system|win_exec)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = cmd_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_OS_COMMAND_INJECTION",
                        weight=0.95,
                        description=f"OS command execution via '{fn_name}' risks command injection",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.UNSAFE_IO_SYSTEM_HAZARD,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class InfiniteLeftRecursionHazardRule(Rule):
    @property
    def name(self) -> str:
        return "INFINITE_LEFT_RECURSION_HAZARD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        rec_pattern = re.compile(r'^\s*([a-zA-Z0-9_]+)\s*\((.*?)\)\s*:-\s*\1\s*\(', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = rec_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_LEFT_RECURSION_HAZARD",
                        weight=0.92,
                        description=f"Direct left-recursive clause '{pred_name}' risks stack overflow under standard SLD resolution",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.INFINITE_LEFT_RECURSION_HAZARD,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class UninstantiatedVarNegationHazardRule(Rule):
    @property
    def name(self) -> str:
        return "UNINSTANTIATED_VAR_NEGATION_HAZARD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        neg_pattern = re.compile(r'(?:\\\+|\bnot\b)\s*(?:\()?\s*(?:var\s*\([A-Z][a-zA-Z0-9_]*\)|\b[a-z0-9_]+\s*\(\s*[A-Z][a-zA-Z0-9_]*\s*\))')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                if neg_pattern.search(line) and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_UNSOUND_NEGATION",
                        weight=0.90,
                        description=f"Negation-as-failure on uninstantiated variable produces unsound logical results: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.UNINSTANTIATED_VAR_NEGATION_HAZARD,
                            target_name="UnsoundNegation",
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class MissingModuleExportHazardRule(Rule):
    @property
    def name(self) -> str:
        return "MISSING_MODULE_EXPORT_HAZARD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        for file in model.files:
            if len(file.predicates) > 5 and len(file.modules) == 0:
                loc = SourceLocation(file_path=file.file_path, line_number=1)
                ev = EvidenceItem(
                    rule_name="PROLOG_MISSING_MODULE",
                    weight=0.88,
                    description=f"File contains {len(file.predicates)} predicates without ':- module/2' encapsulation",
                    location=loc,
                )
                detections.append(
                    Detection(
                        pattern_type=PatternType.MISSING_MODULE_EXPORT_HAZARD,
                        target_name=file.file_path.split("/")[-1],
                        location=loc,
                        confidence=Confidence(0.88),
                        evidence=[ev],
                    )
                )
        return detections
