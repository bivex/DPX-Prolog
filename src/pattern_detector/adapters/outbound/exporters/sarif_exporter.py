import json
import os
from ....domain.detection import DetectionReport
from ....ports.outbound.exporter_port import ExporterPort


class SarifExporter(ExporterPort):
    def export(self, report: DetectionReport, output_path: str) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        results = []
        rules_map = {}

        for d in report.detections:
            rule_id = d.pattern_type.value
            if rule_id not in rules_map:
                rules_map[rule_id] = {
                    "id": rule_id,
                    "name": d.pattern_type.name,
                    "shortDescription": {"text": d.summary},
                    "defaultConfiguration": {"level": "warning" if "hazard" in rule_id else "note"},
                }

            results.append({
                "ruleId": rule_id,
                "message": {"text": f"[{d.category.value}] {d.summary} on '{d.target_name}'"},
                "locations": [
                    {
                        "physicalLocation": {
                            "artifactLocation": {"uri": d.location.file_path},
                            "region": {
                                "startLine": d.location.line_number,
                                "startColumn": d.location.column_number,
                            },
                        }
                    }
                ],
            })

        sarif_doc = {
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "version": "2.1.0",
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": "DPX-Prolog",
                            "informationUri": "https://github.com/bivex/DPX-Prolog",
                            "semanticVersion": "0.1.0",
                            "rules": list(rules_map.values()),
                        }
                    },
                    "results": results,
                }
            ],
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(sarif_doc, f, indent=2, ensure_ascii=False)
