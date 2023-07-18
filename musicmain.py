# Music Player Application

# Using Python, creating a music player that will either pull mp3 files from 
# local computer, or will do a url request to pull music from youtube
# Functionalities:
# [X]: Retrieve existing mp3 files and display them in a list
# [_]: Create a playlist of existing tracks
# [_]: Display thumbnail images if included
# [X]: Music can be paused and played and switch tracks
# [_]: Display Track Name, Artist
# [_]: Can Forward or Rewind track and display track time length and start
# [_]: Sort tracks by alphabetical order or by artist, can be set by user
# [_]: Name Playlists

# Additional Functionalities
# [_]: Pull tracks from YT api 
# [_]: Dark and Neon Modes
# [_]: Switch from Album Snapshot to moving background

# Note: This can be a mobile or desktop application. Possibly can ported for either ios or android

# Music Main will hold the look of the app

import tkinter as tk
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

#First, set up the appearance

#The main window of the app
root = tk.Tk()

#Size of window
root.geometry("650x700")
root.title("Orbitar Music Player") #Window title
root.configure(background= "#344777") #Main Window BG color
root.resizable(False, False) # Enable/Disable Window resizing

#Mixer initialization
mixer.init()

def AddMusic():
    music_path = filedialog.askdirectory()
    if music_path:
        os.chdir(music_path)
        songs = os.listdir(music_path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
                
def PlayMusic():
    music_name = Playlist.get(ACTIVE)
    print(music_name,ACTIVE)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

low_frame = Frame(root, bg= "#338877", width= 650, height=150)
low_frame.place(x=0, y=400) 

image_logo = PhotoImage(file= './image_files/orbital_logo.png')
root.iconphoto(False, image_logo)

Menu = PhotoImage(file= "./image_files/Rectangle 1menu1.png")
Label(root, image= Menu).place(x=0, y= 400, width= 650, height=150)

frame_music = Frame(root, bd= 2, relief= GROOVE)
frame_music.place(x= 0, y= 580, width= 650, height= 150)

play_button = PhotoImage(file= "./image_files/play_arrow_FILL1_wght400_GRAD0_opsz48.png")
Button(root, image=play_button, bg= "#FFFFFF", bd= 0, width= 50, height= 60, command= PlayMusic).place(x= 225, y= 487)

pause_button = PhotoImage(file= "./image_files/pause_FILL1_wght400_GRAD0_opsz48.png")
Button(root, image= pause_button, bg= "#FFFFFF", bd= 0, width= 50, height= 60, command= mixer.music.pause).place(x= 325, y= 487)

volume_button = PhotoImage(file= "./image_files/volume_down_FILL1_wght400_GRAD0_opsz48.png")
panel_vol = Label(root, image= volume_button).place(x= 125, y= 487)

Button(root, text= "Browse Playlist", width= 77, height= 1, font= ("Arial"), fg= "Black", bg="#FFFFFF", command= AddMusic).place(x= 0, y= 550)

scroll_menu = Scrollbar(frame_music)
Playlist = Listbox(frame_music, width= 100, font= ("Arial", 10), bg= "#337788", fg= "black", selectbackground= "lightblue", cursor= "hand2", bd=0, yscrollcommand= scroll_menu.set)
scroll_menu.config(command= Playlist.yview)
scroll_menu.pack(side= RIGHT, fill=Y)
Playlist.pack(side= RIGHT, fill= BOTH)

root.mainloop()





