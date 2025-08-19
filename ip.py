import socket
import requests
import ipaddress
import netifaces
import os
import pyfiglet
from termcolor import colored
from colorama import init
import sys

init(autoreset=True)

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def header():
    ascii_banner = pyfiglet.figlet_format("Nebulon IP-Checker")
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    for i, line in enumerate(ascii_banner.split("\n")):
        print(colored(line, colors[i % len(colors)]))

    print(colored("Author : BJS611 (https://github.com/BJS611)", "yellow"))

def exit_message():
    clear()
    colors = ["red", "yellow", "green", "cyan", "magenta"]
    msg = "Program Has Stopped"
    for i, char in enumerate(msg):
        print(colored(char, colors[i % len(colors)]), end="")
    print("\n")
    sys.exit(0)



def check_local_ip():
    clear()
    try:
        print(colored("[ LAN Interface IP Information ]", "cyan"))

        interfaces = netifaces.interfaces()
        found = False
        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface)

            if netifaces.AF_INET in addrs:
                for link in addrs[netifaces.AF_INET]:
                    ip = link.get('addr')
                    netmask = link.get('netmask')
                    if ip and not ip.startswith("127."):  # skip localhost
                        found = True
                        print("Interface :", colored(iface, "yellow"))
                        print("IP Address:", colored(ip, "green"))
                        print("Netmask   :", colored(netmask, "magenta"))
                        print("-" * 35)

        if not found:
            print(colored("No LAN IP address found.", "red"))

        input(colored("\nPress Enter to return to menu...", "magenta"))
    except (KeyboardInterrupt, EOFError):
        exit_message()

def check_public_ip():
    clear()
    try:
        public_ip = requests.get("https://api.ipify.org").text
        print(colored("[ Public IP Information ]", "cyan"))
        print("Public IP:", colored(public_ip, "green"))
        input(colored("\nPress Enter to return to menu...", "magenta"))
    except (KeyboardInterrupt, EOFError):
        exit_message()
    except Exception as e:
        print(colored("Error fetching public IP:", "red"), e)
        input(colored("\nPress Enter to return to menu...", "magenta"))

def validate_ip():
    clear()
    try:
        ip = input(colored("Enter IP address to validate: ", "yellow"))
        ipaddress.ip_address(ip)
        print(colored(f"{ip} is a valid IP address.", "green"))
        input(colored("\nPress Enter to return to menu...", "magenta"))
    except ValueError:
        print(colored("Invalid IP address.", "red"))
        input(colored("\nPress Enter to return to menu...", "magenta"))
    except (KeyboardInterrupt, EOFError):
        exit_message()

def ip_details():
    clear()
    try:
        ip = input(colored("Enter IP address to get info: ", "yellow"))
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url).json()
        print(colored("[ IP Details ]", "cyan"))
        if res["status"] == "success":
            print("IP       :", colored(res["query"], "green"))
            print("Country  :", colored(res["country"], "yellow"))
            print("Region   :", colored(res["regionName"], "yellow"))
            print("City     :", colored(res["city"], "yellow"))
            print("ISP      :", colored(res["isp"], "magenta"))
            print("Org      :", colored(res["org"], "magenta"))
            print("Lat/Lon  :", colored(f"{res['lat']}, {res['lon']}", "blue"))
        else:
            print(colored("Could not retrieve details for that IP.", "red"))
        input(colored("\nPress Enter to return to menu...", "magenta"))
    except (KeyboardInterrupt, EOFError):
        exit_message()
    except Exception as e:
        print(colored("Error:", "red"), e)
        input(colored("\nPress Enter to return to menu...", "magenta"))

def check_gateway():
    clear()
    try:
        print(colored("[ Default Gateway ]", "cyan"))
        gateways = netifaces.gateways()
        if 'default' in gateways and netifaces.AF_INET in gateways['default']:
            gw = gateways['default'][netifaces.AF_INET][0]
            print("Default Gateway:", colored(gw, "green"))
        else:
            print(colored("No default gateway found.", "red"))
        input(colored("\nPress Enter to return to menu...", "magenta"))
    except (KeyboardInterrupt, EOFError):
        exit_message()

def scan_ports():
    clear()
    try:
        target = input(colored("Enter target IP: ", "yellow"))
        start = int(input(colored("Start port: ", "yellow")))
        end = int(input(colored("End port: ", "yellow")))

        print(colored(f"\n[ Scanning {target} ports {start}-{end} ]", "cyan"))
        for port in range(start, end + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(colored(f"Port {port} is OPEN", "green"))
            s.close()
        input(colored("\nPress Enter to return to menu...", "magenta"))
    except (KeyboardInterrupt, EOFError):
        exit_message()

def main_menu():
    try:
        while True:
            clear()
            header()
            print(colored("=================================", "yellow"))
            print(colored("1) Show LAN IP (Interfaces)", "cyan"))
            print(colored("2) Show Public IP", "cyan"))
            print(colored("3) Validate IP Address", "cyan"))
            print(colored("4) Get IP Details", "cyan"))
            print(colored("5) Show Default Gateway", "cyan"))
            print(colored("6) Scan Ports on IP", "cyan"))
            print(colored("0) Exit", "red"))
            print(colored("=================================", "yellow"))

            choice = input(colored("Select an option: ", "magenta"))

            if choice == "1":
                check_local_ip()
            elif choice == "2":
                check_public_ip()
            elif choice == "3":
                validate_ip()
            elif choice == "4":
                ip_details()
            elif choice == "5":
                check_gateway()
            elif choice == "6":
                scan_ports()
            elif choice == "0":
                exit_message()
            else:
                print(colored("Invalid option. Try again.", "red"))
                input(colored("\nPress Enter to continue...", "magenta"))
    except (KeyboardInterrupt, EOFError):
        exit_message()

if __name__ == "__main__":
    main_menu()
