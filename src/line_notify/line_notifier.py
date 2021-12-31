"""line_notifier.py, module

Line notifier Class file

"""

from requests import post
from requests.models import HTTPError

# import time


class Line():
    """Line, class

    Line Notifier Class

    Attributes
        token (str): secret token for LINE API.

    Examples:
        examples for sending message.
        >>> line = LINE(token="aabbccdeeddff")
        >>> line.notify("helloworld")
    """

    def __init__(self, token):
        self.token = token

    def notify(self, msg):
        """notify, function

        notify message to LINE account

        Args:
            msg (str) : sending message

        Returns:
            Bool: If success to send message, return True.else, return False

        Note:
            No note

        """
        if self.token is None:
            print("token is not set")
            return False
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + self.token}
        payload = {"message": msg}
        try:
            res = post(url, headers=headers, data=payload)
            res.raise_for_status()
        except HTTPError:
            print("post is failed")
            return False
        else:
            return True
