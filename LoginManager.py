import os
import json
import ctypes
import hashlib
import platform
import re
from uuid import getnode
from os import system
from time import sleep
from colorama import Fore, init, Style
import requests
import socket
import whois
import sys
import subprocess
import psutil
import os.path
import logging
import getpass

RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RESET = Fore.RESET

init()

a = os.getenv("APPDATA")
logging.basicConfig(level=logging.INFO, filename="debug.log", format="%(asctime)s - %(levelname)s - %(message)s")
download_config = "https://github.com/Shiggyyy/MultiTool/blob/main/config.json"
download_update = "https://github.com/Shiggyyy/MultiTool/blob/e43cd37ce35a87c26f6cef24a6d012830639569d/update.exe"
logger = logging.getLogger("MultiTool")


def createjson():
    dire = "MultiTool"
    path = os.path.join(a, dire)
    if not os.path.exists(a + "\MultiTool"):
        os.mkdir(path)
        sleep(3)
        r = requests.get(download_config, allow_redirects=True)
        open(a + "\MultiTool\config.json", "wb").write(r.content)
        sleep(4)
    else:
        print("ERROR in config ")

try:
    with open(a + "\MultiTool\config.json", "r") as file:
        config = json.load(file)
    check = config["CHECK"]
    login_manger_title = config["CONS_LOGIN_MANGER_TITLE"]
    title = config["CONSOLE_TITLE"]
    login_pwd = config["LOGIN_PASSWORT"]
    login = config["LOGIN_NAME"]
    ver = config["VERSION_CONFIG"]
    user = config["LOGIN_NAME"]
    passwort = config["LOGIN_PASSWORT"]
    ver_m = config["VERSION_MultiTool"]
except FileNotFoundError:
    createjson()

try:
    check_os = platform.system()
    connect = False
    no_connect = False
    os_av = False
    os_neg = False
    req_version = (2, 3)
    cur_version = sys.version_info
    PCname = platform.node()
    uuid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    arch = platform.machine()
    proc = platform.processor()
    pcip = requests.get('https://api.ipify.org').content.decode('utf8')
    mac = ":".join(re.findall("..", "%012x" % getnode()))
    getip = socket.gethostbyname(socket.gethostname())
except KeyError:
    print(f"[{YELLOW}SYSTEM{RESET}] {RED}Error{RESET} ! JSON File has an error")
    print(f"\r\n[{YELLOW}VISIT{RESET}] Author Discord: {GREEN}SpargelTarzan#7648{RESET}")
    input(f"\r\n\r\n[{YELLOW}INFO{RESET}] Press any key to Exit ! ")
    exit()


def credits():
    os.system("cls")
    print(f"""
                {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ 
            {RESET}

                    [{YELLOW}Contributors{RESET}]

                        [{YELLOW}CEOs{RESET}]

                    SpargelTarzan
                        Solar

                     [{YELLOW}Developer{RESET}]

                        ADAMS


        If you have any questions or problems, please contact 
                        milo.devo@proton.me
    """)
    input()
    main()


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"


def getSystemInfo():
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Your PCs infos
    {RESET}
    
        """)
    uname = platform.uname()
    net_io = psutil.net_io_counters()
    print(f"""
    {Style.BRIGHT}[{YELLOW}System Information{RESET}]{Style.NORMAL}
    
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} System: {GREEN}{uname.system}{RESET}{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Node Name {GREEN}{uname.node}{RESET}{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Machine {GREEN}{uname.machine}{RESET}{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Processor {GREEN}{uname.processor}{RESET}{Style.NORMAL}
    
    
    {Style.BRIGHT}[{YELLOW}CPu Info{RESET}]{Style.NORMAL} 
    
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Physical cores:  {GREEN}{psutil.cpu_count(logical=False)}{RESET}{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Total cores: {GREEN}{psutil.cpu_count(logical=True)}{RESET}{Style.NORMAL}
    
    
    {Style.BRIGHT}[{YELLOW}Network Information{RESET}]{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Public IP: {GREEN}{pcip}{RESET}{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Local IP:  {GREEN}{getip}{RESET}{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Total Bytes Sent: {GREEN}{get_size(net_io.bytes_sent)}{RESET}{Style.NORMAL}
    [{YELLOW}INFO{RESET}]{Style.BRIGHT} Total Bytes Received: {GREEN}{get_size(net_io.bytes_recv)}{RESET}{Style.NORMAL}
    """)
    input(f"\r\n\r\n [{YELLOW}SYSTEM{RESET}]{Style.BRIGHT} Go Back to Main Menu !{Style.NORMAL}")
    selfoptions()


def spambot():
    os.system("cls")
    print(f"""
            {RED}
           _____        .__   __  .__  ___________           .__   
          /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
         /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
        /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
        \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
                \/ SpamBot
        {RESET}
    """)
    inp = input()


def selfoptions():
    os.system("cls")
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Self Options
    {RESET}
        {Style.BRIGHT}[{RED}1{RESET}] {YELLOW}Get Information About you Pc{RESET} >{Style.NORMAL}
        {Style.BRIGHT}[{RED}2{RESET}] {YELLOW}Spam bot {RESET} >{Style.NORMAL}
        
        
        {Style.BRIGHT}[{RED}b{RESET}] {YELLOW}Back to Menu{RESET} >{Style.NORMAL}
        """)
    inp = input(f"{Style.BRIGHT}[{YELLOW}SYSTEM{RESET}] Enter your Choice: {Style.NORMAL}")
    if inp == "1":
        getSystemInfo()
    elif inp == "2":
        spambot()
    elif inp == "b":
        main()
    else:
        selfoptions()


log_folder = ""


def whoisthis():
    global log_folder
    try:
        log_folder = a + "\MultiTool\Backups\website.json.backup"
        dire = "Backups"
        path = os.path.join(dire, a + "\MultiTool\Backups")
        os.mkdir(path)
        logger.info(f"Backups folder was created in {log_folder}\r")
    except FileExistsError:
        logger.info(f"Folder in {log_folder} exist ! \r")
    os.system("cls")
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Whois
    {RESET} 
        """)
    logger_path = os.getcwd()
    website = whois.whois(input(f"[{YELLOW}Whois{RESET}]{Style.BRIGHT} Website: {Style.NORMAL}"))
    with open('website.json', 'w') as f:
        f.write(str(website))
        f.close()
    with open(a + "\MultiTool\Backups\website.json.backup", "w") as f:
        f.write(str(website))
        f.close()
        logger.info(f"website.json.backup was createt in {logger_path}\r")
    if os.path.exists("website.json"):
        print(
            f"\r\n[{YELLOW}SYSTEM{RESET}]{Style.BRIGHT} {GREEN}Website.json{RESET} was created in {GREEN}{os.getcwd()}\website.json{RESET}{Style.NORMAL}")
        logger.info(f"website.json was created in {logger_path}\r")
        sleep(4)
        networkoptions()
    else:
        print(
            f"\r\n[{YELLOW}SYSTEM{RESET}]{Style.BRIGHT} {GREEN}Website.json{RESET} was not created in {GREEN}{os.getcwd()}\website.json{RESET}{Style.NORMAL}")
        logger.warning(f"website.json was not created in {logger_path}\r")
        sleep(4)
        networkoptions()


def nmapScan():
    os.system("cls")
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ NmapScanner
    {RESET} 

        {Style.BRIGHT}[{RED}ERROR{RESET}]{YELLOW} Nmap is currently not working. We will unlock it again soon{RESET}{Style.NORMAL}
        """)
    input("")
    networkoptions()


def ddosattck():
    os.system("cls")
    print(f"""
            {RED}
           _____        .__   __  .__  ___________           .__   
          /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
         /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
        /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
        \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
                \/ DDoS Attack

        {Style.BRIGHT}[{RED}ERROR{RESET}]{YELLOW} The DDOS is currently under development !{RESET}{Style.NORMAL}
        """)
    inp = input("Target: ")



def portscanner():
    os.system("cls")
    print(f"""
            {RED}
           _____        .__   __  .__  ___________           .__   
          /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
         /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
        /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
        \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
                \/ Port Scanner

        {Style.BRIGHT}[{RED}ERROR{RESET}]{YELLOW} The Portscanner is currently under development !{RESET}{Style.NORMAL}
        """)
    input("")
    networkoptions()


def botnet():
    os.system("cls")
    print(f"""
            {RED}
           _____        .__   __  .__  ___________           .__   
          /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
         /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
        /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
        \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
                \/ Bot Net
                
        {Style.BRIGHT}[{RED}ERROR{RESET}]{YELLOW} The botnet is currently under development !{RESET}{Style.NORMAL}
        """)
    input("")
    networkoptions()


def networkoptions():
    os.system("cls")
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Network Options
    {RESET} 
            
        {Style.BRIGHT}[{RED}1{RESET}] {YELLOW}DDoS Attack{RESET} >{Style.NORMAL}
        {Style.BRIGHT}[{RED}2{RESET}] {YELLOW}Port Scanner{RESET} >{Style.NORMAL}
        {Style.BRIGHT}[{RED}3{RESET}] {YELLOW}Whois{RESET} >{Style.NORMAL}
        {Style.BRIGHT}[{RED}4{RESET}] {YELLOW}Nmap Scan{RESET} >{Style.NORMAL}
        {Style.BRIGHT}[{RED}5{RESET}] {YELLOW}BotNet {RESET} >{Style.NORMAL}
        
        {Style.BRIGHT}[{RED}b{RESET}] {YELLOW}Back to menu{RESET}{Style.NORMAL}
        """)
    inp = input(f"[{YELLOW}SYSTEM{RESET}]{Style.BRIGHT} Enter your Choice: {Style.NORMAL}")
    if inp == "1":
        ddosattck()
    elif inp == "2":
        portscanner()
    elif inp == "3":
        whoisthis()
    elif inp == "4":
        nmapScan()
    elif inp == "5":
        botnet()
    elif inp == "b":
        main()
    else:
        networkoptions()


def editconfig():
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Edit Config
    """)
    inp = input(f"{Style.BRIGHT}[{YELLOW}SYSTEM{RESET}] New MultiTool Title: {Style.NORMAL}")
    config["CONSOLE_TITLE"] = config["CONSOLE_TITLE"] = inp

    with open(a + "\MultiTool\config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)

    if config.get("CONSOLE_TITLE", "CONSOLE_TITLE") != "":
        if "CONSOLE_TITLE" and "CONSOLE_TITLE" in config:
            print(f"\r\n{RESET}[{YELLOW}SYSTEM{RESET}] New title set: " + GREEN + config["CONSOLE_TITLE"])
            logger.info(f"New title set: " + config["CONSOLE_TITLE"])


def editconfig2():
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Edit Config
    """)
    inp = input(f"{Style.BRIGHT}[{YELLOW}SYSTEM{RESET}] New MultiTool Title: {Style.NORMAL}")
    config["CONS_LOGIN_MANGER_TITLE"] = config["CONS_LOGIN_MANGER_TITLE"] = inp

    with open(a + "\MultiTool\config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)

    if config.get("CONS_LOGIN_MANGER_TITLE", "CONS_LOGIN_MANGER_TITLE") != "":
        if "CONS_LOGIN_MANGER_TITLE" and "CONS_LOGIN_MANGER_TITLE" in config:
            print(f"\r\n{RESET}[{YELLOW}SYSTEM{RESET}] New title set: " + GREEN + config["CONS_LOGIN_MANGER_TITLE"])
            logger.info(f"new LoginManger title set: " + config["CONS_LOGIN_MANGER_TITLE"] + "\r")


def editjson():
    os.system("cls")
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Edit Config
            
            {RESET}{Style.BRIGHT}[{RED}1{RESET}] {YELLOW}Change MultiTool Title{RESET} >{Style.NORMAL}
            {Style.BRIGHT}[{RED}2{RESET}] {YELLOW}Change LoginManger Title{RESET} >{Style.NORMAL}
            
            {Style.BRIGHT}[{RED}b{RESET}] {YELLOW}Back to menu !{RESET} >{Style.NORMAL}
            
            
    """)
    inp = input(f"{Style.BRIGHT}[{YELLOW}SYSTEM{RESET}] What will u do: {Style.NORMAL}")
    if inp == "1":
        editconfig()
    elif inp == "2":
        editconfig2()
    elif inp == "b":
        configs()
    else:
        editjson()


def createnewuser():
    os.system("cls")
    print(f"""
        {RED}
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
            \/ Create New User
            
    """)
    userinp = input(f"{Style.BRIGHT}[{YELLOW}SYSTEM{RESET}] new username: {Style.NORMAL}")
    passinp = getpass.getpass(f"{Style.BRIGHT}[{YELLOW}SYSTEM{RESET}] new passwort: {Style.NORMAL}")
    logger.info(f"New user was created {userinp}")
    logger.info(f"New password was created {passinp}\r")
    data = hashlib.md5(userinp.encode("utf-8"))
    userinphex = data.hexdigest()
    data1 = hashlib.md5(passinp.encode("utf-8"))
    passinphex = data1.hexdigest()

    config["LOGIN_NAME"] = config["LOGIN_NAME"] = userinphex
    config["LOGIN_PASSWORT"] = config["LOGIN_PASSWORT"] = passinphex

    with open(a + "\MultiTool\config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)
    if config.get("LOGIN_NAME", "LOGIN_PASSWORT") != "":
        if "LOGIN_NAME" and "LOGIN_PASSWORT" in config:
            print(
                f"\r\n{RESET}[{YELLOW}INFO{RESET}] Your username and password are currently being encrypted !\r\n")
            sleep(2)
            print(
                f"{RESET}[{YELLOW}INFO{RESET}] Please remember your password and your username, you can't change it anymore !")
            sleep(2)
            print(f"\r\n{RESET}[{YELLOW}LoginManger{RESET}] User has been created: " + GREEN + config["LOGIN_NAME"])
            print(f"{RESET}[{YELLOW}LoginManger{RESET}] Password for user has been created: " + GREEN + config[
                "LOGIN_PASSWORT"])
            logger.info(f"user Hash: " + config["LOGIN_NAME"])
            logger.info(f"passwort Hash: " + config["LOGIN_PASSWORT"])
            sleep(3)
            configs()


def configs():
    os.system("cls")
    print(f"""
    {RED}
   _____        .__   __  .__  ___________           .__   
  /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
 /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
/    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
\____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
        \/ Config Options
        {RESET}
        
        {Style.BRIGHT}[{RED}1{RESET}] {YELLOW}Edit Config{RESET} >{Style.NORMAL}
        {Style.BRIGHT}[{RED}2{RESET}] {YELLOW}Create new user{RESET} >{Style.NORMAL}
        
        {Style.BRIGHT}[{RED}b{RESET}] {YELLOW}Back to menu{RESET}{Style.NORMAL}
{RESET}   
    """)
    inp = input(f"{Style.BRIGHT}[{YELLOW}SYSTEM{RESET}] Enter your Choice: {Style.NORMAL}")
    if inp == "1":
        editjson()
    elif inp == "2":
        createnewuser()
    elif inp == "b":
        main()
    else:
        configs()


def main():
    logger.info(f"MultiTool has started !")
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    os.system("cls")
    print(f"""
    {RED}
   _____        .__   __  .__  ___________           .__   
  /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
 /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
/    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
\____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
        \/{RESET}                                                


        {Style.BRIGHT}[{RED}1{RESET}] {YELLOW}Self Options{RESET} >{Style.NORMAL}
        {Style.BRIGHT}[{RED}2{RESET}] {YELLOW}Network Options{RESET} >{Style.NORMAL}

        {Style.BRIGHT}[{RED}S{RESET}]{YELLOW} Config{RESET} [{RED}Q{RESET}]{YELLOW} Quit Menu{RESET} [{RED}C{RESET}]{YELLOW} Credit{Style.NORMAL}
        {RESET}
    """)
    inp = input(f"{Style.BRIGHT}\r\n[{YELLOW}SYSTEM{RESET}] Enter your Choice:{GREEN} {Style.NORMAL}")
    if inp == "1":
        selfoptions()
    elif inp == "2":
        networkoptions()
    elif inp == "s":
        configs()
    elif inp == "c":
        credits()
    elif inp == "q":
        exit()
    else:
        main()


def create_acc():
    if config.get("LOGIN_NAME") == "":
        os.system("cls")
        print(f"[{YELLOW}INFO{RESET}] Hey I see you're new. Here you can create your own user ! ")
        print(f"[{YELLOW}INFO{RESET}] Please do {RED}not edit the config{RESET} I'll do everything ")
        sleep(5)
        input(f"[{YELLOW}INFO{RESET}] Press any key to skip !")
        os.system("cls")
        key = input(f"[{YELLOW}LoginManger{RESET}] Create User:{GREEN} ")
        key1 = getpass.getpass(f"{RESET}[{YELLOW}LoginManger{RESET}] Create Passwort:{GREEN} ")
        logger.info(f"New created Account: {key}")
        logger.info(f"New created Passwort: {key1}\r")
        data = hashlib.md5(key.encode("utf-8"))
        dig = data.hexdigest()
        data1 = hashlib.md5(key1.encode("utf-8"))
        dig1 = data1.hexdigest()

        config["LOGIN_NAME"] = config["LOGIN_NAME"] = dig
        config["LOGIN_PASSWORT"] = config["LOGIN_PASSWORT"] = dig1

        with open(a + "\MultiTool\config.json", "w") as outfile:
            json.dump(config, outfile, indent=4)
        if config.get("LOGIN_NAME", "LOGIN_PASSWORT") != "":
            if "LOGIN_NAME" and "LOGIN_PASSWORT" in config:
                print(
                    f"\r\n{RESET}[{YELLOW}INFO{RESET}] Your username and password are currently being encrypted !\r\n")
                sleep(2)
                print(
                    f"{RESET}[{YELLOW}INFO{RESET}] Please remember your password and your username, you can't change it anymore !")
                sleep(2)
                print(f"\r\n{RESET}[{YELLOW}LoginManger{RESET}] User has been created: " + GREEN + config["LOGIN_NAME"])
                print(f"{RESET}[{YELLOW}LoginManger{RESET}] Password for user has been created: " + GREEN + config[
                    "LOGIN_PASSWORT"])
                logger.info(f"Account Hash: {dig}")
                logger.info(f"Passwort Hash: {dig1}\r")
                sleep(3)
                print(
                    f"\r\n{RESET}[{YELLOW}INFO{RESET}]{GREEN} Everything ready{RESET} ! Now you can restart the script")
                input(f"\r\n {RED}Press key to exit {RESET}!")
            else:
                print(f"[{YELLOW}LoginManger{RESET}] {RED}Key not exist{RESET} !")
                sleep(5)
                exit()
        else:
            print(f"[{YELLOW}LoginManger{RESET}] {RED}Error{RESET} ! The config file has an error. User or password "
                  f"could not be created. "
                  f"Please contact the "
                  f"author !")
            logger.error(f"Config file Error")
            input("")
    else:
        print(
            f"[{YELLOW}LoginManger{RESET}] {RED}Error{RESET} ! The config file has an error. Please contact the author !")
        logger.error(f"Config file Error")
        input("")


def login_manager():
    ctypes.windll.kernel32.SetConsoleTitleW(login_manger_title)
    os.system("cls")
    print(f"""{RED}
    
    .____                 .__            _____                                      
    |    |    ____   ____ |__| ____     /     \ _____    ____    ____   ___________ 
    |    |   /  _ \ / ___\|  |/    \   /  \ /  \ __  \  /    \  / ___\_/ __ \_  __ |
    |    |__(  <_> ) /_/  >  |   |  \ /    Y    \/ __ \|   |  \/ /_/  >  ___/|  | \/
    |_______ \____/\___  /|__|___|  / \____|__  (____  /___|  /\___  / \___  >__|   
            \/    /_____/         \/          \/     \/     \//_____/      \/       
    {RESET}
        """)

    log_inp = input(f"{Style.BRIGHT}[{YELLOW}LoginManger{RESET}] Login: {Style.NORMAL}")
    data = hashlib.md5(log_inp.encode("utf-8"))
    dig_log = data.hexdigest()
    if dig_log == login:
        log_pwd_inp = getpass.getpass(f"{Style.BRIGHT}[{YELLOW}LoginManger{RESET}] Passwort: {Style.NORMAL}")
        data1 = hashlib.md5(log_pwd_inp.encode("utf-8"))
        dig_pwd = data1.hexdigest()
        if dig_pwd == login_pwd:
            print(f"{Style.BRIGHT}[{YELLOW}LoginManger{RESET}] {GREEN}You are logged in{RESET} !{Style.NORMAL}")
            logger.info(f"{log_inp} has logged in")
            sleep(2)
            system("cls")
            main()
        else:
            print(f"{Style.BRIGHT}[{YELLOW}LoginManger{RESET}] {RED}Wrong Passwort{RESET} !{Style.NORMAL}")
            sleep(2)
            logger.error(f"Wrong password")
            system("cls")
            login_manager()
    else:
        print(f"{Style.BRIGHT}[{YELLOW}LoginManger{RESET}] {RED}This username doesn't exist{RESET} !{Style.NORMAL}")
        sleep(2)
        system("cls")
        logger.error(f"This username doesnt exist ! Please create one")
        login_manager()



response = requests.get("https://github.com/Shiggyyy/MultiTool/blob/main/update.json")
data = response.text
values = json.loads(data)
c = values.get("config")



def start():
    try:
        if config.get("LOGIN_NAME") != "":     
            login_manager()
        else:
            create_acc()

    except NameError:
        print(f"{Style.BRIGHT}[{YELLOW}SETUP{RESET}] Please Wait ! I'm getting everything ready for you {Style.NORMAL}")
        sleep(1)
        print(f"{Style.BRIGHT}\r\n[{YELLOW}SETUP{RESET}] {GREEN}Download config{RESET}{Style.NORMAL}")
        sleep(3)
        print(f"{Style.BRIGHT}\r\n[{YELLOW}SETUP{RESET}] {GREEN}Ready{RESET} ! Restart !{Style.NORMAL}")
        sleep(2)
        input(f"[{YELLOW}SYSTEM{RESET}] Press any key")

    except KeyboardInterrupt as key_int:
        os.system("cls")
        logger.info(f"[EXIT] !")
        input(RED + f"""
       _____        .__   __  .__  ___________           .__   
      /     \  __ __|  |_/  |_|__| \__    _______   ____ |  |  
     /  \ /  \|  |  |  |\   __|  |   |    | /  _ \ /  _ \|  |  
    /    Y    |  |  |  |_|  | |  |   |    |(  <_> (  <_> |  |__
    \____|__  |____/|____|__| |__|   |____| \____/ \____/|____/
        {RESET}{Style.BRIGHT}[{RED}!{RESET}] {RED}KeyboardInterrupt{RESET} !{Style.NORMAL}
        """ + RESET)


def check_update():
    if ver == c:
        start()
    else:
        if os.path.exists(a + "/MultiTool/update.py"):
            subprocess.call(a + "/MultiTool/update.py") 
        else:
            downloadU = requests.get(download_update, allow_redirects=True)
            path2 = os.path.join(a)
            open(path2 + "/MultiTool/update.py", "wb").write(downloadU.content)
            sleep(4)
            subprocess.call(a + "/MultiTool/update.py") 


if __name__ == "__main__":
    check_update()