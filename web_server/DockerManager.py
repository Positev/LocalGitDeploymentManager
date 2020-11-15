import subprocess, os
from GitManager import repo_path
def compose_up(repoID,compose_path, env_path):
    
    current_working_directory = os.getcwd()
    current_repo_path = repo_path(repoID)
    os.chdir(current_repo_path)
    print(current_repo_path)
    print(current_working_directory)
    env_flag = f'--env-file "{env_path}"' if env_path != '' else ""
    
    os.system(f'docker-compose -f "{compose_path}" {env_flag} up -d --build')
    
    os.chdir(current_working_directory)
    return "Done", 200

def compose_down(file_path):
    pass

