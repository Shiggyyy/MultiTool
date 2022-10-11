import subprocess
import os
import json
from time import sleep
import requests
import platform


os_name = platform.system()
config_path = os.getenv("APPDATA")
download_config = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/config.json"
download_user = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/user.json"
update_file = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/UpdateHandler.exe"

if os_name == "Windows":
    subprocess.check_output(f"setx MultiTool {os.getcwd()}", shell=True)
else:
    exit()

def checkforupdate():
    download = requests.get("https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/update.json")

    data = download.text
    value = json.loads(data)
    update = value.get("MultiTool")

    if os.path.exists(config_path + "\MultiTool\config.json"):

        if version == update:
            print("Login Manager")
        else:
            if os.path.exists(config_path + "/MultiTool/UpdateHandler.py"):
                os.system("cd" + config_path + "py /MultiTool/UpdateHandler.py")
                print("Hab update gemacht !")
            else:
                print("Downlaod update path !")
                download_update = requests.get(update_file, allow_redirects=True)
                join_path = os.path.join(config_path)
                open(join_path + "/MultiTool/UpdateHandler.exe", "wb").write(download_update.content)
                print("Update Downloaded !")
                os.system("cd" + config_path + "py /MultiTool/UpdateHandler.py")
                exit()
    else:
        setup()      


def setup():
    config_folder = "MultiTool"
    path = os.path.join(config_path, config_folder)
    if not os.path.exists(config_path + "/MultiTool"):
        os.mkdir(path)
        sleep(3)
        downloadconfig = requests.get(download_config, allow_redirects=True)
        open(config_path + "/MultiTool/config.json", "wb").write(downloadconfig.content)
    else:
        pass

    user_folder = "user"
    pathuser = os.path.join(config_path + "/MultiTool",  user_folder)    

    if not os.path.exists(pathuser + "/MultiTool/user"):
        try:
            os.mkdir(pathuser)
        except FileExistsError:
            pass
        sleep(3)
        downloaduser = requests.get(download_user, allow_redirects=True)
        open(config_path + "/MultiTool/user/user.json", "wb").write(downloaduser.content)
    else:
        pass



try:
    with open(config_path + "/MultiTool/config.json", "r") as file:
        config = json.load(file)

    print("[SYSTEM] Config Loaded !")
    version = config["VERSION_CONFIG"]

    checkforupdate()
except FileNotFoundError:
    setup()