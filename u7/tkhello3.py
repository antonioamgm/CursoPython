#!/usr/bin/env python

import tkinter

top = tkinter.Tk()

hello = tkinter.Label(top, text='Hola mundo')
hello.pack()

quit = tkinter.Button(top, text='Salir', command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()