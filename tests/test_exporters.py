import os
import tempfile
from pattern_detector.domain.value_objects import PatternType, Confidence, SourceLocation, EvidenceItem
from pattern_detector.domain.detection import Detection, DetectionReport
from pattern_detector.adapters.outbound.exporters.html_hud_exporter import HtmlHudExporter
from pattern_detector.adapters.outbound.exporters.json_exporter import JsonExporter
from pattern_detector.adapters.outbound.exporters.markdown_exporter import MarkdownExporter
from pattern_detector.adapters.outbound.exporters.sarif_exporter import SarifExporter


def test_exporters():
    loc = SourceLocation(file_path="src/parser.pl", line_number=12)
    ev = EvidenceItem(rule_name="DCG", weight=0.95, description="DCG grammar rule", location=loc)
    det = Detection(
        pattern_type=PatternType.DEFINITE_CLAUSE_GRAMMAR,
        target_name="expr",
        location=loc,
        confidence=Confidence(0.95),
        evidence=[ev],
    )
    report = DetectionReport(
        target_path="src/",
        scanned_files_count=1,
        execution_time_seconds=0.005,
        detections=[det],
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        html_p = os.path.join(tmpdir, "report.html")
        json_p = os.path.join(tmpdir, "report.json")
        md_p = os.path.join(tmpdir, "report.md")
        sarif_p = os.path.join(tmpdir, "report.sarif")

        HtmlHudExporter().export(report, html_p)
        JsonExporter().export(report, json_p)
        MarkdownExporter().export(report, md_p)
        SarifExporter().export(report, sarif_p)

        assert os.path.exists(html_p)
        assert os.path.exists(json_p)
        assert os.path.exists(md_p)
        assert os.path.exists(sarif_p)

        with open(html_p, "r", encoding="utf-8") as f:
            content = f.read()
            assert "DPX-Prolog" in content
            assert "Copy for AI" in content

        with open(sarif_p, "r", encoding="utf-8") as f:
            content = f.read()
            assert "2.1.0" in content
