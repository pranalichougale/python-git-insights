import requests
user = "pranalichougale"

headers = {}

def count_commits(user):
    total_commits = 0
    
    # Step 1: Get all repos of the user
    repos_url = f"https://api.github.com/users/{user}/repos"
    repos_response = requests.get(repos_url, headers=headers)
    repos = repos_response.json()

    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{user}/{repo_name}/commits"
        commits_response = requests.get(commits_url, headers=headers, params={"author": user})
        
        if commits_response.status_code == 200:
            commits = commits_response.json()
            total_commits += len(commits)
            print(f"Repo: {repo_name}, Commits: {len(commits)}")
        else:
            print(f"Could not fetch commits for {repo_name}")
    
    return total_commits


if __name__ == "__main__":
    total = count_commits(user)
    print(f"\nTotal commits by {user}: {total}")
