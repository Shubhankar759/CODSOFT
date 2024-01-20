#importing GUI library 
from tkinter import *

#Function to typecast String input into integer or float
def Casting(x):
    if x.find(".")==-1:
        return int(x)
    else:
        return float(x)

#All Function for button to input value of operand
def MainDashOne():
    Numbers.insert(len(Numbers.get()),'1')
    
def MainDashTwo():
    Numbers.insert(len(Numbers.get()),'2')

def MainDashThree():
    Numbers.insert(len(Numbers.get()),'3')
    
def MainDashFour():
    Numbers.insert(len(Numbers.get()),'4')
    
def MainDashFive():
    Numbers.insert(len(Numbers.get()),'5')
    
def MainDashSix():
    Numbers.insert(len(Numbers.get()),'6')
    
def MainDashSeven():
    Numbers.insert(len(Numbers.get()),'7')
    
def MainDashEighth():
    Numbers.insert(len(Numbers.get()),'8')
    
def MainDashNine():
    Numbers.insert(len(Numbers.get()),'9')
    
def MainDashZero():
    Numbers.insert(len(Numbers.get()),'0')
    
def MainDashPoint():
    Numbers.insert(len(Numbers.get()),'.')

#Function to clear numbers on the display
def Clear():
    Numbers.delete(0,END)

#All Function for button to perform operation   
def Add():
    global a
    a=Casting(Numbers.get())
    Clear()
    global operation
    operation=1

def Minus():
    global a
    a=Casting(Numbers.get())
    Clear()
    global operation
    operation=2
    
def Multiple():
    global a
    a=Casting(Numbers.get())
    Clear()
    global operation
    operation=3

def Divide():
    global a
    a=Casting(Numbers.get())
    Clear()
    global operation
    operation=4
    
def Answer():
    b=Numbers.get()
    b=Casting(b)
    Clear()
    if operation==1:
        Numbers.insert(0,str(a+b))
    elif operation==2:
        Numbers.insert(0,str(a-b))
    elif operation==3:
        Numbers.insert(0,str(a*b))
    elif operation ==4:
        Numbers.insert(0,str(a/b))
   
    
#styling of GUI window
window =Tk()
window.geometry("300x400")
window.title('Calculator in Python')
icon = PhotoImage(file='CalSigns.png')
window.iconphoto(True,icon)
window.config(background='black')

#Main Input display of calculator
Numbers = Entry(window,font=('Arial',38),width=7,justify=RIGHT,bg='black',fg='lightgreen')
Numbers.place(x=10,y=10)

#all button of calculator 
PressOne=Button(window,
                text='1',
                height= 3, width=6
                #fg='lightgreen',bg='black'
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashOne,
                font=('Arial',13))
PressOne.place(x=10,y=80)

PressTwo=Button(window,
                text='2',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashTwo,
                font=('Arial',13))
PressTwo.place(x=80,y=80)

PressThree=Button(window,
                text='3',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashThree,
                font=('Arial',13))
PressThree.place(x=150,y=80)

PressFour=Button(window,
                text='4',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashFour,
                font=('Arial',13))
PressFour.place(x=10,y=160)

PressFive=Button(window,
                text='5',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashFive,
                font=('Arial',13))
PressFive.place(x=80,y=160)

PressSix=Button(window,
                text='6',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashSix,
                font=('Arial',13))
PressSix.place(x=150,y=160)

PressSeven=Button(window,
                text='7',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashSeven,
                font=('Arial',13))
PressSeven.place(x=10,y=240)

PressEighth=Button(window,
                text='8',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashEighth,
                font=('Arial',13))
PressEighth.place(x=80,y=240)

PressNine=Button(window,
                text='9',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashNine,
                font=('Arial',13))
PressNine.place(x=150,y=240)

PressZero=Button(window,
                text='0',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashZero,
                font=('Arial',13))
PressZero.place(x=80,y=320)

PressPoint=Button(window,
                text='.',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=MainDashPoint,
                font=('Arial',13))
PressPoint.place(x=10,y=320)

PressPlus=Button(window,
                text='+',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=Add,
                font=('Arial',13))
PressPlus.place(x=220,y=80)

PressMinus=Button(window,
                text='-',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=Minus,
                font=('Arial',13))
PressMinus.place(x=220,y=160)

PressMultiple=Button(window,
                text='×',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=Multiple,
                font=('Arial',13))
PressMultiple.place(x=220,y=240)

PressDivide=Button(window,
                text='÷',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=Divide,
                font=('Arial',13))
PressDivide.place(x=220,y=320)

PressMultiple=Button(window,
                text='=',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',command=Answer,
                font=('Arial',13))
PressMultiple.place(x=150,y=320)

PressCancel=Button(window,
                text='C',
                height= 3, width=6
                ,activeforeground='red',activebackground='black',background='red',command=Clear,
                font=('Arial',10))
PressCancel.place(x=223.5,y=10)

window.mainloop()