import shutil
import subprocess
from pathlib import Path


def find_terraform():
    """
    Find the Terraform executable on the system.
    """
    return shutil.which("terraform")


def run_terraform(args, working_dir=None):
    """
    Run a Terraform command and return its result.
    """
    terraform_path = find_terraform()

    if terraform_path is None:
        raise FileNotFoundError("Terraform is not installed or not in PATH.")

    result = subprocess.run(
        [terraform_path] + args,
        capture_output=True,
        text=True,
        cwd=working_dir
    )

    if result.returncode == 0:
        print("[SUCCESS] Terraform command completed.")
    else:
        print("[ERROR] Terraform command failed.")
        print(result.stderr)

    return result


def validate_terraform(project_dir):
    """
    Validate Terraform configuration files in a project folder.
    """
    project_path = Path(project_dir)

    if not project_path.exists():
        raise FileNotFoundError(
            f"Project directory does not exist: {project_dir}"
        )

    if not project_path.is_dir():
        raise NotADirectoryError(
            f"Path is not a directory: {project_dir}"
        )

    terraform_files = list(project_path.glob("*.tf"))

    if not terraform_files:
        raise FileNotFoundError(
            f"No Terraform (.tf) files found in project directory: {project_dir}"
        )

    return run_terraform(
        ["validate", "-no-color"],
        working_dir=project_path
    )