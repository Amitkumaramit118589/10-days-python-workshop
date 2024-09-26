from tkinter import *

root=Tk()

root.title("EVM")

add=0

cam=0

def addi (a):

global add add=add+1

def add2 (b):

global cam

cam-cam+1

def result(c):

Label (root, text=str (add), height=2,width=10).grid(row=1,column=3)

Label (root, text=str (cam), height=2,width=10).grid(row=2,column=3)
Label (root, text="Winner: Party-2", height=2, width=20).grid ( row = 3 ,column=3)

elif (cam==add):

Label (root, text="Result Tie", height L = 2 ,width=20).grid ( xow = 3 column= btn1.config(state="disable")

btn2.config(state="disable")

root.geometry ("500x500")

Label (root, text="Party1", height=2, width=10).grid(row=1,columns=1) Label (root, text="Party2", height=2,width=10).grid(row=2,columns s = 1 )

btn1=Button (root, text="Vote",command=lambda: add1 (0))

btn1.grid(row=1,column=2)

btn2=Button (root, text="Vote",command=lambda: add2 (0))

btn2.grid(row=2,column=2)

n3=Button (root, text="Result",command=lambda:result(0))

ben3.grid(row=3,column=1)
