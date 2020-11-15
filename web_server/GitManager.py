from pygit2 import clone_repository, Repository
import os, subprocess

def repo_exists(repoID):
    return os.path.exists(repo_path(repoID))

def clone_repo(repoID, git_url):
    cur_repo_path = repo_path(repoID)
    clone_repository(git_url, cur_repo_path)
    return "Done", 200


def pull_repo(repoID):
    current_working_directory = os.getcwd()
    current_repo_path = repo_path(repoID)
    os.chdir(current_repo_path)
    print(current_repo_path)
    output = subprocess.check_output(["git", "pull"])
    os.chdir(current_working_directory)
    return "Done", 200

def repo_path(repoID):
    path =  f"ClonedRepos/{repoID}"
    print(os.getcwd())
    print(path)
    return path