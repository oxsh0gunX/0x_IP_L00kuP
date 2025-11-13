#!/usr/bin/env python3

# =============================================
#   0x_IP_L00kuP - Main Tool
#   Created by: 0xSh0gunX 🛡️
# =============================================

import requests

def get_ip_info(ip_address):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)

        if response.status_code != 200:
            print("Error: Unable to fetch data.")
            return

        data = response.json()

        print("\n===== 0x_IP_L00kuP (by 0xSh0gunX) =====")
        print(f"IP Address     : {data.get('ip', 'N/A')}")
        print(f"City           : {data.get('city', 'N/A')}")
        print(f"Region         : {data.get('region', 'N/A')}")
        print(f"Country        : {data.get('country', 'N/A')}")
        print(f"Location       : {data.get('loc', 'N/A')}")
        print(f"Postal Code    : {data.get('postal', 'N/A')}")
        print(f"Timezone       : {data.get('timezone', 'N/A')}")
        print(f"ISP / Org      : {data.get('org', 'N/A')}")
        print("=======================================\n")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("0x_IP_L00kuP Tool by 0xSh0gunX\n")
    ip = input("Enter an IP address: ")
    get_ip_info(ip)
