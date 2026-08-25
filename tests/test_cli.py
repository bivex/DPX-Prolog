from typer.testing import CliRunner
from pattern_detector.adapters.inbound.cli.main import app

runner = CliRunner()


def test_cli_catalog():
    result = runner.invoke(app, ["catalog"])
    assert result.exit_code == 0
    assert "Pattern & Hazard Catalog" in result.stdout
    assert "logic_hazards" in result.stdout


def test_cli_scan(tmp_path):
    src_file = tmp_path / "test.pl"
    src_file.write_text("""
    :- module(my_mod, [test/1]).
    test(X) --> [X].
    """)

    html_out = tmp_path / "report.html"
    json_out = tmp_path / "report.json"

    result = runner.invoke(app, [
        "scan",
        str(src_file),
        "-H", str(html_out),
        "-J", str(json_out),
    ])

    assert result.exit_code == 0
    assert "Findings Summary" in result.stdout
    assert html_out.exists()
    assert json_out.exists()
