from tkinter import *




window =Tk()
window.geometry("300x400")
window.title('Calculator in Python')
icon = PhotoImage(file='CalSigns.png')
window.iconphoto(True,icon)
window.config(background='black')

PressOne=Button(window,
                text='1',
                height= 3, width=6
                #fg='lightgreen',bg='black'
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressOne.place(x=10,y=80)

PressTwo=Button(window,
                text='2',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressTwo.place(x=80,y=80)

PressThree=Button(window,
                text='3',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressThree.place(x=150,y=80)

PressFour=Button(window,
                text='4',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressFour.place(x=10,y=160)

PressFive=Button(window,
                text='5',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressFive.place(x=80,y=160)

PressSix=Button(window,
                text='6',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressSix.place(x=150,y=160)

PressSeven=Button(window,
                text='7',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressSeven.place(x=10,y=240)

PressEighth=Button(window,
                text='8',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressEighth.place(x=80,y=240)

PressNine=Button(window,
                text='9',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressNine.place(x=150,y=240)

PressZero=Button(window,
                text='0',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressZero.place(x=80,y=320)

PressPoint=Button(window,
                text='.',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressPoint.place(x=10,y=320)

PressPlus=Button(window,
                text='+',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressPlus.place(x=220,y=80)

PressMinus=Button(window,
                text='-',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressMinus.place(x=220,y=160)

PressMultiple=Button(window,
                text='×',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressMultiple.place(x=220,y=240)

PressDivide=Button(window,
                text='÷',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressDivide.place(x=220,y=320)

PressMultiple=Button(window,
                text='=',
                height= 3, width=6
                ,activeforeground='lightgreen',activebackground='black',background='lightgreen',
                font=('Arial',13))
PressMultiple.place(x=150,y=320)

PressCancel=Button(window,
                text='C',
                height= 3, width=6
                ,activeforeground='red',activebackground='black',background='red',
                font=('Arial',10))
PressCancel.place(x=223.5,y=10)

Numbers = Entry(window,font=('Arial',38),width=7,justify=RIGHT)
Numbers.place(x=10,y=10)



window.mainloop()