#!/usr/bin/python3
# -*- Coding: utf-8 -*-

from requests import post
from argparse import ArgumentParser
import sys
# import time

class Line():
    def __init__(self, token):
        self.token = token

    def notify(self,msg):
        if len(self.token) == 0:
            print("token is invalid")
            return False 
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + self.token}
        payload = {"message": msg}
        return post(url, headers=headers, data=payload)
        # time.sleep(1)


def get_args():
    parser = ArgumentParser(description='line notify tool')
    parser.add_argument('--token', type=str, default="", help='token')
    return parser.parse_args()


def main():
    opt = get_args()
    line = Line(token=opt.token)
    return line.notify("test msg")    

if __name__ == "__main__":
    sys.exit(main())
