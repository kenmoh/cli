from typer.testing import CliRunner

from gener8app.main import app

runner = CliRunner()


def test_new():
    result = runner.invoke(app, ["new", "my_project"])
    assert result.exit_code == 0
