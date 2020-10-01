#!/usr/bin/python3
import ctypes
import tkinter as tk
from tkinter import *
import os
import sys
import vlc
class pyplayer(object):
    """docstring forpyplayer."""
    def initilise(arg):
        #os.chdir('/')
        #os.system('ls')
        os.system('mkdir .pyplayerdata')

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
        window.mainloop()
        return window



k = pyplayer()
k.fname()
k.initilise()
