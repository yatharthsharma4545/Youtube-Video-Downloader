from pytube import YouTube
from tkinter import *
from tkinter import messagebox , Menu ,ttk
import os
import pytube
import subprocess
import threading
import time

utube = Tk()
utube.title("YOUTUBE VIDEOS DOWNLOADER ")
utube.iconbitmap("YT.ico")

def start():
    progress['value'] = 10
    utube.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 20
    utube.update_idletasks()
    time.sleep(0.2)

    progress['value'] = 30
    utube.update_idletasks()
    time.sleep(0.2)

    progress['value'] = 40
    utube.update_idletasks()
    time.sleep(0.1)

def bar_l():

    progress['value'] = 50
    utube.update_idletasks()
    time.sleep(0.1)

    progress['value'] = 60
    utube.update_idletasks()
    time.sleep(0.2)

    progress['value'] = 80
    utube.update_idletasks()
    time.sleep(0.3)
    progress['value'] = 100
    progress['value'] = 0

def bar_p():

    progress_play['value'] = 20
    utube.update_idletasks()
    time.sleep(1)

    progress_play['value'] = 50
    utube.update_idletasks()
    time.sleep(1)

    progress_play['value'] = 80
    utube.update_idletasks()
    time.sleep(1)

    progress_play['value'] = 100
    progress_play['value'] = 0

threads=[]

def bar():
    def help_bar():
        messagebox.showinfo("Help"," 1) Check Your internet connection  , 2) Please ensure that you have not changed the name of your E drive it should be default, 3) please don't hit download button multiple times")
    def about():
        messagebox.showinfo("About ","This application is Developed by Yatharth Sharma    # Technologies used # 1) Python  2) libraries like pytube, os , threading , subprocess , ttk , time etc. 3) Tkinter  ")
    def contact():
        messagebox.showinfo("Contact ","Mail : yatharth4545@gmail.com")
    menu= Menu(utube)
    file_item=Menu(menu)
    file_item.add_command(label='Help', command= help_bar)
    file_item.add_command(label='About us', command=about)
    file_item.add_command(label='Contact us', command=contact)
    menu.add_cascade(label="Help",menu=file_item)
    utube.config(menu=menu)

def startThredProcess_low():
    myNewThread = threading.Thread(target=down_vdo_low)
    threads.append(myNewThread)
    myNewThread.start()

def startThredProcess_high():
    myNewThread = threading.Thread(target=down_vdo_high)
    threads.append(myNewThread)
    myNewThread.start()

def startThredProcess_play():
    myNewThread = threading.Thread(target=play)
    threads.append(myNewThread)
    myNewThread.start()

def down_vdo_low():
    try:
        start()
        ytl=YouTube(str(links.get()))
    except:
        progress['value'] = 0
        messagebox.showwarning(" WARNING: "," Connection error")
    else:
        dwl=ytl.streams.get_lowest_resolution()
        dwl.download("E:/")
        bar_l()
        os.startfile("E:/")
        messagebox.showinfo("Notification","Video downloaded Successfully in E drive :)")

def down_vdo_high():
    try:
        start()
        ytl=YouTube(str(links.get()))
    except:
        progress['value'] = 0
        messagebox.showwarning(" WARNING: "," Connection error")
    else:

        dwl=ytl.streams.get_highest_resolution()
        dwl.download("E:/")
        bar_l()
        os.startfile("E:/")
        messagebox.showinfo("Notification","Video downloaded Successfully in E drive :)")

def play():
    try:
        p=Playlist(str(links_play.get()))
    except:
        messagebox.showwarning(" WARNING: "," Connection error")
    else:
        p.download_all("E:/")
        bar_p()
        os.startfile("E:/")
        messagebox.showinfo("Notification","Videos downloaded Successfully in E drive :)")


bar()

hi = Label(utube , text="Welcome , Please read help first  ;)" , bg="bisque", fg="black", font="Lato 13 bold", padx="5", pady="5",borderwidth=4 ,relief="groove")
hi.grid(row=0, column=1, sticky=N+S+E+W )


hii = Label(utube , text=" Now , Paste the video link below and press the download button ;)" , bg="bisque", fg="black", font="Lato 13 bold", padx="5", pady="5",borderwidth=4 ,relief="groove")
hii.grid(row=1, column=1, sticky=N+S+E+W )

hi = Label(utube , text="To Download Whole playlist Paste Playlist Link Below ;)" , bg="bisque", fg="black", font="Lato 13 bold", padx="5", pady="5",borderwidth=4 ,relief="groove")
hi.grid(row=4, column=1, sticky=N+S+E+W )

links = Entry(utube ,width=70, borderwidth=2 ,relief="groove")
links.grid(row = 2 , column=1)

links_play = Entry(utube ,width=70, borderwidth=2 ,relief="groove")
links_play.grid(row = 5 , column=1)

download_low = Button( utube , text=" Low quality Download" , bg="#142E54", fg='white', command= startThredProcess_low , font="Lato 13 ",borderwidth=4 ,relief="groove")
download_low.grid(row=2, column=2, sticky=N+S+E+W )

download_high = Button( utube , text=" High quality Download" , bg="#142E54", fg='white', command= startThredProcess_high , font="Lato 13 ",borderwidth=4 ,relief="groove")
download_high.grid(row=2, column=3, sticky=N+S+E+W )

progress = ttk.Progressbar(utube, orient = HORIZONTAL, length = 100 , mode = 'determinate')
progress.grid(row=3,column=1,sticky=N+S+E+W)

progress_play = ttk.Progressbar(utube, orient = HORIZONTAL, length = 100 , mode = 'determinate')
progress_play.grid(row=6,column=1,sticky=N+E+W+S,padx="5", pady="5")

download_play = Button( utube , text=" Download Playlist" , bg="#142E54", fg='white', command= startThredProcess_play , font="Lato 13 ",borderwidth=4 ,relief="groove")
download_play.grid(row=5, column=2, sticky=N+E+W+S,padx="5", pady="5" )

utube.minsize( 910,250 )
utube.maxsize( 910,250 )

utube.mainloop()
