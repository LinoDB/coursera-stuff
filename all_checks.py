#!/usr/bin/env python3

import os
import shutil
import sys
import socket

"""Something
else"""

"""Some more stuffs"""

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    everything_ok = True
    checks=[
        (check_reboot, "Pending reboot"),
        (check_root_full, "Root partition full"),
        (check_no_network, "No working network")
    ]
    for check, msg in checks:
        if check():
            print(msg)
            everythink_ok = False

    if not everything_ok:
        sys.exit(1)
    print("Everything ok")
    sys.exit(0)

if __name__ == "__main__":
   main()
