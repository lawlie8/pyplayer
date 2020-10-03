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

    def play_songs(arg):
        global media_palyer
        media_palyer = vlc.MediaPlayer()
        media = vlc.Media(r'C:\Users\Lawlie8\Downloads\Music\gotta_friend_in_me.mp3')
        media_palyer.set_media(media)
        media_palyer.audio_set_volume(70)
        media_palyer.play()
        return media_palyer

    def get_volume(media_palyer):
        media_palyer = vlc.MediaPlayer()
        media_palyer.audio_set_volume(70)
        media_palyer.play()

    def stop(arg):
        print('stop')


    def next(arg):
        print('next')


    def prev(arg):
        print('prev')


    def pause(arg):
        pyplayer.play_songs(arg)
        print('pause')

    #def get_volume(arg):
    #    print(arg)

    def fname(arg):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        window = tk.Tk()
        window.tk.call('tk', 'scaling', 2.0)
        window.geometry("1224x720")
        window.title("pyplayer")
        window.configure(bg='#333338')
        window.iconbitmap('assets/py_icon.ico')
        mycanvas = tk.Canvas(window,bg="#7f7278",height=150,bd='0',highlightthickness=0)
        mycanvas.pack(anchor='w',fill='x')
        next_button = PhotoImage(file='assets/next.png')
        next_button = next_button.subsample(2,2) #reduced size of image
        prev_button = PhotoImage(file='assets/prev.png')
        prev_button = prev_button.subsample(2,2)
        stop_button = PhotoImage(file='assets/stop.png')
        stop_button = stop_button.subsample(2,2)
        pause_button = PhotoImage(file='assets/pause.png')
        pause_button = pause_button.subsample(2,2)
        pause_button_label = tk.Label(image=pause_button,bg="#7f7278")
        prev_button_label = tk.Label(image=prev_button,bg="#7f7278")
        next_button_label = tk.Label(image=next_button,bg="#7f7278")
        stop_button_label = tk.Label(image=stop_button,bg="#7f7278")
        ll = [[stop_button_label,pyplayer.stop],[prev_button_label,pyplayer.prev],[next_button_label,pyplayer.next],[pause_button_label,pyplayer.pause]]
        vol_var = tk.DoubleVar()
        vol = tk.Scale(mycanvas,variable=vol_var,command=pyplayer.get_volume,troughcolor='#7f7278',width='10',from_=0,to=100,bg='#7f7278',resolution=1,orient='horizontal',length=100,bd=0,showvalue=False,sliderlength=30)
        vol.pack(anchor='se',side='bottom',pady=70,padx=10)

        for i in ll:
            i[0].pack()
            i[0].bind('<Button-1>',i[1])

        #co-ordinates for buttons  change here
        mycanvas.create_window(300,70,window=pause_button_label,anchor='c')
        mycanvas.create_window(100,70,window=stop_button_label,anchor='c')
        mycanvas.create_window(200,70,window=prev_button_label,anchor='c')
        mycanvas.create_window(400,70,window=next_button_label,anchor='c')
        # TODO: add control buttons int the canvas

        window.mainloop()
        return window



k = pyplayer()
k.fname()
k.initilise()
