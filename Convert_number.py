from tkinter import *

win = Tk()
win.geometry('600x350+700+200')
win.title('Converter')
def read():
    m = var.get()
    b = f'the hex number is: {hex(m)}\n' \
        f'the bin number is: {bin(m)}\n' \
        f'the oct number is: {oct(m)}'
    Label(text=b, bg='silver', fg='black', width=40,font=('mono',14,'bold')).pack(pady=10)

bt1 = Button(text='exit',bd=5,command=quit)
bt1.pack(side=BOTTOM)
var = IntVar()
lb1 = Label(text='Enter Number To Convert').pack(pady=10)
ent1 = Entry(bg='cyan',width=20,textvariable=var).pack(pady=10)
bt2 = Button(text='Press To Convert',bd=5,command=read).pack(pady=10)
win.mainloop()