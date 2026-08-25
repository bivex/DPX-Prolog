import re
from typing import List
from .base import Rule
from ..code_model import CodeModel
from ..detection import Detection
from ..value_objects import PatternType, Confidence, SourceLocation, EvidenceItem


class MonolithicModuleSrpRule(Rule):
    @property
    def name(self) -> str:
        return "MONOLITHIC_MODULE_SRP"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        for file in model.files:
            for mod in file.modules:
                if len(mod.exported_predicates) > 25 or len(mod.predicates) > 30:
                    loc = SourceLocation(file_path=file.file_path, line_number=mod.line_number)
                    ev = EvidenceItem(
                        rule_name="PROLOG_MONOLITHIC_MODULE",
                        weight=0.85,
                        description=f"Module '{mod.name}' exports {len(mod.exported_predicates)} predicates and has {len(mod.predicates)} declarations, violating SRP",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.MONOLITHIC_MODULE_SRP,
                            target_name=mod.name,
                            location=loc,
                            confidence=Confidence(0.85),
                            evidence=[ev],
                        )
                    )
        return detections


class FatPredicateAritySrpRule(Rule):
    @property
    def name(self) -> str:
        return "FAT_PREDICATE_ARITY_SRP"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        for file in model.files:
            for pred in file.predicates:
                if pred.arity >= 8:
                    loc = SourceLocation(file_path=file.file_path, line_number=pred.line_number)
                    ev = EvidenceItem(
                        rule_name="PROLOG_FAT_ARITY",
                        weight=0.85,
                        description=f"Predicate '{pred.signature}' declares excessive arity ({pred.arity} arguments >= 8)",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.FAT_PREDICATE_ARITY_SRP,
                            target_name=pred.signature,
                            location=loc,
                            confidence=Confidence(0.85),
                            evidence=[ev],
                        )
                    )
        return detections


class ImpureStateMutationSrpRule(Rule):
    @property
    def name(self) -> str:
        return "IMPURE_STATE_MUTATION_SRP"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        for file in model.files:
            for pred in file.predicates:
                has_pure = False
                has_side_effect = False
                for c in pred.clauses:
                    if c.body:
                        if "assertz" in c.body or "retract" in c.body or "format(" in c.body or "write(" in c.body:
                            has_side_effect = True
                        else:
                            has_pure = True
                if has_pure and has_side_effect:
                    loc = SourceLocation(file_path=file.file_path, line_number=pred.line_number)
                    ev = EvidenceItem(
                        rule_name="PROLOG_IMPURE_MUTATION",
                        weight=0.88,
                        description=f"Predicate '{pred.signature}' mixes pure declarative relations with impure side-effects (assertz/retract/IO)",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.IMPURE_STATE_MUTATION_SRP,
                            target_name=pred.signature,
                            location=loc,
                            confidence=Confidence(0.88),
                            evidence=[ev],
                        )
                    )
        return detections
