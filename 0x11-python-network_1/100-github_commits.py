#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest)
of a repository by a specific user using the GitHub API.
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/"\
          "{}/commits".format(owner_name, repo_name)
    params = {'per_page': 10}

    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
    except ValueError:
        print("Not a valid JSON response.")
