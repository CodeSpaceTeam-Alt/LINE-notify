""", module
pytest for utils.py
"""

from os import getenv
import pytest
from line_message.line_message import Line


class TestLine():
    """TestLine, Class

    Line-Pytest Class

    Attributes
        line (Line): Line class

    """
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        """setup, function

        setup fixture function

        Note:
            Only initialize self.line.
            This function is called per function.

        """
        token = getenv("TOKEN")
        self.line = Line(token=token)

    def test_notify(self):
        """test_notify, function

        Line notify pytest function

        Note:
            if self.line.notify err, test is failed.

        """
        assert self.line.notify("pytest simple message") is True
        assert self.line.notify("pytest dummy img", "dummy.png") is False
        assert self.line.notify("pytest true img", "tests/test.png") is True
