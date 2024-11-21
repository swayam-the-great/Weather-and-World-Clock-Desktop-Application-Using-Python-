import os
import datetime
import time
import threading
from time import strftime


# FOR GUI
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from PIL import ImageTk, Image
from pygame import mixer
from tkinter import *
from PIL import ImageTk,Image
import time
import pygame as pg

pg.mixer.init()

root=Tk()
root.title("Digital CLOCK :)")
canva_height=520
canva_wide=314

root.geometry(f"{canva_wide}x{canva_height}")
# display time
# WEATHER KA GUI
bg_image = Image.open("pink.PNG")
# TODO: Resize these background images
bg_image= bg_image.resize((314,520))
photo = ImageTk.PhotoImage(bg_image)
bglabel = Label(root,image=photo)
bglabel.place(x=0, y=0)

def timefunt():
    strtime=strftime('%H:%M:%S:%p')
    lb1.config(text=strtime)
    lb1.after(1000,timefunt)


lb0=Label(root ,text="current time",anchor='nw' , font="lucida 10 bold",background="pink",foreground="black" )
lb0.pack( padx="20",pady="0" , fill=X )

lb1=Label(root ,anchor='n' , font="Helvetica 30 bold",background="purple",foreground="cyan" )
lb1.pack( padx="20",pady="0" , fill=X )


#finished here
mixer.init()

lb2=Label(root,anchor='n', text="ALARM ", font="Helvetica 30 bold",background="cyan",foreground="yellow" )
lb2.pack( padx="20",pady="0" , fill=X )


#CLOCK
inputmsg=StringVar()




#FUNCTION LOGIC

alarmtime =StringVar()

def alarm():
    msg1 = messagebox.showinfo('Alarm', "Alarm SET Sucessfully!")
    Alarm = alarmtime.get()
    AlarmT = Alarm
    CurrentTime = time.strftime("%H:%M")

    while AlarmT != CurrentTime:
        CurrentTime = time.strftime("%H:%M")

    if AlarmT == CurrentTime:
        pg.mixer.music.load('tone.mp3')
        pg.mixer.music.play()
        msg = messagebox.showinfo('Alarm', f'{inputmsg.get()}')
        if msg == 'ok':
            mixer.music.stop()



Clock=Image.open("clock_img.PNG")

# TODO: Resize these images
Clock= Clock.resize((145, 145))
photo1=ImageTk.PhotoImage(Clock)
img1=Label(image=photo1 )
img1.pack(side="top")


lbj=Label(root ,text="Alarm clock",anchor='nw' , font="lucida 10 bold",background="pink",foreground="black" )
lbj.pack( padx="20",pady="0" , fill=X )


f1=Frame(root,)
set_time=Label(f1,text="Set time:", font="lucida 12 bold",background="pink",foreground="black")
set_time.pack( side="left",pady=0 )

inpt1=Entry(f1,font="lucida 10 bold",textvariable=alarmtime,background="grey",foreground="black",width=20)
inpt1.pack(side="right")
f1.pack()


set_msg=Label(root,text="Set Remainder:", font="lucida 12 bold",background="pink",foreground="blue")
set_msg.pack( anchor='nw' ,padx=48,pady=2)

inpt2=Entry(root,font="lucida 10 bold",textvariable= inputmsg,background="grey",foreground="blue",width=25)
inpt2.pack(anchor='ne',padx=10 )

set_alarm=Button(root,text="SET",command=alarm, width=10)
set_alarm.pack(pady=20)




timefunt()


root.mainloop()




