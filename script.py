import requests
import pandas as pd

user = "antarpreetsinghsran"

headers = {}

def count_commits(user):
    total_commits = 0
    all_commit_dates = []

    
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

            # Collect commit dates
            for commit in commits:
                commit_date = commit["commit"]["author"]["date"]
                all_commit_dates.append(commit_date)

            print(f"Repo: {repo_name}, Commits: {len(commits)}")
        else:
            print(f"Could not fetch commits for {repo_name}")
    
    #  Return both total commits and commit dates
    return total_commits, all_commit_dates

def commits_by_period(commit_dates):
    # Convert list to pandas DataFrame
    df = pd.DataFrame(commit_dates, columns=["date"])
    df["date"] = pd.to_datetime(df["date"])

    # Commits per Day
    per_day = df.groupby(df["date"].dt.date).size()

    # Commits per Week
    per_week = df.groupby(df["date"].dt.isocalendar().week).size()

    # Commits per Month
    per_month = df.groupby(df["date"].dt.to_period("M")).size()

    return per_day, per_week, per_month

if __name__ == "__main__":
    total, commit_dates = count_commits(user)
    print(f"\nTotal commits by {user}: {total}")

    if commit_dates:
        per_day, per_week, per_month = commits_by_period(commit_dates)

        print("\nCommits per Day:")
        print(per_day)

        print("\nCommits per Week:")
        print(per_week)

        print("\nCommits per Month:")
        print(per_month)
