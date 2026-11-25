import shutil
import subprocess


def find_terraform():
    """
    Find the Terraform executable on the system.
    """
    return shutil.which("terraform")


def run_terraform(args):
    """
    Run a Terraform command and return its result.
    """
    terraform_path = find_terraform()

    if terraform_path is None:
        raise FileNotFoundError("Terraform is not installed or not in PATH.")

    result = subprocess.run(
        [terraform_path] + args,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("[SUCCESS] Terraform command completed.")
    else:
        print("[ERROR] Terraform command failed.")
        print(result.stderr)

    return result