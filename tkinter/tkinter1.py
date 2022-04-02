#!/usr/bin/python3.8

from tkinter import *
from tkinter import messagebox
top = Tk()
top.title('first tkinter')
'''add widgets here

    activeforeground: to set the foreground color when button is under the cursor.
    bg: to set he normal background color.
    command: to call a function.
    font: to set the font on the button label.
    image: to set the image on the button.
    width: to set the width of the button.
    height: to set the height of the button.

'''
#button = Button(top,text='Stop', width=50, height=50, command=top.destroy)
#destroys the app
'''
    bd: to set the border width in pixels.
    bg: to set the normal background color.
    cursor: to set the cursor used in the canvas.
    highlightcolor: to set the color shown in the focus highlight.
    width: to set the width of the widget.
    height: to set the height of the widget.
'''
#code
'''
button  = Canvas(top, width=40, height=60)
button.pack()
canvas_height=600
canvas_width=600
y = int(canvas_height / 2)
button.create_line(0, y, canvas_width, y )
'''
#checkboexe
'''
var1 = IntVar()
Checkbutton(top, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(top, text='female', variable=var2).grid(row=1, sticky=W)
'''
#Entry
'''
Label(top, text='First Name').grid(row=0)
Label(top, text='Last Name').grid(row=1)
e1 = Entry(top)
e2 = Entry(top)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
'''
#Frame
'''
frame = Frame(top)
frame.pack()
bottomframe = Frame(top)
bottomframe.pack( side = RIGHT )
redbutton = Button(frame, text = 'Red', bg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown', width='100', command=frame.destroy)
greenbutton.pack( side = BOTTOM )
bluebutton = Button(frame, text ='Blue', bg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(frame, text ='Black', fg ='black',height='20',command=frame.print("BLACCK))
blackbutton.pack( side = BOTTOM)
'''
#Label
'''
w = Label(top, text='GeeksForGeeks.org!')
w.pack()
'''
#Listbox
'''''
Lb = Listbox(top)
Lb.insert(0, 'Python')
Lb.insert(1, 'Java')
Lb.insert(2, 'C++')
Lb.insert(3, 'Any other')
Lb.grid()
'''''
#MenuButton
'''
mb= Menubutton ( top, text="condiments",bg ="red")
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0)
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

mb.pack()
'''
#Menu
''''
menu = Menu(top)
top.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator() # a small line
filemenu.add_command(label='Exit', command=top.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
'''
#messagels

'''''
ourMessage ='This is our Message'
messageVar = Message(top, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
'''
#Radiobuttons
'''''
v = IntVar()
Radiobutton(top, text='yes', variable=v, value=1).pack(anchor=W)
Radiobutton(top, text='no', variable=v, value=2).pack(anchor=W)
'''''
#scale
'''''
w = Scale(top, from_=0, to=200)
w.pack()
w = Scale(top, from_=0, to=200, orient=HORIZONTAL)
w.pack()
'''
#scrooll bar
'''''
scrollbar = Scrollbar(top)
scrollbar.pack( side = LEFT, fill = Y )
mylist = Listbox(top, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, 'This is line number' + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
'''''
#spinbox
'''''
w = Spinbox(top, from_ = 0, to = 10)
w.pack()
'''
#panelwindow
'''''
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Entry(m1, bd=5)
m1.add(left)
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
top = Scale(m2, orient=HORIZONTAL)
m2.add(top)
'''
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")
def Destroy():
   command = top.destroy()

B = Button(top, text = "Hello", command = helloCallBack)
C = Button(top, text = "Quit", command = Destroy)
C.place(x = 50,y = 50)
B.place(x = 70,y = 70)
top.mainloop()

print("Program compiled!!")
print("####################### TUSHAR ####################")
print("***************************************************")