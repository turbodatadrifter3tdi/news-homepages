import sqlite3

from click.testing import CliRunner

from newshomepages import robotstxt


def test_robotstxt_cli(tmp_path):
    """Test a single robots.txt request."""
    runner = CliRunner()
    result = runner.invoke(robotstxt.cli, ["latimes", "-o", tmp_path])
    assert result.exit_code == 0


def test_sqlite_extensions():
    """Verify that the sqlite extension can be loaded."""
    conn = sqlite3.connect(":memory:")
    conn.enable_load_extension(True)
    conn.load_extension("libsqlite_robotstxt")
    conn.close()
