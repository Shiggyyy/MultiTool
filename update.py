import os
import json
from time import sleep
from colorama import Fore
import requests

a = os.getenv("APPDATA")
download_url = "https://github.com/Shiggyyy/MultiTool/blob/main/config.json"
download_MultiTool = "https://github.com/Shiggyyy/MultiTool/blob/e43cd37ce35a87c26f6cef24a6d012830639569d/LoginManager.exe"

ver_m = ""
ver_c = ""

path = os.path.join(a + "\MultiTool")

with open(a + "\MultiTool\config.json", "r") as file:
    config = json.load(file)

ver_m = config["VERSION_MultiTool"]
ver_c = config["VERSION_CONFIG"]


def update_config():
    r = requests.get(download_url, allow_redirects=True)
    open(a + "\MultiTool\config.json", "wb").write(r.content) 

def update_main():
    downloadM = requests.get(download_MultiTool, allow_redirects=True)
    open("MultiTool.exe", "wb").write(downloadM.content)


response = requests.get("https://github.com/Shiggyyy/MultiTool/blob/main/update.json")
data = response.text
values = json.loads(data)

m = values.get("MultiTool")
c = values.get("config")


if ver_c == c:
    print("[UPDATE] Config up to date !")
    if ver_m == m:
        print("[UPDATE] MultiTool up to date !")
    else:
        update_main()
else:
    update_config()

input("")