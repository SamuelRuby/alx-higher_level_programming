#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = Request(url)
    with urlopen(req) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf8")))
