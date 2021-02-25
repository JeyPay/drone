
from tkinter import *
from random import randint
import PID

widthV = 640
heightV = 640
dataX = 35
dataY = 0
oldX = 35
oldY = 30
setpoint = 320

root = Tk()

w = Canvas(root,width=widthV,height=heightV)
w.create_line(35,20,35,heightV)
w.create_line(0,heightV-30,widthV,heightV-30)
tex1 = Label(root, text='30',fg='black')
tex1.place(bordermode=OUTSIDE, x=0, y=heightV-40)
tex2 = Label(root, text='100',fg='black')
tex2.place(bordermode=OUTSIDE, x=0, y=30)
w.grid()

pid = PID.PID(10, 2, 0.1)
pid.SetPoint = setpoint
pid.setSampleTime(0.02)

def p(e):
    pid.SetPoint = pid.SetPoint + 100
    print(pid.SetPoint)

def m(e):
    pid.SetPoint = pid.SetPoint - 100
    print(pid.SetPoint)

def c(e):
    pid.SetPoint = int(input('Value : '))

def update():
    global dataX,dataY,oldX,oldY,pid,setpoint

    #print(setpoint, dataX, dataY, pid.SetPoint)
    pid.update(dataY)
    dataY = pid.output

    w.create_line(oldX,oldY*12,dataX,dataY*12,fill='red',tag='points')
    oldX = dataX
    oldY = dataY

    dataX += 4
    if dataX>=640:
        oldX = 35
        dataX = 35
        w.delete('points')

    root.bind('p',p)
    root.bind('m',m)
    root.bind('c',c)
    root.after(20,update)

root.after(1,update)
root.mainloop()
