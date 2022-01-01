"""utils.py, module

Line notifier utilities

"""

from argparse import ArgumentParser
import sys
from line_notify.line_notifier import Line


def get_args():
    """get_args, function

    get command-line arguments

    Returns:
        NameSpace: parser.parse_args() returns

    Note:
        No note

    """
    parser = ArgumentParser(description='line notify tool')
    parser.add_argument('--token', type=str, default="", help='token')
    parser.add_argument('--message', type=str, default="test msg", help='message')
    return parser.parse_args()


def main():
    """main, function

    notify message cli main

    Returns:
        Bool: If success to send message, return True.else, return False

    """
    opt = get_args()
    line = Line(token=opt.token)
    return line.notify(opt.message)


if __name__ == "__main__":
    sys.exit(main())
