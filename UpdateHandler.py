import os
import requests

config_path = os.getenv("APPDATA")
MultiTool = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/MultiTool.exe"
config = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/config.json"

def update():
    downloadconfig = requests.get(config, allow_redirects=True)
    open("config.json", "wb").write(downloadconfig.content)

    print("Config Downloaded und settet !")

    downloadMultiTool = requests.get(MultiTool, allow_redirects=True)
    open("MultiTool", "wb").write(downloadMultiTool.content)

