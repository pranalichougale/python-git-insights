import requests
import pandas as pd
from colorama import Fore, Style

user = "pranalichougale"
headers = {"Authorization": ""}

def count_commits(user):
    total_commits = 0

    # Step 1: Get all repos of the user
    repos_url = f"https://api.github.com/users/{user}/repos"
    repos_response = requests.get(repos_url,headers=headers)
    repos = repos_response.json()

    print(Fore.GREEN + "*****Count of Commits started*****" + Style.RESET_ALL)
    if not isinstance(repos, list):
        print("Unexpected response:", repos)
        return 0
    
    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{user}/{repo_name}/commits"
        commits_response = requests.get(commits_url, headers=headers,params={"author": user})
        
        if commits_response.status_code == 200:
            commits = commits_response.json()
            total_commits += len(commits)
            print(f"Repo: {repo_name}, Commits: {len(commits)}")
        else:
            print(f"Could not fetch commits for {repo_name}")
    
    return total_commits

def count_of_pulls(user):
    total_pulls = 0 

    # Step 1: Get all repos of the user
    repos_url = f"https://api.github.com/users/{user}/repos"
    repos_response = requests.get(repos_url,headers=headers)
    repos = repos_response.json()

    print(Fore.GREEN + "*****Count of Pull Request started*****" + Style.RESET_ALL)
    if not isinstance(repos, list):
        print("Unexpected response:", repos)
        return 0
    for repo in repos:
        repo_name = repo['name']
        total_pulls_url = f"https://api.github.com/repos/{user}/{repo_name}/pulls?state=closed"
        total_pulls_response = requests.get(total_pulls_url,headers=headers, params={"author": user})

        if total_pulls_response.status_code == 200:
            pulls = total_pulls_response.json()
            total_pulls += len(pulls)

            print(f"Repo: {repo_name}, pulls: {len(pulls)}")
        else:
            print(f"Could not fetch pulls for {repo_name}")

def list_of_branch(user):
    all_branches={}
    
    repos_url = f"https://api.github.com/users/{user}/repos"
    repos_response = requests.get(repos_url,headers=headers)
    repos = repos_response.json()

    print(Fore.GREEN + "*****List of Branches*****" + Style.RESET_ALL)
    if not isinstance(repos, list):
        print("Unexpected response:", repos)
        return 0
    for repo in repos:
        repo_name = repo['name']
        list_of_branch_url =f"https://api.github.com/repos/{user}/{repo_name}/branches"
        list_of_branch_response = requests.get(list_of_branch_url,headers=headers, params={"author": user})

        if list_of_branch_response.status_code == 200:
            branches = list_of_branch_response.json()
            branch_names = [b['name'] for b in branches]
            all_branches[repo_name] = branch_names
        else:
           print(f"no branch has been created")
    
    return all_branches


if __name__ == "__main__":
    total = count_commits(user)
    print(f"Total commits by {user}: {total}")

    total = count_of_pulls(user)
    print(f"Total pulls by {user}: {total}")
    
    branches = list_of_branch(user)
    print(f"Branches: {branches}")
    

