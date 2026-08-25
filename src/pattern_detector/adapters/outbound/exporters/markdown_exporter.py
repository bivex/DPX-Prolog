import os
from ....domain.detection import DetectionReport
from ....ports.outbound.exporter_port import ExporterPort


class MarkdownExporter(ExporterPort):
    def export(self, report: DetectionReport, output_path: str) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        lines = [
            "# 🦉 DPX-Prolog Architecture & Logic Pattern Findings Report\n",
            f"- **Target Path**: `{report.target_path}`",
            f"- **Scanned Files**: `{report.scanned_files_count}`",
            f"- **Execution Time**: `{report.execution_time_seconds:.4f}s`",
            f"- **Total Detections**: `{report.total_detections}`\n",
            "## 📊 Category Breakdown\n",
        ]
        for cat, cnt in sorted(report.category_counts.items()):
            lines.append(f"- **{cat}**: `{cnt}`")

        lines.append("\n## 🔍 Detected Patterns & Declarative Hazards\n")
        lines.append("| # | Category | Pattern Type | Target Functor | Confidence | Location | Summary |")
        lines.append("|---|---|---|---|:---:|---|---|")

        for idx, d in enumerate(report.detections, start=1):
            loc_str = f"{os.path.basename(d.location.file_path)}:{d.location.line_number}"
            lines.append(
                f"| {idx} | `{d.category.value}` | `{d.pattern_type.value}` | `{d.target_name}` | **{d.confidence.percentage}%** | `{loc_str}` | {d.summary} |"
            )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
