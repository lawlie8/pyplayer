#!/usr/bin/python3
import ctypes
import tkinter as tk
from tkinter import *
import os
import sys
import vlc
import time
import datetime


class pyplayer(object):
    """docstring forpyplayer."""
    def initilise(arg):

        os.system('mkdir .pyplayerdata')

        if os.path.isfile('.pyplayerdata/config.pyplayer'):
            check_file = open('config.pyplayer','w+')
            data = {"version":"1.0","platform":sys.platform,"author":"lawlie8","last_modified":str(datetime.date.today())+"/"+time.strftime("%H:%M:%S",time.localtime())}
            check_file.write(str(data))
        else:
            check_file = open('config.pyplayer','w+')

        pass

    def check_for_playlist(arg):
        play_list = open('current')

        pass


    def fname(arg):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        window = tk.Tk()
        window.tk.call('tk', 'scaling', 2.0)
        window.geometry("1024x720")
        window.title("pyplayer")
        window.configure(bg='#333338')
        window.iconbitmap('assets/py_icon.ico')
        mycanvas = tk.Canvas(window,bg="#333338",height=150,bd='0',highlightthickness=0)
        mycanvas.pack(anchor='w',fill='x')
        # TODO: add control buttons int the canvas
        window.mainloop()
        return window



k = pyplayer()
k.fname()
k.initilise()
