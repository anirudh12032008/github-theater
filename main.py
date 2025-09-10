import os
from rich.prompt import Prompt
import random
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
    # for j, i in enumerate(res.json()[:10]):
    #     # for the message I only need the text until I get /n after that I get the descriptions
    #     msg = i['commit']['message'].split('\n')[0]
    #     sha = i['sha'][:7]
    #     author = i['commit']['author']['name']
    #     date = i['commit']['author']['date'][:10]
    #     dash = "└─" if j == len(res.json()[:10]) - 1 else "├─"
    #     line = f"{dash} [{date}] - [cyan]{author}[/] -- [green]{msg}[/] ([magenta]{sha}[/])"
    #     console.print(line)
    #     # console.print(f"Repo: {repo}-----Author: {i['commit']['author']['name']}-----Date: {i['commit']['author']['date']}-----Message: {msg}")
    #     # console.print("")
    console.log(f"[green] YOO Once upon a time, in the ultra pro max repo [bold red]{repo}[/bold red]...[/green]")
    temp = [
        "[bold cyan]the almiighty lord of codes [yellow]{author}[/yellow] wrote this [bold magenta]legendary[/bold magenta] piece of code on [green]{date}[/green] and in the least golden color it was called [red]{sha}[/red][/bold cyan]",
        "[bold cyan]the [red]dumbesttt[/red] of all time [yellow]{author}[/yellow] just dropped this [bold red]absolutely garabagee[/bold red] code on [green]{date}[/green] and it was marked as [magenta]{sha}[/magenta][/bold cyan]",
        "[bold cyan]ts [bold yellow]lazy mf[/bold yellow] [yellow]{author}[/yellow] made this [bold green]Legendary Move[/bold green] on [green]{date}[/green] with this weierd code [red]{sha}[/red][/bold cyan]",
        "[bold cyan]{author} has just [bold magenta]vibe coded[/bold magenta] a lot on [green]{date}[/green] and put [red]{sha}[/red] label on it, hahah[/bold cyan]"
    ]


    for j, i in enumerate(res.json()[::-1][:10]):
        msg = i['commit']['message'].split('\n')[0]
        sha = i['sha'][:7]
        author = i['commit']['author']['name']
        date = i['commit']['author']['date'][:10]
        # I just got to know that random module has this thing too 
        text = random.choice(temp).format(
            author=author,
            date= date,
            sha = sha,
            msg = msg
        )
        scene = Panel.fit(
            text,
            title=f"Scene {j+1}",
            border_style="bright_blue"
        )
        console.print(scene)


def theater():
    pass

if __name__ == "__main__":
    username = "anirudh12032008"
    # fetchrepodts(username)
    # repos= fetchreponame(username)
    # userrepo = Prompt.ask("[bold blue]name of repo : [/bold blue]")
    # if userrepo in repos:
    #     fetchcommit(username, userrepo)
    # else:
    #     console.print(f"[red] BROOO don't you know the repo name :sob sob sob:, you are idiot, hahaha [/red]")
    fetchcommit(username,"armed")