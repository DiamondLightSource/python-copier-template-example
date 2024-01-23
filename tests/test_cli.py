import subprocess
import sys

from python_copier_template_example import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "python_copier_template_example", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
