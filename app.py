
import argparse
import shutil

VERSION = "0.1.0"


def hello():
    print("\nWelcome to InfraForge!")
    print("Infrastructure. Forged entirely through code.\n")


def version():
    print(f"InfraForge version: {VERSION}")


def doctor():
    print("\nChecking your development environment...\n")

    terraform_path = shutil.which("terraform")

    if terraform_path:
        print("[OK] Terraform is installed.")
        print(f"Location: {terraform_path}")
    else:
        print("[WARNING] Terraform is not installed or not in PATH.")

    print("\nEnvironment check completed.\n")


def main():
    parser = argparse.ArgumentParser(
        prog="infraforge",
        description="Zero-click infrastructure automation platform."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    subparsers.add_parser("hello", help="Display welcome message")
    subparsers.add_parser("version", help="Display application version")
    subparsers.add_parser("doctor", help="Check development environment")

    args = parser.parse_args()

    if args.command == "hello":
        hello()
    elif args.command == "version":
        version()
    elif args.command == "doctor":
        doctor()


if __name__ == "__main__":
    main()
