from GitManager import *
from DockerManager import *
import json

def load_repo_defs():
    path = 'Config/repos.json'

    with open(path) as repo_file:
        global repos
        repos = json.loads(repo_file.read())

allowed_actions = ['init', 'update']
repos = {}
load_repo_defs()

def handle_action(repoID, action):
    #if repos == {}:
    #    return "No Repos Registered", 405
    action = action.lower()
    if action == 'init':
        if not repo_exists(repoID):
            if repoID in repos.keys():
                response = clone_repo(repoID, repos[repoID]["RepoLink"]) 
                #compose_up("")
                return response
            else:
                return "Repo not registered", 405
        else:
            return "Repo already cloned. Clone to update", 405
    elif action == 'update':
        if repo_exists(repoID):
            response = pull_repo(repoID) 
            compose_up(repoID, repos[repoID]["ComposePath"], repos[repoID]["EnvPath"])
            return response
        else:
            return "Repo has not been cloned. Must init.", 405
    else: 
        return 'not allowed', 405

