from tkinter import *
from pytube import YouTube
import os


root = Tk()




def Startmp3():

    startedlabelmp3 = Label(root, text="Download Started", bg="red", fg="black")
    startedlabelmp3.config(font=("Arial", 30))
    startedlabelmp3.grid(column=4)
    root.update_idletasks()
    downloadmp3()
    root.update_idletasks()




def downloadmp3():

    url = urlbox.get()
    command = ' youtube-dl -f 140 -o "/root/Musik/YourSoundtrack" %s' %(url)
    os.system(command)
    finishedlabelmp3 = Label(root, text="Finished Downloading saved in Music", fg="black", bg="red")
    finishedlabelmp3.config(font=("Arial", 30))
    finishedlabelmp3.grid(column=4)
    root.update_idletasks()





def Startmp4():
    startedlabel = Label(root, text="Download Started", bg="red", fg="black")
    startedlabel.config(font=("Arial", 30))
    startedlabel.grid(column=4)
    root.update_idletasks()
    downloadmp4()





def downloadmp4():

    url = urlbox.get()
    download = YouTube("%s" %(url))
    video = download.get('mp4', '720p')
    video.download("/root/Videos/")
    root.update_idletasks()
    finishedlabel = Label(root, text="Finished Downloading saved in Videos", bg="red", fg="black")
    finishedlabel.config(font=("Arial", 30))
    finishedlabel.grid(column=4)
    root.update_idletasks()





root.geometry("1000x750")
root.config(bg="red")
root.title("YouTube Downloader")

startlabel = Label(root, text="YouTube Downloader", fg="black", bg="red")
startlabel.config(font=("Arial", 40))
startlabel.grid(column=4)

urllabel = Label(root, text="URL", bg="red", fg="white")
urllabel.config(font=("Arial", 30))
urllabel.grid(row=100, column=0, sticky=W)

urlbox = Entry(root, width=30)
urlbox.grid(row=100, columnspan=2)




downloadbuttonmp4 = Button(root, text="Download mp4", bg="red", fg="white", command=Startmp4)
downloadbuttonmp4.config(font=("Arial", 20))
downloadbuttonmp4.grid(row=101, column=0)

downloadbuttonmp3 = Button(root, text="Download mp3", bg="red", fg="white", command=Startmp3)
downloadbuttonmp3.config(font=("Arial", 20))
downloadbuttonmp3.grid(row=101, column=1)



root.mainloop()




