from tkinter import *
main = Tk()
HWA='Hello World App'
messageVar = Message(main, text = HWA)
messageVar.config(bg='red')
messageVar.pack( )
main.mainloop( )