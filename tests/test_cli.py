from click.testing import CliRunner

from weatherx.cli import cli


class TestWeather:
    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["temperature"])
        assert result.exit_code == 0
        