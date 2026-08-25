import pytest
from pattern_detector.domain.value_objects import (
    PatternCategory,
    PatternType,
    Confidence,
    ConfidenceLevel,
    SourceLocation,
    EvidenceItem,
)
from pattern_detector.domain.code_model import (
    PrologClause,
    PrologDirective,
    PrologPredicate,
    PrologModule,
    PrologFile,
    CodeModel,
)
from pattern_detector.domain.detection import Detection, DetectionReport
from pattern_detector.domain.pattern import PATTERN_CATALOG


def test_confidence_levels():
    c1 = Confidence(0.95)
    assert c1.level == ConfidenceLevel.VERY_HIGH
    assert c1.percentage == 95

    c2 = Confidence(0.75)
    assert c2.level == ConfidenceLevel.HIGH

    c3 = Confidence(0.55)
    assert c3.level == ConfidenceLevel.MEDIUM

    c4 = Confidence(0.30)
    assert c4.level == ConfidenceLevel.LOW


def test_source_location():
    loc = SourceLocation(file_path="src/expert_system.pl", line_number=42, column_number=5)
    assert str(loc) == "src/expert_system.pl:42:5"


def test_code_model():
    model = CodeModel()
    pf = PrologFile(
        file_path="src/parser.pl",
        raw_content=":- module(my_parser, [parse/2]).\nparse(A, B) :- true.",
    )
    mod = PrologModule(name="my_parser", exported_predicates=["parse/2"], line_number=1)
    pred = PrologPredicate(name="parse", arity=2, line_number=2)
    pf.modules.append(mod)
    pf.predicates.append(pred)

    model.add_file(pf)
    assert len(model.files) == 1
    assert model.get_module("my_parser") == mod
    assert model.get_predicate("parse/2") == pred


def test_detection_report():
    loc = SourceLocation(file_path="src/test.pl", line_number=10)
    det = Detection(
        pattern_type=PatternType.DEFINITE_CLAUSE_GRAMMAR,
        target_name="expr",
        location=loc,
        confidence=Confidence(0.95),
        evidence=[EvidenceItem(rule_name="DCG", weight=0.95, description="DCG grammar rule", location=loc)],
    )
    report = DetectionReport(
        target_path="src/",
        scanned_files_count=1,
        execution_time_seconds=0.012,
        detections=[det],
    )
    assert report.total_detections == 1
    assert report.category_counts[PatternCategory.LOGIC_CONSTRAINTS.value] == 1
    d_dict = report.to_dict()
    assert d_dict["total_detections"] == 1
