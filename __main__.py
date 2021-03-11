import os
import sys

def get_lxc_ids():
    return os.system("pct list | tail -n +2 | cut -f1 -d' '")


def get_container_status(id: int):
    return os.system(f"pct status {id}")


def exec_command(id: int, command: str):
    return os.system(f"pct exec {id} {command}")

def main():
    print("""
    [1] Apt-Get Update & Upgrade
    
    [c] Custom Command
    """)
    selection = input("Which Option?: ")
    if selection == "1":
        pass
    elif selection == "c":
        pass
    else:
        print("Invalid Selection")
