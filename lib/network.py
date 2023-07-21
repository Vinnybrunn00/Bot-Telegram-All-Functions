import requests
from tkinter import messagebox
import subprocess
import sys

url = 'https://google.com'

def CheckNetwork(timeout:str):
    """check connection"""
    try:
        requests.get(url=url, timeout=timeout)
    except requests.exceptions.ConnectionError:
        platform = subprocess.check_output(['uname', '-o'], encoding='cp860')
        for sistema in platform.split('\n'):
            if 'Android' in sistema:
                print('Connect Network Error')
                sys.exit()
            else:
                messagebox.showinfo(
                title='HTTPSConnectionPool Error',message='Connect Network Error')
                sys.exit()
