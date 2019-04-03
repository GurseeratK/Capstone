import tkinter
from tkinter import ttk
root = tkinter.Tk()
root.title("Python Capstone Project")
root.geometry("800x400")
root.resizable(False, False)
nb = ttk.Notebook(root)
nb.grid(row = 1, column = 0 )
page1 = ttk.Frame(nb)
nb.add(page1, text='Tab1')
 
page2 = ttk.Frame(nb)
nb.add(page2, text='Tab2')



root.mainloop()