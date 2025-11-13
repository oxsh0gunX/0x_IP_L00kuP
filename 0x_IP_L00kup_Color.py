#!/usr/bin/env python3

# =============================================
#   0x_IP_L00kuP - Color Edition
#   Made by: 0xSh0gunX 🛡️
# =============================================

import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

banner = f"""
{Fore.CYAN}
██████╗  ██╗ ██████╗      
██╔══██╗███║██╔════╝      
██████╔╝╚██║██║  ███╗     
██╔══██╗ ██║██║   ██║     
██████╔╝ ██║╚██████╔╝     
╚═════╝  ╚═╝ ╚═════╝       

   {Fore.GREEN}0x_IP_L00kuP
   {Fore.YELLOW}By 0xSh0gunX 🛡️
"""

for line in banner.split("\n"):
    print(line)
    time.sleep(0.05)


def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    r = requests.get(url)

    if r.status_code != 200:
        print(Fore.RED + "Error: Unable to fetch IP info")
        return
    
    data = r.json()
    print(Fore.MAGENTA + "\n========= IP Information =========")
    print(Fore.CYAN + f"IP Address     : {data.get('ip')}")
    print(f"City           : {data.get('city')}")
    print(f"Region         : {data.get('region')}")
    print(f"Country        : {data.get('country')}")
    print(f"Location       : {data.get('loc')}")
    print(f"Postal Code    : {data.get('postal')}")
    print(f"Timezone       : {data.get('timezone')}")
    print(f"ISP / Org      : {data.get('org')}")
    print(Fore.MAGENTA + "==================================\n")


if __name__ == "__main__":
    ip = input(Fore.YELLOW + "Enter an IP: ")
    get_ip_info(ip)
