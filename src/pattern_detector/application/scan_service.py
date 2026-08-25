from pathlib import Path
from typing import List, Optional, Union
from ..domain.detection import DetectionReport
from ..ports.inbound.parser_port import ParserPort
from ..ports.inbound.detector_port import PatternDetectorPort
from ..adapters.outbound.exporters.html_hud_exporter import HtmlHudExporter
from ..adapters.outbound.exporters.json_exporter import JsonExporter
from ..adapters.outbound.exporters.markdown_exporter import MarkdownExporter
from ..adapters.outbound.exporters.sarif_exporter import SarifExporter


class ScanService:
    def __init__(self, parser: ParserPort, detector: PatternDetectorPort):
        self.parser = parser
        self.detector = detector

    def scan_paths(
        self,
        paths: List[Union[str, Path]],
        html_out: Optional[str] = None,
        json_out: Optional[str] = None,
        markdown_out: Optional[str] = None,
        sarif_out: Optional[str] = None,
    ) -> DetectionReport:
        model = self.parser.parse_code_model(paths)
        report = self.detector.detect(model)

        if html_out:
            HtmlHudExporter().export(report, html_out)
        if json_out:
            JsonExporter().export(report, json_out)
        if markdown_out:
            MarkdownExporter().export(report, markdown_out)
        if sarif_out:
            SarifExporter().export(report, sarif_out)

        return report
