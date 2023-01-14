# How to upload your game

## Prerequisites
* Build of your game
* 64-bit Windows machine
* [Python 3.9](https://www.python.org/downloads/release/python-390/) or newer
* Newest [build uploader](https://github.com/GameSwift/gameswift-build-uploader/releases)
* 3 secret values provided by [peter@gameswift.io](mailto:peter@gameswift.io)
  * User API key
  * Application secret
  * Branch secret

## Setup Python environment
1. Install a Python release the way you prefer from [https://www.python.org](https://www.python.org/).
2. Verify that your Python installation is valid by running below command in command line. The version returned by this command should be 3.9 or higher.
```bat
python --version
```

3. Install required Python packages by running below command in command line.
```bat
python -m pip install argparse
```
4. Download the newest release of build uploader and unpack it. We suggest unpacking the archive to a directory named `gameswift-build-uploader`.

## Use script
In order to actually upload a build, you need to run `build_uploader.py` script in Windows command line. Script needs 5 parameters described below.
* `build-directory` - directory containing your game build. The script will take care of archiving it before uploading to launcher. For example, if your build executable is located at `D:\build_1\game.exe`, the build directory should be `D:\build_1`.
* `build-label` - label of build to be uploaded. Usually used for build version, we suggest the most common [semantic versioning](https://semver.org/) for this purpose.
* `user-api-key` - unique user key needed for all uploading actions.
* `application-secret` - unique application key. This differs for your Windows/Mac builds within one game.
* `branch-secret` - unique branch key indicating which branch should be used to publish the build. This differs for your Windows/Mac build branches.

Sample usage:
```bat
python D:\gameswift-build-uploader\src\build_uploader.py ^
--build-directory "D:\Builds\MyGameBuild_0_1_1" ^
--build-label "0.1.1" ^
--user-api-key "1234567890abcdef1234567890abcdef" ^
--application-secret "1234567890abcdef1234567890abcdef" ^
--branch-secret "1234567890abcdef1234567890abcdef"
```

Note: the process of uploading can take some time, depending on your build size and connection speed. After successful upload script should exit with a message like `[UPLOADER] Upload successfully finished!`.

# Troubleshooting
In case of any problems, you can try reading help for build uploader like below or contact us at [peter@gameswift.io](mailto:peter@gameswift.io).
```bat
python D:\gameswift-build-uploader\src\build_uploader.py -h
```
