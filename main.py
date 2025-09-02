import os
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
import requests
from rich.console import Console

def fetchrepodts(id):
    url = f"https://api.github.com/users/{id}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error  {id}: {response.status_code}")
        return 
    for i in response.json():
        # make the below line pretty using rich
        panel = Panel.fit(f"[bold green]Repo - {i['name']}[/bold green]\n"
                          f"Stars - {i['stargazers_count']}\n"
                          f"Forks - {i['forks_count']}\n"
                          f"Language - {i['language']}\n"
                          f"Issues - {i['open_issues_count']}")
        console.print(panel)

def fetchreponame(id):
    url = f"https://api.github.com/users/{id}/repos"
    res = requests.get(url)
    if res.status_code == 200:
        # print the repo names with rich using panel
        for i in res.json():
            panel = Panel.fit(f"[bold green]{i['name']}[/bold green]")
            console.print(panel)
        return [i['name'] for i in res.json()]

console=Console()
def fetchcommit(id, repo):
    url = f"https://api.github.com/repos/{id}/{repo}/commits"
    res = requests.get(url)
    if res.status_code != 200:
        console.print(f"Error  {repo}: {res.status_code}")
        return
    console.print(Panel.fit(f"[bold green]Commit History --- {id}/{repo}[/bold green]"))
    for j, i in enumerate(res.json()[:10]):
        # for the message I only need the text until I get /n after that I get the descriptions
        msg = i['commit']['message'].split('\n')[0]
        sha = i['sha'][:7]
        author = i['commit']['author']['name']
        date = i['commit']['author']['date'][:10]
        dash = "└─" if j == len(res.json()[:10]) - 1 else "├─"
        line = f"{dash} [{date}] - [cyan]{author}[/] -- [green]{msg}[/] ([magenta]{sha}[/])"
        console.print(line)
        # console.print(f"Repo: {repo}-----Author: {i['commit']['author']['name']}-----Date: {i['commit']['author']['date']}-----Message: {msg}")
        # console.print("")
        # console.print("")

def theater():
    pass

if __name__ == "__main__":
    username = "anirudh12032008"
    # fetchrepodts(username)
    repos= fetchreponame(username)
    userrepo = Prompt.ask("[bold blue]name of repo : [/bold blue]")
    if userrepo in repos:
        fetchcommit(username, userrepo)
    else:
        console.print(f"[red] BROOO don't you know the repo name :sob sob sob:, you are idiot, hahaha [/red]")
