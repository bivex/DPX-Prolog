import re
from typing import List
from .base import Rule
from ..code_model import CodeModel
from ..detection import Detection
from ..value_objects import PatternType, Confidence, SourceLocation, EvidenceItem


class ChainOfResponsibilityRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_CHAIN_OF_RESPONSIBILITY"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        chain_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:handle|process|dispatch|fallback)[a-zA-Z0-9_]*)\s*\(.*?\)\s*:-(?:.*?;\s*)+', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = chain_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_CHAIN_OF_RESPONSIBILITY",
                        weight=0.95,
                        description=f"Predicate '{pred_name}' implements GoF Chain of Responsibility with disjunctive fallback branching",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_CHAIN_OF_RESPONSIBILITY,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class CommandRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_COMMAND"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        cmd_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:execute|run_command|dispatch_cmd)[a-zA-Z0-9_]*)\s*\((.*?Command.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = cmd_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_COMMAND",
                        weight=0.95,
                        description=f"Predicate '{pred_name}' implements GoF Command encapsulating executable operations as first-class terms",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_COMMAND,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class InterpreterRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_INTERPRETER"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        interp_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:eval_expr|eval_ast|evaluate_tree|interp)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = interp_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_INTERPRETER",
                        weight=0.90,
                        description=f"Predicate '{pred_name}' implements GoF Interpreter evaluating syntax tree expressions",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_INTERPRETER,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class IteratorRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_ITERATOR"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        iter_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:iterator|next_element|generator|stream_item)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = iter_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_ITERATOR",
                        weight=0.92,
                        description=f"Predicate '{pred_name}' implements GoF Iterator yielding elements on backtracking",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_ITERATOR,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class MediatorRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_MEDIATOR"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        med_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:mediator|blackboard|coordinator|bus_notify)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = med_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_MEDIATOR",
                        weight=0.90,
                        description=f"Predicate '{pred_name}' implements GoF Mediator coordinating subsystem communication",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_MEDIATOR,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class MementoRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_MEMENTO"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        mem_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:snapshot|checkpoint|save_state|restore_state|rollback)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = mem_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_MEMENTO",
                        weight=0.90,
                        description=f"Predicate '{pred_name}' implements GoF Memento recording state checkpoints for restoration",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_MEMENTO,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class ObserverRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_OBSERVER"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        obs_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:subscribe|broadcast|notify_listeners|add_observer|emit_event)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = obs_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_OBSERVER",
                        weight=0.95,
                        description=f"Predicate '{pred_name}' implements GoF Observer broadcasting event notifications to listeners",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_OBSERVER,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class StateRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_STATE"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        state_pattern = re.compile(r'^\s*([a-zA-Z0-9_]+)\s*\((?:state\([A-Za-z0-9_]+\)|.*?,\s*[A-Z][a-zA-Z0-9_]*0\s*,\s*[A-Z][a-zA-Z0-9_]*)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = state_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_STATE",
                        weight=0.95,
                        description=f"Predicate '{pred_name}' implements GoF State pattern threading explicit state transitions",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_STATE,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.95),
                            evidence=[ev],
                        )
                    )
        return detections


class StrategyRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_STRATEGY"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        strategy_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:with_strategy|apply_algorithm|solve_with|run_strategy)[a-zA-Z0-9_]*)\s*\((.*?Strategy.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = strategy_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_STRATEGY",
                        weight=0.92,
                        description=f"Predicate '{pred_name}' implements GoF Strategy injecting interchangeable algorithmic goals",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_STRATEGY,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class TemplateMethodRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_TEMPLATE_METHOD"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        template_pattern = re.compile(r'^\s*([a-zA-Z0-9_]*(?:process_pipeline|execute_flow|algorithm_skeleton)[a-zA-Z0-9_]*)\s*\((.*?)\)\s*:-', re.MULTILINE)
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = template_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    pred_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_TEMPLATE_METHOD",
                        weight=0.90,
                        description=f"Predicate '{pred_name}' implements GoF Template Method defining invariant algorithm steps with hook calls",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_TEMPLATE_METHOD,
                            target_name=pred_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections


class VisitorRule(Rule):
    @property
    def name(self) -> str:
        return "GOF_VISITOR"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        visitor_pattern = re.compile(r'=\.\.|\b(term_variables|compound_name_arguments|term_structure)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                if visitor_pattern.search(line) and not line.strip().startswith("%"):
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="BEHAVIORAL_VISITOR",
                        weight=0.92,
                        description=f"GoF Visitor compound term traversal via univ (=..) or term reflection: '{line.strip()}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.GOF_VISITOR,
                            target_name="TermVisitor",
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections
