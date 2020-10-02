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
            current_playlist = check_file.readlines()[0]
            check_file.write(str(current_playlist+"\n"+data))
        else:
            data = {"version":"1.0","platform":sys.platform,"author":"lawlie8","last_modified":str(datetime.date.today())+"/"+time.strftime("%H:%M:%S",time.localtime())}
            check_file = open('.pyplayerdata/config.pyplayer','w+')
            check_file.write('global_playlist\n'+data)
        pass

    def check_for_global_playlist(arg):
        check_file = open('.pyplayerdata/config.pyplayer')
        return check_file.readlines()[0]

    def stop(arg):
        print('stop')
    def next(arg):
        print('next')
    def prev(arg):
        print('prev')
    def pause(arg):
        print('pause')



    def fname(arg):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        window = tk.Tk()
        window.tk.call('tk', 'scaling', 2.0)
        window.geometry("1224x720")
        window.title("pyplayer")
        window.configure(bg='#333338')
        window.iconbitmap('assets/py_icon.ico')
        mycanvas = tk.Canvas(window,bg="#333338",height=150,bd='0',highlightthickness=1)
        mycanvas.pack(anchor='w',fill='x')
        next_button = PhotoImage(file='assets/next.png')
        next_button = next_button.subsample(2,2) #reduced size of image
        prev_button = PhotoImage(file='assets/prev.png')
        prev_button = prev_button.subsample(2,2)
        stop_button = PhotoImage(file='assets/stop.png')
        stop_button = stop_button.subsample(2,2)
        pause_button = PhotoImage(file='assets/pause.png')
        pause_button = pause_button.subsample(2,2)
        pause_button_label = tk.Label(image=pause_button,bg="#333338")
        prev_button_label = tk.Label(image=prev_button,bg="#333338")
        next_button_label = tk.Label(image=next_button,bg="#333338")
        stop_button_label = tk.Label(image=stop_button,bg="#333338")
        stop_button_label.pack()
        prev_button_label.pack()
        next_button_label.pack()
        pause_button_label.pack()
        pause_button_label.bind('<Button-1>',pyplayer.pause)
        stop_button_label.bind('<Button-1>',pyplayer.stop)
        prev_button_label.bind('<Button-1>',pyplayer.prev)
        next_button_label.bind('<Button-1>',pyplayer.next)

        #co-ordinates for buttons  change here
        mycanvas.create_window(1090,70,window=pause_button_label,anchor='e')
        mycanvas.create_window(850,70,window=stop_button_label,anchor='e')
        mycanvas.create_window(990,70,window=prev_button_label,anchor='e')
        mycanvas.create_window(1190,70,window=next_button_label,anchor='e')
        # TODO: add control buttons int the canvas
        window.mainloop()
        return window



k = pyplayer()
k.fname()
k.initilise()
