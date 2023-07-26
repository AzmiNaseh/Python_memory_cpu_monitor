import plotly.express as px
import pandas as pd
from datetime import datetime
import math
import datetime as dt
today = datetime.now()
import glob
import os

list_of_files = glob.glob('/home/ubuntu/mem_cpu_monitor/cpu_mem-*') 

os.system("mv /home/ubuntu/mem_cpu_monitor/*.html /home/ubuntu/mem_cpu_monitor/older_files")

#latest_file = max(list_of_files, key=os.path.getmtime)
latest_file = "/home/ubuntu/mem_cpu_monitor/cpu_mem-2023-01-11-13-31-33.csv"
print('Lastest cpu_mem csv file is'+ latest_file)   



def plot_cpu():
    df = pd.read_csv(latest_file)
    CPU_AVG = round(df["cpu_avg(%)"].mean(), 2)
    MEM_AVG = round(df["ram_active(G)"].mean()/1024,2)  
    df['ram_active(G)'] = df['ram_active(G)']/1024
    df['swap_used(M)'] = df['swap_used(M)']/1024
    df["time"] = df['epoch_time'] = [dt.datetime.fromtimestamp(t) for t in df.epoch_time]
    
    fig = px.line(df, x = 'time', y = ['cpu_avg(%)', 'ram_active(G)','disk_space_used(%)','swap_used(M)'], title="<b>MEM_CPU_PLOT               CPU_AVG= {}(%)  MEM_AVG={}(G)</b>".format(CPU_AVG, MEM_AVG))
    fig.write_html("/home/ubuntu/mem_cpu_monitor/cpu_mem_mpr_"+today.strftime('%Y-%m-%d_%H-%M-%S')+".html", full_html=False, include_plotlyjs='cdn')
    fig.show()

def plot_netspeed():   
    list_of_files = glob.glob('/home/ubuntu/personal_workspace/cpu_mem_disk/netspeed-*')  
    latest_file = max(list_of_files, key=os.path.getmtime)
    if list_of_files:
        print('Lastest netspeed csv file is' , list_of_files)
        df = pd.read_csv(latest_file)
        UP_AVG = round(df["net_upload"].mean(),2)
        DOWN_AVG = round(df["net_dload"].mean(),2)
        df["time"] = df['epoch_time'] = [dt.datetime.fromtimestamp(t) for t in df.epoch_time]
        fig = px.line(df, x = 'time', y = ['net_dload','net_upload'], title="<b>INTERNET SPEED PLOT                   UP_AVG= {}(Mbps)  DOWN_AVG={}(Mbps)</b>".format(UP_AVG, DOWN_AVG))
        fig.write_html("netspeed_"+today.strftime('%Y-%m-%d_%H-%M-%S')+".html")
        fig.show()

    else:
        ('not available')

if __name__ == "__main__":
    plot_cpu()
#    plot_netspeed()
