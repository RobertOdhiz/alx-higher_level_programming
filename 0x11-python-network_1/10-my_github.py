#!/usr/bin/python3
"""
Python script that uses the GitHub API to display your id.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, token)

    try:
        response = requests.get(url, auth=auth)
        user_data = response.json()

        if 'id' in user_data:
            print(user_data['id'])
        else:
            print("None")
    except ValueError:
        print("None")
