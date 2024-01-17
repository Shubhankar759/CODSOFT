from tkinter import *
import random

def submit():
  Display.delete(0, END)
  words=WordCount.get()
  uppercase="QWERTYUIOPASDFGHJKLZXCVBNM"
  lowercase="qwertyuiopasdfghjklzxcvbnm"
  numb='1234567890'
  spe="}]!@#%$^&*()~`,./<>?:;_-+=*|[{\"\'\\"
  mark=''
  
  if num.get():
    mark +=numb
    
  if ustr.get():
    mark+=uppercase
  
  if lstr.get():
    mark+=lowercase
  
  if spech.get():
    mark+=spe

  password="".join(random.sample(mark,words))
  Display.insert(0,password)
  print(password)
  
  
  
  

window = Tk()
window.title("Python Password Generator")
window.geometry("400x370")
window.config(background='#262626')

def copy_to_clip():
    window.clipboard_clear()
    window.clipboard_append(Display.get())
    window.update()
   

num=BooleanVar()
lstr=BooleanVar()
ustr=BooleanVar()
spech=BooleanVar()

heading = Label(window,
                text="Password Generator",
                font=("Arial",20),
                fg='#4da6ff',
                bg='#262626'
               )
heading.place(x=5,y=0)


menu=Label(window,
                text="Password Elements",
                font=("Arial",12),
                fg='#4da6ff',
                bg='#262626'
               )
menu.place(x=5,y=45)

Num = Checkbutton(window,
                  text='Numbers',
                  variable=num,
                  font=("Arial",10),
                  fg='#4da6ff',
                   bg='#262626',
                  activeforeground='#ff884d',
                  activebackground='#262626'
                  )

Num.place(x=7,y=77)

Ustr = Checkbutton(window,
                  text='Uppercase',
                  variable=ustr,
                  font=("Arial",10),
                  fg='#4da6ff',
                   bg='#262626',
                  activeforeground='#ff884d',
                  activebackground='#262626'
                  )

Ustr.place(x=7,y=110)

Lstr = Checkbutton(window,
                  text='Lowercase',
                  variable=lstr,
                  font=("Arial",10),
                  fg='#4da6ff',
                   bg='#262626',
                  activeforeground='#ff884d',
                  activebackground='#262626'
                  )

Lstr.place(x=7,y=143)

Special = Checkbutton(window,
                  text='Special charaters',
                  variable=spech,
                  font=("Arial",10),
                  fg='#4da6ff',
                  bg='#262626',
                  activeforeground='#ff884d',
                  activebackground='#262626'
                  )

Special.place(x=7,y=174)

Countmenu=Label(window,
                text="Enter Length of password",
                font=("Arial",12),
                fg='#4da6ff',
                bg='#262626'
               )
Countmenu.place(x=5,y=205)

WordCount= Scale(window,
                 from_=1,
                 to=30,
                 orient=HORIZONTAL,
                 length=385,
                 fg='#4da6ff',
                 background='#262626',
                 activebackground='#262626')

WordCount.place(x=5,y=235)

WordCount.set(8)

Submit = Button(window,text='Generate',
                font=("Arial",10),
                    height=1,
                    width=7,
                    fg='#4da6ff',
                    bg='#262626',
                  activeforeground='#ff884d',
                  activebackground='#262626',
                  command=submit
                  )

Submit.place(x=170,y=287)

Display = Entry(window,
                font=("Arial",13),
                width=33,
               fg='black',
               bg='#b3b3b3')

Display.place(x=10,y=325)

CopyButton = Button(window,text='Copy',
                    font=("Arial",10),
                    height=1,
                    width=6,
                    fg='#4da6ff',
                    bg='#262626',
                  activeforeground='#ff884d',
                  activebackground='#262626',
                   command=copy_to_clip)

CopyButton.place(x=325,y=324)



window.mainloop()