import os
import sys
from time import sleep


def get_lxc_ids():
    containers = os.system("pct list | tail -n +2 | cut -f1 -d' '")
    cont = containers.split('')
    return cont


def get_container_status(lxc_id: int):
    return os.system(f"pct status {lxc_id}")


def start_container(lxc_id: int):
    os.system(f"pct start {lxc_id}")
    sleep(5)
    return


def stop_container(lxc_id: int):
    os.system(f"pct stop {lxc_id}")
    sleep(5)
    return


def exec_command(lxc_id: int, command: str, start_if_stopped=True):
    container_status = get_container_status(lxc_id)
    stopped = False
    if container_status == "status: stopped" and start_if_stopped:
        stopped = True
        start_container(lxc_id)
    cmdoutput = os.system(f"pct exec {id} {command}")
    if stopped:
        stop_container(lxc_id)
    return cmdoutput


def pick_command():
    valid_options = ['1', 'c']
    print("""
    [1] Apt-Get Update & Upgrade
    
    [c] Custom Command
    """)
    selection = input("Which Option?: ")
    if selection not in valid_options:
        exit("Invalid Selection")
    return selection


def pick_container():
    containers = get_lxc_ids()
    print(os.system("pct list"))

    user = input("Containers?:")
    if user.lower() == "all":
        user = containers
    else:
        user = user.split(" ")
    return user


def main():
    selection = pick_command()
    containers = pick_container()
    print(selection, containers)


