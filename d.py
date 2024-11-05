from tkinter import *

root = Tk()

root.title("main")
l1 = Label(root, text="This a root window")
l1.pack()


top = Toplevel()
top.title("Root")
l2 = Label(top, text="This a top window")
l2.pack()


root.mainloop()
top.mainloop()
