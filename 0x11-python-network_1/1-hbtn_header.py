#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from sys import argv

    url = argv[1]

    with urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
