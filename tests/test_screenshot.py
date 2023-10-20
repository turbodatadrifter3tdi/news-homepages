from click.testing import CliRunner

from newshomepages import screenshot


def test_cropped(tmp_path):
    """Test a cropped screenshot."""
    runner = CliRunner()
    result = runner.invoke(screenshot.cli, ["drudge", "-o", tmp_path])
    assert result.exit_code == 0


def test_full(tmp_path):
    """Test a full-page screenshot."""
    runner = CliRunner()
    result = runner.invoke(screenshot.cli, ["drudge", "-o", tmp_path, "--full-page"])
    assert result.exit_code == 0
