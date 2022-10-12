import os
import shutil
import requests
from time import sleep

config_path = os.getenv("APPDATA")

MultiTool = "https://raw.githubusercontent.com/Shiggyyy/MultiTool//main/MultiTool.py"
config = "https://raw.githubusercontent.com/Shiggyyy/MultiTool/main/config.json"

def update():
    print("[SYSTEM] Connect to UpdateServer")
    sleep(2)
    print("[SYSTEM] Connected !")
    print("[SYSTEM] Download: config.json")
    downloadconfig = requests.get(config, allow_redirects=True)
    open("config.json", "wb").write(downloadconfig.content)
    print("[SYSTEM] config.json replaced !")
    downloadMultiTool = requests.get(MultiTool, allow_redirects=True)
    open("MultiTool.py", "wb").write(downloadMultiTool.content)
    print("[SYSTEM] Download: MultiTool.exe")
    print("[SYSTEM] Search for env")
    sleep(1.5)
    installpath = os.getenv("MultiTool")
    print(f"[SYSTEM] Found {installpath}")
    a = shutil.copy("MultiTool.py", "MultiTool.py.new")
    os.remove("MultiTool.py")
    shutil.move("MultiTool.py.new", installpath)
    #print(f"[SYSTEM] MultiTool.exe moved to {installpath}.")
    #print("[SYSTEM] Done.")
    old_file = os.path.join(installpath, "MultiTool.py.new")
    new_file = os.path.join(installpath, "MultiTool.py")
    deletefile = os.path.join(installpath, "MultiTool.py")
    os.remove(deletefile)
    os.rename(old_file, new_file)



update()