#!/usr/bin/env python

import tkinter

top = tkinter.Tk()
quit = tkinter.Button(top, text='Hola mundo',
command=top.quit)
quit.pack()
tkinter.mainloop()