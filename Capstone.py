import tkinter
from tkinter import ttk
root = tkinter.Tk()
root.title("Python Capstone Project")
root.geometry("800x400")
root.resizable(False, False)
nb = ttk.Notebook(root, width= 790,height = 380)
nb.grid(row = 1, column = 0 )
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
nb.add(page1, text='Profile')
nb.add(page3, text ='College application Deadlines')
nb.add(page2, text='Extracurriculars/other activities')
btn_save = ttk.Button(page1, text = "Save", command = lambda: clicked)
btn_update = ttk.Button(page1, text = "Update", command = lambda: clicked)
txt_name = ttk.Entry(page1)
txt_age = ttk.Entry(page1)
lbl_name = ttk.Label(page1, text="Name:")
lbl_age = ttk.Label(page1, text="Age:")


#btn_update.grid(row= 1, column = 1)
#btn_save.grid(row =1, column = 0)
txt_name.grid(row = 0, column = 1)
lbl_name.grid(row = 0, column = 0 )
lbl_age.grid(row = 1, column = 0)

#Profile tab interior

#txt_name = tkinter.Entry(root, width= 10)
#txt_name.grid( row = 0,column = 0)
# College application deadlines tab interior
# activity tab interior



root.mainloop()