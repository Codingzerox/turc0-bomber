import socket
import time
import sys
import os
from colorama import init, Fore, Style
import random

init(autoreset=True)

banners = [
r"""
  █████                                     █████   
 ░░███                                    ███░░░███ 
 ███████   █████ ████ ████████   ██████  ███   ░░███
░░░███░   ░░███ ░███ ░░███░░███ ███░░███░███    ░███
  ░███     ░███ ░███  ░███ ░░░ ░███ ░░░ ░███    ░███
  ░███ ███ ░███ ░███  ░███     ░███  ███░░███   ███ 
  ░░█████  ░░████████ █████    ░░██████  ░░░█████░  
   ░░░░░    ░░░░░░░░ ░░░░░      ░░░░░░     ░░░░░░   
""",
r"""
     __                  ____ 
  / /___  ____________/ __ \\
 / __/ / / / ___/ ___/ / / /
/ /_/ /_/ / /  / /__/ /_/ / 
\\__/\\__,_/_/   \\___/\\____/  
""",
r"""
_____                    _______ 
__  /____  ________________  __ \\
_  __/  / / /_  ___/  ___/  / / /
/ /_ / /_/ /_  /   / /__ / /_/ / 
\\__/ \\__,_/ /_/    \\___/ \\____/  
"""
]

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_animated_banner(banner):
    clear()
    lines = banner.splitlines()
    for line in lines:
        color = random.choice(colors)
        print(color + line)
        time.sleep(0.1)
    time.sleep(1)

def port_scanner(target, start_port=1, end_port=1024):
    print(f"\n{Fore.CYAN}Scanning ports on {target} from {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{Fore.GREEN}[+] Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("\nExiting program.")
            sys.exit()
        except socket.gaierror:
            print(f"\n{Fore.RED}Hostname could not be resolved.")
            sys.exit()
        except socket.error:
            print(f"\n{Fore.RED}Couldn't connect to server.")
            sys.exit()
    print(f"\n{Fore.YELLOW}Scan completed.")

def main():
    for banner in banners:
        print_animated_banner(banner)

    target = input(Fore.WHITE + "Enter target IP or hostname: ")
    port_scanner(target)

if __name__ == "__main__":
    main()
