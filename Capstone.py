import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
# downloaded DB Browser for SQLite
import sqlite3 # for database

root = tkinter.Tk()
root.title("Python Capstone Project")
root.geometry("1440x900")
root.configure(background = "lightgrey")
#root.resizable(False, False)
conn = sqlite3.connect("college_info.db") 
c = conn.cursor()
nb = ttk.Notebook(root, width = 1380, height = 730)
nb.grid(row = 1, column = 0 )
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
nb.add(page1, text="Profile")
nb.add(page2, text ="College application Deadlines")
nb.add(page3, text="Extracurriculars/other activities")
#Profile tab interior
photo = PhotoImage(file="flower.gif")
w = Label(page1, image=photo)
w.photo = photo
w.grid(row = 0, column = 0, rowspan = 2)
txt_name = ttk.Entry(page1)
txt_age = ttk.Entry(page1)
txt_dob = ttk.Entry(page1)
lbl_name = ttk.Label(page1, text=" Full name:")
lbl_age = ttk.Label(page1, text="Age:")
lbl_dob = ttk.Label(page1, text="DOB:\n*(dd/mm/yyyy)")
lbl_gender = ttk.Label(page1, text="Gender:")
btn_save = ttk.Button(page1, text = "Save", command = lambda: clicked)
btn_update = ttk.Button(page1, text = "Update", command = lambda:clicked)
var_chk = IntVar()
rdl_1 = ttk.Radiobutton(page1,text = "Male", variable = var_chk, value = 1)
rdl_2 = ttk.Radiobutton(page1,text = "Female", variable = var_chk, value = 2)
rdl_3 = ttk.Radiobutton(page1,text = "Other", variable = var_chk, value = 3)

txt_name.grid(row = 0, column = 2)
txt_age.grid(row = 1, column = 2)
txt_dob.grid(row = 2, column =2)
lbl_name.grid(row = 0, column = 1 )
lbl_age.grid(row = 1, column = 1)
lbl_dob.grid(row =2 , column = 1)
lbl_gender.grid(row = 3, column = 1)
rdl_1.grid(row =3, column = 2, sticky = "w")
rdl_2.grid(row =3, column = 2, sticky = "")
rdl_3.grid(row =3, column = 2, sticky = "e")

btn_update.grid(row= 4, column = 2)
btn_save.grid(row =4, column = 1)

#College deadlines tab interior
#FUNCTIONS

#College widgets
lblfr_college = ttk.LabelFrame(page2, text = "") # Information labelframe - top
lbl_name = ttk.Label(lblfr_college, text = "Name of College: ", font = ("Arial", 15))
lbl_tuition_fees = ttk.Label(lblfr_college, text = "Tuition fees: ", font = ("Arial",15))
lbl_accomodation_cost = ttk.Label(lblfr_college, text = "Accomodation cost: ", font = ("Arial",15))
lbl_rank_sw = ttk.Label(lblfr_college, text = "Ranking SW: ", font = ("Arial",15))
lbl_program = ttk.Label(lblfr_college, text = "Program applied: ", font = ("Arial",15))
lbl_location = ttk.Label(lblfr_college, text = "Location: ", font = ("Arial",15))
lbl_requirements = ttk.Label(lblfr_college, text = "Requirements:",font =("Arial",15))

txt_name = ttk.Entry(lblfr_college)
txt_tuition_fees = ttk.Entry(lblfr_college)
txt_accomodation_cost = ttk.Entry(lblfr_college)
txt_rank_sw = ttk.Entry(lblfr_college)
txt_program = ttk.Entry(lblfr_college)
txt_location = ttk.Entry(lblfr_college)
txt_requirements = ttk.Entry(lblfr_college)


#Function for page 2 

#Treeview
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 13)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=("Noteworthy", 15)) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders




tree = ttk.Treeview(page2, columns = ("Fees","Accomo.","Program","Rank","Location","Requirements"))#style="mystyle.Treeview"

tree.heading('#0', text="College")
tree.heading("Fees", text="Tuition fees")
tree.heading("Accomo.", text="Accomodation cost")
tree.heading("Program", text = "Program")
tree.heading("Rank", text="Ranking SW")
tree.heading("Location", text = "Location")
tree.heading("Requirements", text = "Requirements")
def insert():
	if  txt_name.get() == "" or txt_tuition_fees.get() == "" or txt_program.get() == "" or txt_requirements.get() == "":
		messagebox.showinfo("Empty", "Please enter a name")
	else:
	#c.execute("""CREATE TABLE employees (
							#first text
							#)""")
		#c.execute("""CREATE TABLE college_data(
							#"Name of college " TEXT
							#"Tuition fees" INTEGER
							#"Accomodation cost" INTEGER
							#"Program" TEXT
							#"Rank SW" INTEGER
							#"Location" TEXT
							#"Requirements" TEXT
							#)""")
		c.execute("INSERT INTO college_data ('Name of College','Tuition Fees', 'Accomodation cost', 'Program applied', 'Rank SW', 'Location', 'Requirements') VALUES (?,?,?,?,?,?,?)", ( txt_name.get(), txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get()))
		conn.commit()
		tree.insert("", "end", text=txt_name.get(), values=(txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get()))
		messagebox.showinfo("Update", "Successfully added to the database.")
btn_add = ttk.Button(lblfr_college,text = "Add", command = insert)
lblfr_college.grid(row = 0, column = 0, sticky = "nw")
lbl_name.grid(row = 0, column = 0)
lbl_tuition_fees.grid(row = 1, column = 0)
lbl_accomodation_cost.grid(row = 2, column = 0)
lbl_rank_sw.grid(row = 3, column = 0)
lbl_program.grid(row = 4, column = 0)
lbl_location.grid(row = 5, column = 0)
lbl_requirements.grid(row = 6, column = 0)
txt_name.grid(row = 0, column = 1)
txt_tuition_fees.grid(row = 1, column = 1)
txt_accomodation_cost.grid(row = 2, column = 1) 
txt_rank_sw.grid(row = 3, column = 1)
txt_program.grid(row = 4, column = 1) 
txt_location.grid(row = 5, column = 1)
txt_requirements.grid(row = 6, column = 1)
tree.grid(row = 1, column = 0, rowspan = 10)
btn_add.grid(row = 6, column = 3)

#activities tab interior

#txt_name = tkinter.Entry(root, width= 10)
#txt_name.grid( row = 0,column = 0)
# College application deadlines tab interior
# activity tab interior



root.mainloop()