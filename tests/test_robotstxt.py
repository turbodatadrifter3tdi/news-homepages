from click.testing import CliRunner

from newshomepages import robotstxt


def test_robotstxt_cli(tmp_path):
    """Test a single robots.txt request."""
    runner = CliRunner()
    result = runner.invoke(robotstxt.cli, ["latimes", "-o", tmp_path])
    assert result.exit_code == 0
