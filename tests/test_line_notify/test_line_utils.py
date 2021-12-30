""", module
pytest for utils.py
"""

from os import getenv
import pytest
from line_notify.line_notifier import Line


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
        token = getenv("SECRET_SETTING")
        self.line = Line(token=token)

    def test_notify(self):
        """test_notify, function

        Line notify pytest function

        Note:
            if self.line.notify err, test is failed.

        """
        assert self.line.notify("test") is True
