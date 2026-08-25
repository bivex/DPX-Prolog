import json
import os
from ....domain.detection import DetectionReport
from ....ports.outbound.exporter_port import ExporterPort


class HtmlHudExporter(ExporterPort):
    def export(self, report: DetectionReport, output_path: str) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        report_data_json = json.dumps(report.to_dict(), ensure_ascii=False)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DPX-Prolog // Logic Programming HUD</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,600;0,800;1,400&family=Plus+Jakarta+Sans:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #060B19;
            --surface: #0E1A38;
            --surface-hover: #162650;
            --border: #1F3668;
            --accent: #00F5D4;
            --accent-glow: rgba(0, 245, 212, 0.15);
            --cyan: #38BDF8;
            --amber: #F59E0B;
            --crimson: #FF0054;
            --purple: #9D4EDD;
            --text: #F1F5F9;
            --text-muted: #94A3B8;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        }}

        body {{
            background: var(--bg);
            color: var(--text);
            padding: 2.5rem;
            min-height: 100vh;
        }}

        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 1.5rem;
            margin-bottom: 2rem;
        }}

        .logo-group {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}

        .logo-icon {{
            font-size: 2.2rem;
            background: rgba(0, 245, 212, 0.1);
            border: 1px solid var(--accent);
            padding: 0.4rem 0.8rem;
            border-radius: 10px;
        }}

        h1 {{
            font-size: 1.8rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #FFF 30%, var(--accent) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .ai-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: linear-gradient(135deg, #00F5D4 0%, #059669 100%);
            color: #060B19;
            font-weight: 700;
            font-size: 0.85rem;
            padding: 0.55rem 1.1rem;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 14px rgba(0, 245, 212, 0.25);
        }}

        .ai-btn:hover {{
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(0, 245, 212, 0.4);
            filter: brightness(1.1);
        }}

        .ai-btn.copied {{
            background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%);
            color: #060B19;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.25rem;
            margin-bottom: 2.5rem;
        }}

        .stat-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.25rem;
            transition: all 0.2s ease;
        }}

        .stat-card:hover {{
            border-color: var(--accent);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px var(--accent-glow);
        }}

        .stat-label {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
            font-family: 'JetBrains Mono', monospace;
        }}

        .stat-val {{
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--accent);
            font-family: 'JetBrains Mono', monospace;
        }}

        .filter-bar {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }}

        .search-input {{
            flex: 1;
            min-width: 280px;
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 0.75rem 1.25rem;
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            outline: none;
        }}

        .search-input:focus {{
            border-color: var(--accent);
        }}

        .filter-btn {{
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.85rem;
            transition: 0.2s;
        }}

        .filter-btn.active, .filter-btn:hover {{
            background: var(--accent);
            color: #060B19;
            font-weight: 600;
            border-color: var(--accent);
        }}

        .findings-table {{
            width: 100%;
            border-collapse: collapse;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            overflow: hidden;
        }}

        th, td {{
            padding: 1rem 1.25rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
            font-size: 0.9rem;
        }}

        th {{
            background: rgba(14, 26, 56, 0.95);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-muted);
        }}

        tr:hover td {{
            background: var(--surface-hover);
        }}

        .badge {{
            display: inline-block;
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
        }}

        .badge-logic {{ background: rgba(0, 245, 212, 0.15); color: var(--accent); border: 1px solid var(--accent); }}
        .badge-meta {{ background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid var(--cyan); }}
        .badge-gof {{ background: rgba(157, 78, 221, 0.15); color: var(--purple); border: 1px solid var(--purple); }}
        .badge-hazard {{ background: rgba(255, 0, 84, 0.15); color: var(--crimson); border: 1px solid var(--crimson); }}
        .badge-solid {{ background: rgba(245, 158, 11, 0.15); color: var(--amber); border: 1px solid var(--amber); }}

        .code-pill {{
            font-family: 'JetBrains Mono', monospace;
            background: rgba(0,0,0,0.3);
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            border: 1px solid var(--border);
            font-size: 0.82rem;
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo-group">
            <div class="logo-icon">🦉</div>
            <div>
                <h1>DPX-Prolog // Logic Programming HUD</h1>
                <p style="color: var(--text-muted); font-size: 0.85rem;">ISO Prolog, SWI-Prolog, CLP(FD/R/Q), CHR & Meta-Interpreter Static Analyzer</p>
            </div>
        </div>
        <div style="display: flex; gap: 0.75rem; align-items: center;">
            <button id="copy-ai-btn" class="ai-btn" onclick="copyForAi()">
                <span>🤖</span>
                <span id="copy-ai-text">Copy for AI</span>
            </button>
            <span class="badge badge-logic" id="exec-time"></span>
        </div>
    </header>

    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-label">Total Detections</div>
            <div class="stat-val" id="total-count">0</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Logic & Constraints</div>
            <div class="stat-val" id="logic-count" style="color: var(--accent);">0</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">GoF Patterns</div>
            <div class="stat-val" id="gof-count" style="color: var(--purple);">0</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Declarative Hazards</div>
            <div class="stat-val" id="hazard-count" style="color: var(--crimson);">0</div>
        </div>
    </div>

    <div class="filter-bar">
        <input type="text" id="search-box" class="search-input" placeholder="Filter by pattern, category, functor, or filename...">
        <button class="filter-btn active" data-filter="ALL">ALL</button>
        <button class="filter-btn" data-filter="logic_constraints">LOGIC & CLP</button>
        <button class="filter-btn" data-filter="higher_order_meta">HIGHER-ORDER</button>
        <button class="filter-btn" data-filter="gof_">GoF PATTERNS</button>
        <button class="filter-btn" data-filter="logic_hazards">HAZARDS</button>
        <button class="filter-btn" data-filter="solid_principles">SOLID</button>
    </div>

    <table class="findings-table">
        <thead>
            <tr>
                <th>#</th>
                <th>Category</th>
                <th>Pattern Type</th>
                <th>Target Functor</th>
                <th>Confidence</th>
                <th>Location</th>
                <th>Summary</th>
            </tr>
        </thead>
        <tbody id="findings-body"></tbody>
    </table>

    <script>
        const reportData = {report_data_json};

        document.getElementById('total-count').textContent = reportData.total_detections;
        document.getElementById('exec-time').textContent = reportData.execution_time_seconds.toFixed(4) + 's';

        const catCounts = reportData.category_counts || {{}};
        document.getElementById('logic-count').textContent = (catCounts['logic_constraints'] || 0) + (catCounts['higher_order_meta'] || 0);
        const gofTotal = (catCounts['gof_creational'] || 0) + (catCounts['gof_structural'] || 0) + (catCounts['gof_behavioral'] || 0);
        document.getElementById('gof-count').textContent = gofTotal;
        document.getElementById('hazard-count').textContent = (catCounts['logic_hazards'] || 0);

        function renderTable(items) {{
            const tbody = document.getElementById('findings-body');
            tbody.innerHTML = '';
            items.forEach((d, idx) => {{
                const tr = document.createElement('tr');
                let badgeClass = 'badge-logic';
                if (d.category.includes('gof')) badgeClass = 'badge-gof';
                else if (d.category.includes('meta')) badgeClass = 'badge-meta';
                else if (d.category.includes('hazard')) badgeClass = 'badge-hazard';
                else if (d.category.includes('solid')) badgeClass = 'badge-solid';

                tr.innerHTML = `
                    <td style="color: var(--text-muted); font-family: 'JetBrains Mono';">${{idx + 1}}</td>
                    <td><span class="badge ${{badgeClass}}">${{d.category}}</span></td>
                    <td><span class="code-pill" style="color: var(--accent);">${{d.pattern_type}}</span></td>
                    <td><strong style="color: #FFF;">${{d.target_name}}</strong></td>
                    <td style="font-family: 'JetBrains Mono'; font-weight: 700; color: var(--accent);">${{d.confidence.percentage}}%</td>
                    <td style="font-family: 'JetBrains Mono'; font-size: 0.85rem; color: var(--text-muted);">${{d.location.file_path.split('/').pop()}}:${{d.location.line_number}}</td>
                    <td style="color: var(--text-muted); font-size: 0.85rem;">${{d.summary}}</td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        renderTable(reportData.detections);

        let activeFilter = 'ALL';
        const searchBox = document.getElementById('search-box');

        function applyFilters() {{
            const q = searchBox.value.toLowerCase();
            const filtered = reportData.detections.filter(d => {{
                const matchFilter = activeFilter === 'ALL' || d.category.startsWith(activeFilter) || d.category === activeFilter;
                const matchSearch = !q ||
                    d.pattern_type.toLowerCase().includes(q) ||
                    d.target_name.toLowerCase().includes(q) ||
                    d.summary.toLowerCase().includes(q) ||
                    d.location.file_path.toLowerCase().includes(q);
                return matchFilter && matchSearch;
            }});
            renderTable(filtered);
        }}

        document.querySelectorAll('.filter-btn').forEach(btn => {{
            btn.addEventListener('click', () => {{
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                activeFilter = btn.getAttribute('data-filter');
                applyFilters();
            }});
        }});

        searchBox.addEventListener('input', applyFilters);

        function copyForAi() {{
            const btn = document.getElementById('copy-ai-btn');
            const btnText = document.getElementById('copy-ai-text');

            let text = "# 🦉 DPX-Prolog Analysis Findings Summary\\n\\n";
            text += "- **Target Path**: " + reportData.target_path + "\\n";
            text += "- **Scanned Files**: " + reportData.scanned_files_count + "\\n";
            text += "- **Execution Time**: " + reportData.execution_time_seconds.toFixed(4) + "s\\n";
            text += "- **Total Detections**: " + reportData.total_detections + "\\n\\n";

            text += "## 📊 Category Breakdown\\n";
            for (const [cat, cnt] of Object.entries(reportData.category_counts || {{}})) {{
                text += "- **" + cat + "**: " + cnt + "\\n";
            }}

            text += "\\n## 🔍 Detections & Patterns\\n";
            reportData.detections.forEach((d, i) => {{
                const loc = d.location.file_path.split('/').pop() + ":" + d.location.line_number;
                text += (i + 1) + ". **[" + d.category + "] " + d.pattern_type + "** on `" + d.target_name + "` (" + d.confidence.percentage + "% confidence) at `" + loc + "`\\n";
                text += "   - *Summary*: " + d.summary + "\\n";
                if (d.evidence && d.evidence.length > 0) {{
                    d.evidence.forEach(ev => {{
                        text += "   - *Evidence*: " + ev.description + "\\n";
                    }});
                }}
            }});

            navigator.clipboard.writeText(text).then(() => {{
                btn.classList.add('copied');
                btnText.textContent = '✔ Copied to Clipboard!';
                setTimeout(() => {{
                    btn.classList.remove('copied');
                    btnText.textContent = 'Copy for AI';
                }}, 2500);
            }}).catch(err => {{
                console.error('Failed to copy', err);
            }});
        }}
    </script>
</body>
</html>
"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
