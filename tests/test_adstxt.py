import pytest
from click.testing import CliRunner

from newshomepages import adstxt


@pytest.mark.vcr()
def test_adstxt_cli(tmp_path):
    """Test a single ads.txt request."""
    runner = CliRunner()
    result = runner.invoke(adstxt.cli, ["reuters", "-o", tmp_path])
    assert result.exit_code == 0
