import argparse

ARGUMENTS = [
    {
        "name": "--build-directory",
        "description": "Absolute path to your build directory.",
    },
    {
        "name": "--build-label",
        "description": "Label for uploaded build. Example: 0.1.1",
    },
    {
        "name": "--user-api-key",
        "description": "User API key provided by GameSwift.",
    },
    {
        "name": "--application-secret",
        "description": "Application secret provided by GameSwift.",
    },
    {
        "name": "--branch-secret",
        "description": "Branch secret provided by GameSwift.",
    },
]


def parse_arguments():
    parser = argparse.ArgumentParser(description='Uploads build to GameSwift launcher.')
    for arg in ARGUMENTS:
        var_name = arg["name"].replace("--", "").replace("-", "_")
        parser.add_argument(arg["name"], dest=var_name, required=True, help=arg["description"])

    args = parser.parse_args()
    return args.build_directory, args.build_label, args.user_api_key, args.application_secret, args.branch_secret
