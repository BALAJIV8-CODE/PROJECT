#!/usr/bin/ python3 

import shutil
import psutil 


# function to check the storage space are have require 
def check_disk_usage(disk):
    space = shutil.disk_usage(disk)
    free = space.free / space.total * 100 
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("Everything is Ok")
