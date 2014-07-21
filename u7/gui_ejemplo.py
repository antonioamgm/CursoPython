import Gui

g = Gui.Gui()
g.title('Gui')


label = g.la(text='Press the button.')
button = g.bu(text='Press me.')


def make_label():
    g.la(text='Thank you.')

button2 = g.bu(text='No, press me!', command=make_label)

g.mainloop()