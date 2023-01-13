import json
import os
import sys

import argument_parser


def main_routine():
    abs_build_directory, label, user_api_key, application_secret, branch_secret = argument_parser.parse_arguments()

    _upload_build(application_secret, user_api_key, label, abs_build_directory)
    version_id, label = _list_versions(application_secret, user_api_key)
    if label == label:
        _publish_to_channel(branch_secret, user_api_key, label, version_id)
    else:
        _log("Fatal: incorrect version retrieved!")
        sys.exit(1)
    _log(f"Upload successfully finished! Your game build with label {label} should be available on "
         f"GameSwift launcher in a few minutes.")


def _upload_build(application_secret, user_api_key, new_version, abs_build_directory):
    arguments = f'-s "{application_secret}" -a "{user_api_key}" -l "{new_version}" ' \
                f'-f "{abs_build_directory}" --overwrite-draft --publish'
    full_command = _create_tool_command("make-version", arguments)
    _perform_system_command(full_command)


def _list_versions(secret, user_api_key):
    arguments = f'-s "{secret}" -a "{user_api_key}" --format json'
    full_command = _create_tool_command("list-versions", arguments)
    _log(f"Executing command: {full_command}")
    output = os.popen(full_command).read()
    last_version = json.loads(output)[0]
    version_id = last_version["id"]
    label = last_version["label"]
    _log(f"Version id: {version_id}, label of newest listed version: {label}")
    return version_id, label


def _publish_to_channel(branch_secret, user_api_key, new_version, version_id):
    arguments = f'-s "{branch_secret}" -a "{user_api_key}" -l "{new_version}" --group-version "{version_id}" ' \
                f'--publish --overwrite-draft'
    full_command = _create_tool_command("channel-make-version", arguments)
    _perform_system_command(full_command)


def _perform_system_command(command):
    _log(f"Executing command: {command}")
    command_to_execute = f'cmd /c "{command}"'
    return_code = os.system(command_to_execute)
    _log(f"Command {command} returned exit code: {return_code}")
    return return_code


def _create_tool_command(command, arguments):
    bat_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin/patchkit-tools.bat'))

    if not os.path.exists(bat_path):
        _log("Fatal: cannot find tools binary!")
        sys.exit(1)

    full_command = f'"{bat_path}" {command} {arguments}'
    return full_command


def _log(message):
    print(f"[UPLOADER] {message}")


if __name__ == '__main__':
    main_routine()
