import subprocess
import os
import json
from time import sleep
import requests


config_path = os.getenv("APPDATA")
download_config = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/config.json"
update_file = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/UpdateHandler.exe"

def checkforupdate():
    download = requests.get("https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/update.json")

    data = download.text
    value = json.loads(data)
    update = value.get("MultiTool")

    if os.path.exists(config_path + "\MultiTool\config.json"):

        if version == update:
            print("Login Manager")
        else:
            if os.path.exists(config_path + "/MultiTool/UpdateHandler.txt"):
                subprocess.call(config_path + "/MultiTool/UpdateHandler.exe")
                print("Hab update gemacht ! ")
            else:
                print("Downlaod update path !")
                download_update = requests.get(update_file, allow_redirects=True)
                join_path = os.path.join(config_path)
                open(join_path + "/MultiTool/UpdateHandler.exe", "wb").write(download_update.content)
                print("Update Downloaded !")
                subprocess.call(config_path + "/MultiTool/UpdateHandler.exe")
                exit()
    else:
        setup()      


def setup():
    config_folder = "MultiTool"
    path = os.path.join(config_path, config_folder)
    if not os.path.exists(config_path + "\MultiTool"):
        os.mkdir(path)
        sleep(3)
        download = requests.get(download_config, allow_redirects=True)
        open(config_path + "\MultiTool\config.json", "wb").write(download.content)
    else:
        pass



try:
    with open(config_path + "\MultiTool\config.json", "r") as file:
        config = json.load(file)

    print("[SYSTEM] Config Loaded !")

    login = config["LOGIN_NAME"]
    passwort = config["LOGIN_PASSWORT"]
    version = config["VERSION_CONFIG"]

    checkforupdate()
except FileNotFoundError:
    setup()