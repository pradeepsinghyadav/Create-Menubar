# import tkinter as tk
# from tkinter import ttk
# win = tk.Tk()
# win.title("Menu Bar")
# def func():
#     pass

# main_menu = tk.Menu(win)
# main_menu.add_command(label="file",command=func)
# main_menu.add_command(label="save",command=func)
# main_menu.add_command(label="new",command=func)
# main_menu.add_command(label="edit",command=func)
# secondary_menu =tk.Menu(main_menu)
# secondary_menu.add_command(label = "undo",command= func)
# secondary_menu.add_command(label = "new file",command = func)
# secondary_menu.add_cascade(label= "new",menu= main_menu)
# win.config(menu=main_menu)
# win.mainloop()






import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,messagebox,filedialog
import os

main_application=tk.Tk()
main_application.geometry("1200x800")
main_application.title("Pradeeps Text Editor")






main_menu=tk.Menu()
file=tk.Menu(main_menu,tearoff=False)
edit=tk.Menu(main_menu,tearoff=False)
view=tk.Menu(main_menu,tearoff=False)
color_theme=tk.Menu(main_menu,tearoff =False)


# now cascading
main_menu.add_cascade(level="File",menu=file)
main_menu.add_cascade(level="Edit",menu=edit)
main_menu.add_cascade(level="View",menu=view)
main_menu.add_cascade(level="Color Theme",menu=color_theme)











main_application.config(menu=main_menu)
main_application.mainloop()
