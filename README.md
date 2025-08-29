# GitHub Insights with Python  

This project is a **mini Python script** that connects to the **GitHub REST API** to fetch useful insights about a given GitHub user, including:  

-  Total commits per repository  
-  Total closed pull requests per repository  
-  List of branches in each repository  

It’s a beginner-friendly project that demonstrates how to work with APIs, authentication, and JSON data in Python.  

---

##  Features  

1. **Count Commits** – Fetches the number of commits for each repository of a user.  
2. **Count Pull Requests** – Fetches the number of closed pull requests made by the user.  
3. **List Branches** – Lists all branches available in each repository.  
4. **Colored Output** – Uses the `colorama` library for better terminal readability.  

---

##  Tech Stack  

- **Python 3**  
- **requests** → For making API calls  
- **colorama** → For colored console output  
- **pandas** → (Optional) For handling structured data if extended later  

---

##  Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/python-git-insights.git
   cd python-git-insights
2. Install dependencies:  
   pip install -r requirements.txt

 ---  

##  Usage

1. Open script.py and update your GitHub username:

   user = "your-github-username"

2.(Optional) Add your GitHub Personal Access Token in headers for higher API limits:

   headers = {"Authorization": "token YOUR_GITHUB_PAT"}

3. Run the script:

   python script.py

4. Example output:

  *****Count of Commits started*****
  Repo: form-with-javascript, Commits: 5
  Repo: python-git-insights, Commits: 10
  Total commits by your-username: 15

  *****Count of Pull Request started*****
  Repo: python-git-insights, Pulls: 3
  Total pulls by your-username: 3

  *****List of Branches*****
  {'python-git-insights': ['main', 'dev'], 'form-with-javascript': ['main']}

---  

## Requirements

Create a requirements.txt file with:

requests
pandas
colorama

Install using:

pip install -r requirements.txt

## Future Improvements

Paginate API results to count all commits and PRs (currently limited to 30 per API call).

Export data to Excel/CSV using Pandas.

Build a simple Streamlit Dashboard for visualization.

   

