from itertools import zip_longest
import subprocess
from datetime import datetime
import csv
import psutil
import glob
import shutil
import os

filename_cpu = "/path/to/folder/mem_cpu_monitor/" + datetime.now().strftime('cpu_mem-%Y-%m-%d-%H-%M-%S.csv')


timedate = []
cpu = []
ram = []
diskavail = []
swap = []

cmd_ram = "free -m | head -2 | tail -1 | awk '{print $3}'"
cmd_timestamp = ("date +'%s'")
cmd_diskspace = "df -h | head -4 | tail -1 | awk '{print $5}' | sed 's/.$//'"
cmd_swap = "vmstat -s | grep 'used swap' | awk '{print $1}'"

source = "/path/to/folder/mem_cpu_monitor/"
dest = "/path/to/folder/mem_cpu_monitor/older_files/"

files=os.listdir(source)
print(files)

def move_older_files():
    try:
        for file in files:
            if (file.endswith(".csv") or file.endswith(".html")):
   	         shutil.move(file,dest)
    except:
        print("no csv to move")

def get_mem_cpu():
    try:
        while True:
            a = psutil.cpu_percent(4)
            rc, b = subprocess.getstatusoutput(cmd_ram)
            rc, c = subprocess.getstatusoutput(cmd_timestamp)
            rc, d = subprocess.getstatusoutput(cmd_diskspace)
            rc, e = subprocess.getstatusoutput(cmd_swap)
            timedate.append(c)
            cpu.append(a)
            ram.append(b)
            diskavail.append(d)
            swap.append(e)
            with open(filename_cpu, "w+") as f_output:
                csv_output = csv.writer(f_output)
                csv_output.writerow(["epoch_time", "cpu_avg(%)","ram_active(G)","disk_space_used(%)", "swap_used(M)"])
                csv_output.writerows(zip_longest(timedate , cpu, ram, diskavail, swap))
            print (c,a, b,d,e)
    except:
        pass



if __name__== "__main__":
    move_older_files()
    get_mem_cpu()
