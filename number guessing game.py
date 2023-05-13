import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox

a = random.choice(["black","red","orange","gray"])
b = random.choice(["lime","blue","cyan","salmon"])

NGG = tk.Tk()
NGG.title("NUMBER GUESSİNG GAME")
NGG.minsize(400,300)
NGG.maxsize(400,300)

BOT_NUMBER = random.randrange(1,100)

def RESTART():
    global BOT_NUMBER
    AREA["text"] = "GUESS THE NUMBER!\n1<x<100"
    BOT_NUMBER = random.randrange(1,100)
    RB.place(width = 400,height = 100,x = 0,y = 2000)
    GB.place(width = 400,height = 100,x = 0,y = 200)
    GET_AREA.delete(0,END)

def GUESS():
    global BOT_NUMBER
    acxz1 = GET_AREA.get()
    NUMBER = int(acxz1)
    
    if NUMBER > BOT_NUMBER:
        msg = Tk()
        msg.withdraw()
        messagebox.showwarning("LOWER","LOWER."+"\n"+"PLEASE GUESS AGAİN!")
        AREA["text"] = "LOWER!"
        GET_AREA.delete(0,END)

    if NUMBER < BOT_NUMBER:
        msg = Tk()
        msg.withdraw()
        messagebox.showwarning("HİGHTER","HİGHTER."+"\n"+"PLEASE GUESS AGAİN!")
        AREA["text"] = "HİGHTER!"
        GET_AREA.delete(0,END)


    if NUMBER == BOT_NUMBER:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("CORRECT","YOUR NUMBER İS CORRECT. "+"\n"+str(BOT_NUMBER))
        AREA["text"] = "CORRECT. İT'S " + str(BOT_NUMBER)
        RB.place(width = 400,height = 100,x = 0,y = 200)
        GB.place(width = 400,height = 100,x = 0,y = 2000)
        
    
AREA = tk.Label(NGG,text = "GUESS THE NUMBER!\n1<x<100",fg = b,bg = a,font = "Arial 25")
AREA.place(width = 400,height = 100,x = 0,y = 0)

GET_AREA = tk.Entry(NGG,fg = a,bg = b,font = "Arial 50")
GET_AREA.place(width = 400,height = 100,x = 0,y = 100)

GB = tk.Button(NGG,text = "GUESS",fg = b,bg = a,activeforeground = b,activebackground = a,font = "Arial 50",command = GUESS)
GB.place(width = 400,height = 100,x = 0,y = 200)

RB = tk.Button(NGG,text = "RESTART",fg = b,bg = a,activeforeground = b,activebackground = a,font = "Arial 50",command = RESTART)
RB.place(width = 400,height = 100,x = 0,y = 2000)

NGG.mainloop()
