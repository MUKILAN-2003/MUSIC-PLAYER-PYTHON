######################## PROGRAMMED BY : S.MUKILAN ############################
#-------------------------     MUSIC   PLAYER       --------------------------#

import pygame
import sys
from tkinter import *
from PIL import Image,ImageTk
import os
from tkinter.filedialog import askdirectory

pygame.init()
pygame.mixer.init()

WINDOW = Tk()
bg = Image.open('Images/bg_music.png')
bg = ImageTk.PhotoImage(bg)
bg_s = Label(WINDOW,image=bg).place(x=0,y=0)
song_s = ' '
a_file = ' '

play_sign = Image.open('Images/play.png')
play_sign = ImageTk.PhotoImage(play_sign)
pause_sign = Image.open('Images/pause.png')
pause_sign = ImageTk.PhotoImage(pause_sign)
unpause_sign = Image.open("Images/unpause.png")
unpause_sign = ImageTk.PhotoImage(unpause_sign)
stop_sign = Image.open('Images/stop.png')
stop_sign = ImageTk.PhotoImage(stop_sign)
browse_sign = Image.open('Images/browse.png')
browse_sign = ImageTk.PhotoImage(browse_sign)
cross_sign = Image.open('Images/cross.png')
cross_sign = ImageTk.PhotoImage(cross_sign)
icon = PhotoImage(file = "Images/icon.png")
WINDOW.iconphoto(False, icon)

brw = Label(WINDOW,text='Brwose  A  Song  Folder  > > > > >',font=('Mistral',19,'bold'),fg='dark red',bg='green')
brw.place(x=5,y=473.5)

def set_v(val):
    pygame.mixer.music.set_volume(float(val)/100)
    
def browse_m(playlist):
    global a_file,brw
    a_file = ' '
    try:
        playlist.delete(0,'end')
        path = askdirectory(title='Select Folder')
        os.chdir(path)
        songtracks = os.listdir()
        brw.destroy()
        for track in songtracks:
            if 'mp3' in track.split('.') or 'wav' in track.split('.'): 
                playlist.insert(END,track)
                a_file = 'found'
        if a_file != 'found':
            playlist.insert(END,'*  No  Audio  File  Found ! ! !')
            brw = Label(WINDOW,text='Brwose  A  Song  Folder  > > > >>',font=('Mistral',19,'bold'),fg='dark red',bg='gold')
            brw.place(x=5,y=473.5)
    except:
        pass

def close_m():
    pygame.quit()
    WINDOW.destroy()
    sys.exit()

class MusicPlayer():
    def __init__(self,WINDOW):
        self.WINDOW = WINDOW
        self.WINDOW.geometry('400x532')
        self.WINDOW.title("MusicPlayer")
        self.track = StringVar()
        self.status = StringVar()
        Button(WINDOW,bg='silver',image=play_sign, command=lambda:self.play_m()).place(x=20,y=170)
        Button(WINDOW,bg='silver',image=pause_sign, command=lambda:self.pause_m()).place(x=120,y=170)
        Button(WINDOW,bg='silver',image=unpause_sign, command=lambda:self.unpause_m()).place(x=220,y=170)
        Button(WINDOW,bg='silver',image=stop_sign, command=lambda:self.stop_m()).place(x=320,y=170)
        Button(WINDOW,bg='silver',image=browse_sign, command=lambda:browse_m(self.playlist)).place(x=330,y=454)
        Button(WINDOW,bg='silver',image=cross_sign,command=lambda:close_m()).place(x=377,y=0)
        
        vol = Scale(from_ = 100,to = 0,orient = VERTICAL,resolution =1,sliderlength=20,highlightbackground='dark red',cursor='target',activebackground='dark red',length=113,width=15,bg='silver',command=set_v).place(x=355,y=25)
        Label(WINDOW,text='Volume',font = ("Mistral",12,"bold"),bg='silver',fg='dark red').place(x=347,y=145)

        songsframe = LabelFrame(self.WINDOW,text="Song Playlist",font=("Mistral",19,"bold"),bg="silver",fg="dark green",relief=GROOVE)
        songsframe.place(x=0,y=220,width=400,height=232)
        status = Label(self.WINDOW,textvariable=self.status,font=("Mistral",32,"bold"),bg="silver",fg="red").place(x=110,y=90)
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="red",font=("Mistral",18,"bold"),bg="silver",fg="dark red",relief=GROOVE)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

    def play_m(self):
        global song_s
        try:
            self.track.set(self.playlist.get(ACTIVE))
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            song_s = 'playing'
            self.status.set("[ Playing ]")
            pygame.mixer.music.play()
        except:
            pass

    def pause_m(self):
        global song_s
        if song_s == 'playing':
            self.status.set("[ Paused ]")
            pygame.mixer.music.pause()
            song_s = 'paused'

    def unpause_m(self):
        global song_s
        if song_s == 'paused':
            self.status.set("[ Playing ]")
            pygame.mixer.music.unpause()
            song_s = 'playing'

    def stop_m(self):
        global song_s
        if song_s == 'paused' or song_s == 'playing':
            self.status.set("[ Stopped ]")
            pygame.mixer.music.stop()
            song_s = 'stoped'

MusicPlayer(WINDOW)
WINDOW.mainloop()
