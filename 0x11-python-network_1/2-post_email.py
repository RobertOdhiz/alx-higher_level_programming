#!/usr/bin/python3
"""
POST script
"""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv
    import urllib.parse as up

    url = argv[1]
    values = {'email': argv[2]}
    data = up.urlencode(values).encode('utf-8')

    req = Request(url, data, method='POST')
    with urlopen(req) as response:
        body = response.read()
    print(body.decode('utf-8'))
