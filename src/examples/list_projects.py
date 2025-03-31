
from typing import Dict, List, Optional
import json
from pytaigaclient.client import TaigaClient

TAIGA_HOST = "http://localhost:9000"


def login(username, password) -> Optional[TaigaClient]:
    cli = TaigaClient(TAIGA_HOST)
    try:
        result = cli.auth.login(username=username, password=password)
        cli.update_token(result["auth_token"])
        return cli
    except Exception as e:
        print(f"Login failed: {e}")
        return None


def print_projects_list(cli: TaigaClient) -> None:
    try:
        projects = cli.projects.list()
        if not projects:
            print("No projects found.")
            return
        for project in projects:
            print(json.dumps(project, indent=4, sort_keys=True))
    except Exception as e:
        print(f"Failed to list projects: {e}")


def create_project(cli: TaigaClient, name: str, description: str) -> Optional[int]:
    try:
        project = cli.projects.create(name=name, description=description)
        print(f"Project created: ID {project['id']}, Name: {project['name']}")
        return project["id"]
    except Exception as e:
        print(f"Failed to create project: {e}")
        return


if __name__ == "__main__":
    cli = login("test", "test")
    project_id = create_project(cli, "Test Project", "This is a test project.")
    if project_id:
        print(f"Project created with ID: {project_id}")
    print_projects_list(cli)
