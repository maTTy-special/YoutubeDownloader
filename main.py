from tkinter import *
from pytube import YouTube

window=Tk()
window.geometry("500x550")
window.config(bg="red")
window.title("Video Downloader by TOHIRJON")

youtube_logo=PhotoImage(file="YTicon.png")
window.iconphoto(False,youtube_logo)

Label(window,text="Video Downloader",font="Arial 25 bold",bg="yellow").pack(padx=5,pady=50)

video_link=StringVar()

Label(window,text="Enter link : ",font=("Cambria",15,"bold")).place(x=170,y=110)
Entry_link=Entry(window,width=40,font=35,textvariable=video_link,bd=4).place(x=50,y=150)

def video_download():
    video_url=YouTube(str(video_link.get()))
    videos=video_url.streams.first()
    videos.download()
   

    Label(window,text="Download Completed !",font=("Arial",30,"bold"),bg="green",fg="black").place(x=20,y=480)

Button(window,text="DOWNLOAD",font=("Verdana",25,"bold"),bg="yellow",command=video_download).place(x=120,y=300)



window.mainloop()
