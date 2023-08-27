import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-list")
root.geometry("400x600+400+100")
root.resizable(False,False)


task_list=[]

#icon
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False,Image_icon)
#Top Bar
TopImage=PhotoImage(file="Image/topbar.png")
Label(root,image=TopImage).pack( )



root.mainloop()

