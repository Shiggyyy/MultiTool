import os
import shutil
import requests
from time import sleep
config_path = os.getenv("APPDATA")

MultiTool = "https://raw.githubusercontent.com/Shiggyyy/MultiTool//main/MultiTool.py"
config = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/config.json"
exefile = "MultiTool"

def update():
    downloadconfig = requests.get(config, allow_redirects=True)
    open("config.json", "wb").write(downloadconfig.content)

    downloadMultiTool = requests.get(MultiTool, allow_redirects=True)
    open("MultiTool1.py", "wb").write(downloadMultiTool.content)
    installpath = os.getenv("MultiTool")


    sleep(3)
    shutil.move(exefile, installpath)


update()




