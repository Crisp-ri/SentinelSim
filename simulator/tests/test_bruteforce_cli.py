from typer.testing import CliRunner
from unittest.mock import patch

from simulator.cli import app

runner = CliRunner()


def test_bruteforce_command_with_defaults():
    with patch("simulator.cli.bruteforce_module.bruteforce") as mock_bruteforce:
        result = runner.invoke(app, [])

    assert result.exit_code == 0
    mock_bruteforce.assert_called_once()


def test_bruteforce_command_with_custom_options():
    with patch("simulator.cli.bruteforce_module.bruteforce") as mock_bruteforce:
        result = runner.invoke(
            app,
            [
                "--delay", "0.5",
                "--target-ip", "192.168.1.200",
                "--attempts", "25",
            ],
        )

    assert result.exit_code == 0
    mock_bruteforce.assert_called_once_with(25, 0.5, "192.168.1.200")


def test_bruteforce_command_prints_success_message():
    with patch("simulator.cli.bruteforce_module.bruteforce"):
        result = runner.invoke(
            app,
            [
                "--delay", "0.3",
                "--target-ip", "192.168.1.100",
                "--attempts", "50",
            ],
        )

    assert result.exit_code == 0
    assert "Brute-force simulation completed" in result.stdout
    assert "50 attempts" in result.stdout
    assert "0.3 seconds" in result.stdout
    assert "192.168.1.100" in result.stdout


def test_bruteforce_command_rejects_invalid_attempts():
    result = runner.invoke(
        app,
        [
            "--attempts", "not-an-int",
        ],
    )

    assert result.exit_code != 0