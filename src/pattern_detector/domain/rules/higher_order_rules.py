import re
from typing import List
from .base import Rule
from ..code_model import CodeModel
from ..detection import Detection
from ..value_objects import PatternType, Confidence, SourceLocation, EvidenceItem


class HigherOrderMaplistRule(Rule):
    @property
    def name(self) -> str:
        return "HIGHER_ORDER_MAPLIST"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        ho_pattern = re.compile(r'\b(maplist|include|exclude|foldl|convlist|partition)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = ho_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_HIGHER_ORDER_PREDICATE",
                        weight=0.92,
                        description=f"Higher-order list transformation predicate '{fn_name}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.HIGHER_ORDER_MAPLIST,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.92),
                            evidence=[ev],
                        )
                    )
        return detections


class AllSolutionsAggregationRule(Rule):
    @property
    def name(self) -> str:
        return "ALL_SOLUTIONS_AGGREGATION"

    def evaluate(self, model: CodeModel) -> List[Detection]:
        detections: List[Detection] = []
        agg_pattern = re.compile(r'\b(findall|setof|bagof|aggregate|aggregate_all)\s*\(')
        for file in model.files:
            for line_idx, line in enumerate(file.raw_content.splitlines(), start=1):
                m = agg_pattern.search(line)
                if m and not line.strip().startswith("%"):
                    fn_name = m.group(1)
                    loc = SourceLocation(file_path=file.file_path, line_number=line_idx)
                    ev = EvidenceItem(
                        rule_name="PROLOG_ALL_SOLUTIONS",
                        weight=0.90,
                        description=f"All-solutions aggregation second-order predicate '{fn_name}'",
                        location=loc,
                    )
                    detections.append(
                        Detection(
                            pattern_type=PatternType.ALL_SOLUTIONS_AGGREGATION,
                            target_name=fn_name,
                            location=loc,
                            confidence=Confidence(0.90),
                            evidence=[ev],
                        )
                    )
        return detections
