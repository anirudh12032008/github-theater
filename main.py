import time
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
            # console.print(panel)
        return [i['name'] for i in res.json()]

console=Console()
def fetchcommit(id, repo):
    url = f"https://api.github.com/repos/{id}/{repo}/commits"
    res = requests.get(url)
    if res.status_code != 200:
        console.print(f"Error  {repo}: {res.status_code}")
        return
    console.print(Panel.fit(f"[bold green]Commit History --- {id}/{repo}  (latest 20 only) [/bold green]"))
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
        "[bold cyan]the almiighty lord of codes [yellow]{author}[/yellow] wrote this [bold magenta]legendary[/bold magenta] piece of code on [green]{date}[/green] and in the least golden color it was called [red]{sha}[/red][/bold cyan] \n {msg}",
        "[bold cyan]the [red]dumbesttt[/red] of all time [yellow]{author}[/yellow] just dropped this [bold red]absolutely garabagee[/bold red] code on [green]{date}[/green] and it was marked as [magenta]{sha}[/magenta][/bold cyan] \n {msg}",
        "[bold cyan]ts [bold yellow]lazy mf[/bold yellow] [yellow]{author}[/yellow] made this [bold green]Legendary Move[/bold green] on [green]{date}[/green] with this weierd code [red]{sha}[/red][/bold cyan] \n {msg}",
        "[bold cyan]{author} has just [bold magenta]vibe coded[/bold magenta] a lot on [green]{date}[/green] and put [red]{sha}[/red] label on it, hahah[/bold cyan] \n {msg}"
    ]
    color = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    between = ["[bold cyan] >> curtains close, next act incoming <<[/bold cyan]", 
                 "[bold green] >> lets see what happens next << [bold green]",
                 "[bold red] >> wtf did this person did!!!!!! << [bold red]",
                 "[bold yellow] >> omg omg omg omg omg whattttt!!!! << [bold yellow]",
                         "[bold magenta] >> this thing fucked up the whole codebase :( << [bold magenta]"]
    
    for j, i in enumerate(res.json()[::-1][:20]):
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
            f"\n\n{text}\n\n",
            title=f"Scene --- {j+1}",
            border_style=random.choice(color),
            padding=(0, 2)
        )
        console.print(scene)
        # this is a very new and cool thing I came across through rich documentation so thought to use here instead of normaly print thing
        console.rule(f" [bold red] {random.choice(between)} [/bold red] ", style=random.choice(color))
        time.sleep(1.7)
    
def contributors(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/contributors"
    res = requests.get(url)
    if res.status_code != 200:
        console.print(f"Error  {repo}: {res.status_code}, hahahha")
        return
    console.print(Panel.fit(f"[bold magenta] CAST of the worst show [bold yellow] {repo} [/bold yellow] [/bold magenta]"))

    for i in res.json():
        console.print(f"[bold green]{i['login']} ---> destruction power : {i['contributions']} [/bold green]")

from pyfiglet import Figlet

def issues(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/issues"
    res = requests.get(url)

    if res.status_code != 200:
        console.print(f"Error   {repo}: {res.status_code},hahahahahahhha")
        
        return
    
    iss = []
    for i in res.json():
        iss.append(i)
    
    if not iss:
        console.print(Panel.fit(f"[green] no monster here [/green]", border_style="green"))
        return
    console.print(Panel.fit(f"[bold red] MOSTERSSSS!! in {repo} [/bold red]", border_style="red"))

    for i in iss:
        console.print(f"[magenta] monster {i['number']} named {i['title']} created by {i['user']['login']}[/magenta]")
        console.print("")


from rich.align import Align

def intro():
    x = Figlet(font="doom")
    y = x.renderText("GITHUB THEATER")
    console.print(Align.center(f"[bold magenta] {y} [/bold magenta]"))
    console.print(Align.center("[bold yellow] get readyyy for the worst show everrrrrr!!!!! ( I already warned you hahaha ) [/bold yellow]"))
    console.print(Align.center("[bold red] Only few repos will be shown in the list due to github api being pain in ass and not actually providing all repos [/bold red]"))
    time.sleep(3)

def ending(username, repo):
    console.rule("[bold red] THIS IS HOW {repo} ENDED..... [/bold red]", style="magenta")
    time.sleep(2)
    console.print(Panel.fit(f"the tradegy is over.. the bugs still live in the repo with their family... and this is the story of every dumb repo!!! \n Hope you enjoyed it!! \n Owner of this Theater - Anirudh Sahu (GH: anirudh12032008, Slack: @Anirudh) \n and I created this for #terminalcraft and #summer-of-making Less then 30% AI was used in this project and the creativity you can just see already :hehe: ", border_style="bright_red"))

def theater(username, repo):

    # intro()
    wish = Panel.fit(
        f"[bold magenta] SHOW is starting sooooonnn..............[/bold magenta]"
        f"[cyan] Starring : {username}(dumbass) in [bold red] {repo} [/bold red] [/cyan]",
        title="UPCOMINGG SHOWWW",
        border_style="bright_yellow"
    )
    console.print(wish)
    time.sleep(3)
    console.print(Align.center(" YOU WILL REGRET THIS, hahahaha"))
    time.sleep(3)
    contributors(username, repo)
    time.sleep(5)
    issues(username, repo)
    time.sleep(5)
    fetchcommit(username,repo)
    time.sleep(5)
    ending(username, repo)

if __name__ == "__main__":
    intro()
    # username = "hackclub"
    username = Prompt.ask("[bold magenta] Username : [/bold magenta]")
    fetchrepodts(username)
    repos= fetchreponame(username)
    userrepo = Prompt.ask("[bold blue]name of repo : [/bold blue]")
    # if userrepo in repos:
    #     theater(username, userrepo)
    # else:
    #     console.print(f"[red] BROOO don't you know the repo name :sob sob sob:, you are idiot, hahaha [/red]")
    theater(username, userrepo)

    # theater(username, "armed")
    # issues(username, "armed")
    # contributors(username, "armed")