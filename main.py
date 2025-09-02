import os
from 
import requests
from rich.console import Console

def fetchrepo(id):
    url = f"https://api.github.com/users/{id}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error  {id}: {response.status_code}")
        return 
    for i in response.json():
        print(f"Repo - {i['name']} Stars - {i['stargazers_count']} Forks - {i['forks_count']} Language - {i['language']} issues - {i['open_issues_count']}")


def fetchcommit(id, repo):
    url = f"https://api.github.com/repos/{id}/{repo}/commits"
    res = requests.get(url)
    if res.status_code != 200:
        print(f"Error  {repo}: {res.status_code}")
        return
    for i in res.json()[:10]:
        # for the message I only need the text until I get /n after that I get the descriptions
        msg = i['commit']['message'].split('\n')[0]
        print(f"Repo: {repo}-----Author: {i['commit']['author']['name']}-----Date: {i['commit']['author']['date']}-----Message: {msg}")
        print("")

if __name__ == "__main__":
    username = "anirudh12032008"
    fetchcommit(username, "armed")