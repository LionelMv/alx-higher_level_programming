#!/usr/bin/python3
"""
Given repo and owner name as argvs,
use Github API (documentation in documentation
https://developer.github.com/v3/repos/commits/)
to list last 10 commits.
Usage: ./100-github_commits.py [github_repo] [github_owner]
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(url)
    list_commits = r.json()
    for commit in list_commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
