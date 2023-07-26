from itertools import zip_longest
from threading import Thread
import subprocess
from datetime import datetime
import csv


filename_net = datetime.now().strftime('netspeed-%Y-%m-%d-%H-%M.csv')


timedate = []
download = []
upload = []


cmd4 = ("date +'%s'")
cmd7 = "speedtest-cli | grep -e Download | awk '{print $2}'"
cmd8 = "speedtest-cli | grep -e Upload | awk '{print $2}'"



def get_internet_speed():
    try:
        while True:
            rc, c = subprocess.getstatusoutput(cmd4)
            rc, f = subprocess.getstatusoutput(cmd7)
            rc, g = subprocess.getstatusoutput(cmd8)
            timedate.append(c)
            download.append(f)
            upload.append(g)
            with open(filename_net, "w+") as f_output:
                csv_output = csv.writer(f_output)
                csv_output.writerow(["epoch_time", "net_dload", "net_upload"])
                csv_output.writerows(zip_longest(timedate , download, upload))
            print (c, f,g)
    except:
        pass


if __name__== "__main__":

    get_internet_speed()


