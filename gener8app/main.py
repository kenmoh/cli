import os
import platform
import subprocess
import time

import typer
from rich import print as rich_print
from rich.progress import track


app = typer.Typer()


@app.command()
def new(project_name: str = typer.Argument(..., help="The name of the project")):

    venv = f"{project_name}_env"
    total = 0

    for value in track(
        range(100),
        description=f":hourglass: [purple3]Creating {project_name.capitalize()} project...[/purple3] :hourglass:",
    ):
        time.sleep(0.01)
        total += 1

    try:
        os.makedirs(project_name)
    except FileExistsError:
        rich_print(f"[bold red]{project_name} already exists.[/bold red]")

    app_dir = os.path.join(project_name, "app")
    os.makedirs(app_dir)

    templates = os.path.join(app_dir, "templates")
    os.makedirs(templates)

    static = os.path.join(app_dir, "static")
    os.makedirs(static)

    directories = [
        "config",
        "database",
        "models",
        "routers",
        "schemas",
        "services",
        "test",
        "utils",
    ]
    for directory in directories:
        os.makedirs(os.path.join(app_dir, directory))
        with open(os.path.join(app_dir, directory, "__init__.py"), "w") as f:
            f.write("")
        with open(os.path.join(app_dir, directory, f"{directory}.py"), "w") as f:
            if directory == "config":
                f.write("# Create your project configurations here")
            elif directory == "database":
                f.write("# Create your database connection and configurations here")
            elif directory == "models":
                f.write("# Create your models here")
            elif directory == "routes":
                f.write("# Create your routes here")
            elif directory == "schema":
                f.write("# Create your pydantic schemas here")
            elif directory == "test":
                f.write("# Write your test here")
            elif directory == "utils":
                f.write("# Create your project utility methods or classes here")
            elif directory == "services":
                f.write("# Create your services that talks to database here")

    open(f"{app_dir}/__init__.py", "a").close()
    open(f"{app_dir}/main.py", "a").close()
    open(f"{project_name}/.env", "a").close()
    open(f"{project_name}/README.md", "a").close()
    open(f"{project_name}/.gitignore", "a").close()
    open(f"{project_name}/requirements.txt", "a").close()
    open(f"{project_name}/Dockerfile", "a").close()
    open(f"{project_name}/docker-compose.yaml", "a").close()

    # Initialize git
    subprocess.run(["git", "init"], cwd=project_name)

    rich_print(
        f" :rocket: [bold green]SUCCESS: {project_name} created [/bold green]! :rocket: :rocket:"
    )

    # Create virtual environment based on OS
    if platform.system() == "Windows":
        subprocess.run(["python", "-m", "venv", venv], cwd=project_name)
    else:
        subprocess.run(["python3", "-m", "venv", venv], cwd=project_name)

    rich_print(
        f"[cyan]cd into {project_name} and activate {venv}(virtual environment) [/cyan]"
    )
    rich_print(
        "[bold magenta]Keep building amazing things !!![/bold magenta] :sparkles: :sparkles:"
    )


@app.callback()
def callback():
    """
    Generate a bare-bone FastAPI project
    """


# if __name__ == "__main__":
#     app()
