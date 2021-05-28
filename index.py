from github import Github
from credentials import token
from cli import repos_prompt, repo_prompt

print("Authenticating...")

# authenticate user
git = Github(token)
user = git.get_user()

print("Loading repositories...")

# select to remove repositories
repos = user.get_repos()
selected = repos_prompt(repos)

for repo in selected:
    if repo_prompt(repo):
        repo.delete()
