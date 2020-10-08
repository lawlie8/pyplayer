#!/usr/bin/python3
import ctypes
import tkinter as tk
from tkinter import *
import os
from eyed3 import id3
import hashlib
import sys
from PIL import ImageTk, Image
try:
    import vlc
except:
    os.system('pip install python-vlc')
import time
import datetime

class menu_class(object):
    """docstring formenu_class."""

    def __init__(self, arg):
        pass

    def destroy_menu():
        try:
            menu_window.destroy()
            pyplayer.destroy_window()
        except:
            pyplayer.destroy_window()
            pass


    def refresh_playlist_window():
        import glob
        fm = open('.pyplayerdata/file_monitoring.pyplayer','r+')
        global_playlist = open('.pyplayerdata/global_playlist.pyplayer','a+')
        x = fm.read().split('\n')
        for i in x:
            if i!='':
                files = glob.glob(i + '/**/*.mp3', recursive=True)
        for i in files:
            try:
                global_playlist.write(str(i+'\n'))
            except:
                pass
        global_playlist.close()
        pass



    def add_dirs_function():
        from tkinter import filedialog
        enc_file_list = []
        window_filename =  filedialog.askdirectory(initialdir = "/",title = "Select file")
        enc_file_list.append(window_filename)
        dir_files = open(".pyplayerdata/file_monitoring.pyplayer",'a+')
        for dir_list in enc_file_list:
            dir_files.write(dir_list+'\n')
        dir_files.close()
        pass



    def open_menu(arg):
        global menu_window
        menu_window = tk.Tk()
        menu_window.tk.call('tk', 'scaling', 2.0)
        menu_window.geometry("720x720")
        menu_window.title("Menu")
        menu_window.configure(bg='#333338')
        menu_window.iconbitmap('assets/py_icon.ico')
        mylist = Listbox(menu_window,width='90',height='7',bg='white',bd=0,fg='black')#yscrollcommand=enc_file_scroll.set,
        mylist.insert(END,"    +++ Monitoring following dir's +++     ",' ')
        fm = open('.pyplayerdata/file_monitoring.pyplayer','r+')
        #print(fm.read())
        x = fm.read().split('\n')
        for i in x:
            if i != '':
                mylist.insert(END,'      '+i)
        search_files = tk.Label(menu_window,fg='white',text="Monitoring dir's",bg='#333338')
        search_files.pack(padx=20,pady=50,anchor='w')
        mylist.pack(pady=0,anchor='w',padx=50,fill='x')
        refresh_button = tk.Button(menu_window,text='Refresh',activebackground='black',highlightcolor='black',bd=1,relief='flat',height=0,width=10,fg='white',bg='#338237',command=lambda :menu_class.refresh_playlist_window())
        add_dirs_button = tk.Button(menu_window,text='Add dirs',activebackground='black',highlightcolor='black',bd=1,relief='flat',height=0,width=10,fg='white',bg='#338237',command=lambda :menu_class.add_dirs_function())
        add_dirs_button.place(x=50,y=300)
        refresh_button.place(x=150,y=300)
        menu_window.mainloop()
        pass



class pyplayer(object):
    """docstring forpyplayer."""
    def shuffle_list(): #shuffle the list from here come up with a algorithm shit Head
        global_playlist = open('.pyplayerdata/global_playlist.pyplayer','r+').readlines()


    def initilise(arg):
        os.system('mkdir .pyplayerdata')
        if os.path.isfile('.pyplayerdata/file_monitoring.pyplayer'):
            pass
        else:
            fm = open('.pyplayerdata/file_monitoring.pyplayer','a+')
            fm.close()
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

    def destroy_window():
        window.destroy()

    def check_for_global_playlist(arg):
        check_file = open('.pyplayerdata/config.pyplayer')
        return check_file.readlines()[0]

    def __init__(self):
        instance = open('.pyplayerdata/in.txt','w+').write('on')
        print('ss')
        #current_song = r'C:/Users/Lawlie8/Downloads\Music\Santara - Suki.mp3'

    def play_songs(arg):
        media_palyer.audio_set_volume(100)
        media_palyer.play()
        #play_button_label.pack_forget()
        pause_button = PhotoImage(file='assets/pause.png')
        pause_button = pause_button.subsample(2,2)
        pause_button_label = tk.Label(image=pause_button,bg="#7f7278")
        pause_button_label.pack()
        mycanvas.create_window(300,70,window=pause_button_label,anchor='c')
        pause_button_label.bind('<Button-1>',pyplayer.pause)


        #Ignore all errors for the following code, it works

        try:
            mycanvas.update('pause_button_label')
        except:
            mycanvas.update('play_button_label')
        finally:
            print('play')
            #img change doesn't work
            window.bind('<Return>',pyplayer.pause)

    def get_volume(arg):
        print(arg)

    def stop(arg):
        media_palyer.stop()
        play_button = PhotoImage(file='assets/play.png')
        play_button = play_button.subsample(2,2)
        play_button_label = tk.Label(image=play_button,bg="#7f7278")
        play_button_label.pack()
        mycanvas.create_window(300,70,window=play_button_label,anchor='c')
        play_button_label.bind('<Button-1>',pyplayer.play_songs)
        try:
            mycanvas.update('pause_button_label')
        except:
            mycanvas.update('play_button_label')
        finally:
            print('pause')

        print('stop')


    def next(arg):
        print('next')


    def prev(arg):
        print('prev')


    def pause(arg):

        media_palyer.pause()
        #pause_button_label.pack_forget()
        play_button = PhotoImage(file='assets/play.png')
        play_button = play_button.subsample(2,2)
        play_button_label = tk.Label(image=play_button,bg="#7f7278")
        play_button_label.pack()
        mycanvas.create_window(300,70,window=play_button_label,anchor='c')
        play_button_label.bind('<Button-1>',pyplayer.play_songs)
        mycanvas.create_image(460,75,image=img,anchor='w')

        #Ignore all errors for the following code,it works

        try:
            mycanvas.update('pause_button_label')
        except:
            mycanvas.update('play_button_label')
        finally:
            print('pause')
            window.bind('<Return>',pyplayer.play_songs)


    def CurSelect(arg):
        global media_palyer

        value=str(current_mylist.get(current_mylist.curselection())).strip('\n').strip(' ')
        list_file = open('.pyplayerdata/config.pyplayer','r+')
        current_playlist = str(list_file.readlines()[0]).strip('\n')
        song_list = open('.pyplayerdata/'+current_playlist+'.pyplayer','r+').readlines()
        for song,ind in zip(song_list,range(0,len(song_list))):
            if(song.split('\\')[-1].strip('\n')==value):
                to_play = song_list[ind].strip('\n')

        try:#kill me please some one just kill me this sucks i shud have read documentation
            if(open('.pyplayerdata/in.txt','r+').read() == 'on'):
                media_palyer= vlc.MediaPlayer(to_play)
                media_palyer.play()
            else:
                media_palyer.stop()
                media_palyer= vlc.MediaPlayer(to_play)
                media_palyer.play()
            print('s')

        except:
            pass

        instance = open('.pyplayerdata/in.txt','w+').write('off')
        #instance.close()
        try:
            mycanvas.delete('label')
        except:
            pass
        #instance_a = open('.pyplayerdata/instance.pyplayer','w+').write('on').close()
        tag = id3.Tag()
        tag.parse(to_play)
        artist_value = tag.artist
        album_value = tag.album
        song_value = tag.title
        try:
            sha1 = hashlib.sha1()
            BUF_SIZE = 65536
            with open(to_play, 'rb') as f:
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    sha1.update(data)

            for image in tag.images:
                image_file = open('.album-art/'+sha1.hexdigest()+'.png','wb')
                image_file.write(image.image_data)
                image_file.close()
        except:
            pass
        #print("song title"+str(tag.images))
        if str(tag.title) == 'None':
            song_value = value[0:55]

        song_name_label = tk.Label(mycanvas,text=song_value,bg='#7f7278',fg='white')
        song_name_label.pack()
        song_artist_label = tk.Label(mycanvas,text=artist_value,bg='#7f7278',fg='white')
        song_artist_label.pack()
        song_album_label = tk.Label(mycanvas,text=album_value,bg='#7f7278',fg='white')
        song_album_label.pack()
        try:
        #print(str(value+'.png'))

            basewidth = 120
            global img
            img = Image.open(str('.album-art/'+sha1.hexdigest()+'.png'))
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(str('.album-art/'+sha1.hexdigest()+'.png'))
            img = ImageTk.PhotoImage(Image.open(str('.album-art/'+sha1.hexdigest()+'.png')))
            #img = img.resize((200,200),Image.ANTIALIAS)
            mycanvas.create_image(460,75,image=img,anchor='w')
        except Exception as e:
            '''
            default_album_button = PhotoImage(file='assets/default.png')
            #default_album_button = default_album_button.subsample(2,2)
            default_album_label = tk.Label(image=default_album_button,bg="#7f7278")
            default_album_label.pack()
            mycanvas.create_window(460,70,window=default_album_label,anchor='w')
            '''
            print('awwwwwwwaofihcanluktabckeshgcabjkhgcfabjshgcfbajkhfcgb'+str(e))
            pass

        #art_button = PhotoImage(file=str(sha1.hexdigest()+'.png'))
        #art_button = art_button.sample(2,2)
        #art_button_label = tk.Label(image=art_button,bg="#7f7278")
        #art_button_label.pack()







        #add mutagen or id3 code to get song artist
        mycanvas.create_window(600,40,tags=('label',),window=song_name_label,anchor='w')
        mycanvas.create_window(600,70,tags=('label',),window=song_artist_label,anchor='w')
        mycanvas.create_window(600,100,tags=('label',),window=song_album_label,anchor='w')

        try:
            mycanvas.update('song_name_label')
        except:
            pass
        pyplayer.play_songs(arg)
        pass
    #def get_volume(arg):
    #    print(arg)

    def fname(arg):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        global window
        window = tk.Tk()
        window.tk.call('tk', 'scaling', 2.0)
        window.geometry("1224x720")
        window.title("pyplayer")
        window.configure(bg='#333338')
        window.iconbitmap('assets/py_icon.ico')
        global mycanvas#play_button_label,pause_button_label,

        window.protocol('WM_DELETE_WINDOW',menu_class.destroy_menu)

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
        play_button = PhotoImage(file='assets/play.png')
        play_button = play_button.subsample(2,2)
        menu_button = PhotoImage(file='assets/menu.png')
        menu_button_label = tk.Label(image=menu_button,bg="#7f7278")

        play_button_label = tk.Label(image=play_button,bg="#7f7278")
        pause_button_label = tk.Label(image=pause_button,bg="#7f7278")
        prev_button_label = tk.Label(image=prev_button,bg="#7f7278")
        next_button_label = tk.Label(image=next_button,bg="#7f7278")
        stop_button_label = tk.Label(image=stop_button,bg="#7f7278")
        ll = [[stop_button_label,pyplayer.stop],[prev_button_label,pyplayer.prev],[next_button_label,pyplayer.next],[play_button_label,pyplayer.play_songs],[menu_button_label,menu_class.open_menu]] #,[pause_button_label,pyplayer.pause]
        vol_var = tk.DoubleVar()
        #vol = tk.Scale(mycanvas,variable=vol_var,command=pyplayer.get_volume,troughcolor='#7f7278',width='10',from_=0,to=100,bg='#7f7278',resolution=1,orient='horizontal',length=100,bd=0,showvalue=False,sliderlength=30)
        #vol.pack(anchor='se',side='bottom',pady=70,padx=10)
        for i in ll:
            i[0].pack()
            i[0].bind('<Button-1>',i[1])

        #co-ordinates for buttons  change here
        mycanvas.create_window(15,15,window=menu_button_label,anchor='c')

        mycanvas.create_window(300,70,window=play_button_label,anchor='c')
        mycanvas.create_window(100,70,window=stop_button_label,anchor='c')
        mycanvas.create_window(200,70,window=prev_button_label,anchor='c')
        mycanvas.create_window(400,70,window=next_button_label,anchor='c')
        # TODO: add control buttons int the canvas
        list_file = open('.pyplayerdata/config.pyplayer','r+')
        current_playlist = str(list_file.readlines()[0]).strip('\n')
        list_file.close()
        global current_mylist

        list_file_box = open('.pyplayerdata/'+current_playlist+'.pyplayer','r+')
        current_mylist = Listbox(window,height='100',bg='#333338',bd=0,fg='white',highlightthickness=1,activestyle='none')#yscrollcommand=enc_file_scroll.set,

        for i in list_file_box.readlines():
            i = i.split('\\')[-1]
            current_mylist.insert(END,'     '+i)
        current_mylist.bind('<<ListboxSelect>>',pyplayer.CurSelect)
        current_mylist.pack(pady=0,fill='both',side='top')
        window.mainloop()
        return play_button_label,pause_button_label



k = pyplayer()
k.fname()
k.initilise()
