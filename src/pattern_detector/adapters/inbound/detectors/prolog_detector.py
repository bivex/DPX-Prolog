import time
from typing import List, Optional
from ....domain.code_model import CodeModel
from ....domain.detection import Detection, DetectionReport
from ....domain.rules import get_all_rules
from ....domain.rules.base import Rule
from ....ports.inbound.detector_port import PatternDetectorPort


class PrologPatternDetector(PatternDetectorPort):
    def __init__(self, rules: Optional[List[Rule]] = None):
        self.rules = rules if rules is not None else get_all_rules()

    def detect(self, model: CodeModel) -> DetectionReport:
        start_time = time.perf_counter()
        all_detections: List[Detection] = []

        for rule in self.rules:
            try:
                results = rule.evaluate(model)
                all_detections.extend(results)
            except Exception:
                pass

        elapsed = time.perf_counter() - start_time
        target_path = model.files[0].file_path if model.files else "."

        return DetectionReport(
            target_path=target_path,
            scanned_files_count=len(model.files),
            execution_time_seconds=elapsed,
            detections=all_detections,
        )
