import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# downloaded DB Browser for SQLite
import sqlite3 # for database
root = tkinter.Tk()
#root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#print(root.filename)


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
#lblfr_profile = ttk.LabelFrame(page1, text = "MY PROFILE") # not working
#lblfr_profile.grid(row = 4, column = 1,sticky = "nw") # not working
hobbies = tkinter.Text(page1, width = 40, height = 5, wrap = "word")

career = tkinter.Text(page1, width = 40, height = 5, wrap = "word")
lbl_career = ttk.Label(page1, text = "What are your career aspirations:")
lbl_hobbies = ttk.Label(page1, text = "Hobbies:")
lbl_name = ttk.Label(page1, text=" Full name:")
lbl_age = ttk.Label(page1, text="Age:")
lbl_dob = ttk.Label(page1, text="DOB:\n*(dd/mm/yyyy)")
lbl_gender = ttk.Label(page1, text="Gender:")
lbl_space = ttk.Label(page1, text = "")
btn_save = ttk.Button(page1, text = "Save", command = lambda: clicked)
btn_update = ttk.Button(page1, text = "Update", command = lambda:clicked)
var_chk = IntVar()
rdl_1 = ttk.Radiobutton(page1,text = "Male", variable = var_chk, value = 1)
rdl_2 = ttk.Radiobutton(page1,text = "Female", variable = var_chk, value = 2)
rdl_3 = ttk.Radiobutton(page1,text = "Other", variable = var_chk, value = 3)
txt_name.grid(row = 0, column = 2)
txt_age.grid(row = 1, column = 2)
txt_dob.grid(row = 2, column =2)
hobbies.grid(row = 4, column = 2, rowspan = 4)
lbl_space.grid(row = 8, column = 2)
career.grid(row = 9, column = 2, rowspan = 4) #
lbl_name.grid(row = 0, column = 1 )
lbl_age.grid(row = 1, column = 1)
lbl_dob.grid(row =2 , column = 1)
lbl_gender.grid(row = 3, column = 1)
lbl_hobbies.grid(row = 4, column = 1)
lbl_career.grid(row = 9, column = 1) #
rdl_1.grid(row =3, column = 2, sticky = "w")
rdl_2.grid(row =3, column = 2, sticky = "")
rdl_3.grid(row =3, column = 2, sticky = "e")
btn_update.grid(row= 13, column = 2)
btn_save.grid(row =13, column = 1)

#College deadlines tab interior
#FUNCTIONS

#College widgets
lblfr_college = ttk.LabelFrame(page2, text = "") # Information labelframe - top
lbl_name = ttk.Label(lblfr_college, text = "Name of College: *", font = ("Arial", 15))
lbl_tuition_fees = ttk.Label(lblfr_college, text = "Tuition fees: *", font = ("Arial",15))
lbl_accomodation_cost = ttk.Label(lblfr_college, text = "Accomodation cost: ", font = ("Arial",15))
lbl_rank_sw = ttk.Label(lblfr_college, text = "Ranking SW: ", font = ("Arial",15))
lbl_program = ttk.Label(lblfr_college, text = "Program applied:*", font = ("Arial",15))
lbl_location = ttk.Label(lblfr_college, text = "Location: ", font = ("Arial",15))
lbl_requirements = ttk.Label(lblfr_college, text = "Requirements:*",font =("Arial",15))

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

tree = ttk.Treeview(page2, columns = ("Fees","Accomo.","Program","Rank","Location","Requirements", "mystyle.Treeview"))#style="mystyle.Treeview"
tree.heading('#0', text="College",anchor = "w")
tree.heading("Fees", text="Tuition fees",anchor = "w")
tree.heading("Accomo.", text="Accomodation cost",anchor = "w")
tree.heading("Program", text = "Program",anchor = "w")
tree.heading("Rank", text="Ranking SW",anchor = "w")
tree.heading("Location", text = "Location",anchor = "w")
tree.heading("Requirements", text = "Requirements",anchor = "w")
# searching and updating the database - working on it
#lbl_id = ttk.Label(lblfr_college,text = "Id:")
#txt_id = ttk.Entry(lblfr_college)
#lbl_id.grid(row = 8 , column = 0)
#txt_id.grid(row = 8, column = 1)
#btn_search = ttk.Button(lblfr_college, text = "Search id", command = search)
#def search():

	#sql = "SELECT * FROM college_data WHERE id = ?"
	#results = c.execute(sql, (txt_id.get(), ))
	#for r in results:
		 #txt_name.get()= r[1]
		#txt_tuition_fees.get()  = r[2]
		#txt_accomodation_cost.get() =r[3]
		#txt_rank_sw.get()= r[4]
		#txt_program.get()= r[5]
		#txt_location.get() = r[6]
		#txt_requirements.get() = r[7]
	#conn.commit()
	#txt_name.delete(0, "end")
	#txt_name.insert(0, txt_name)
	
#def update():
#	pass
# -----  end

def insert():
	if  txt_name.get() == "" or txt_tuition_fees.get() == "" or txt_program.get() == "" or txt_requirements.get() == "":
		messagebox.showinfo("Error", "Please enter the minimum required fields.(marked by *)")
	else:
			#Creating a table college_data in the database college_info.db
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
			messagebox.showinfo("Update", "Successfully added to the college_info database.")

def delete():      
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete selected data entry.")
        if confirm == True:
        	selected_item = tree.selection()[0]
        	tree.delete(selected_item)
        	
#code for word count

btn_add = ttk.Button(lblfr_college,text = "Add", command = insert)
btn_delete = ttk.Button(lblfr_college, text = "Delete", command = delete)
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
btn_delete.grid(row = 6 , column = 4)

#Activities tab interior
def length_of_text(event):
	text = general_description.get("1.0", "end-1c").split(" ")
	txt_word_count.delete(0,"end")
	txt_word_count.insert(0, "{}".format(len(text)))
	lbl_word_alert = ttk.Label(lblfr_text,text = "                                                                                                                                      ", font = ("Arial",15) ,foreground = "red", justify = "left")
	lbl_word_alert.grid(row = 1, column = 0)
	
	if len(text)>100:		
		lbl_word_alert["text"] = " You have exceeded the maximum word length by {}. Please shorten your response.".format(len(text)-100)
		
	if len(text) <= 100:
		lbl_word_alert["text"] =  "                                                                                                                                      "
                                          									
def remove():
	confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete selected data entry.")
	if confirm == True:
		selected_item = tree_2.selection()[0]
		tree_2.delete(selected_item)
        
lblfr_activity = ttk.LabelFrame(page3, text = "Extracurricular inforamtion") # Information labelframe - top
lblfr_text = ttk.LabelFrame(page3, text = "Description(in less than 100 words):")
lbl_word_alert = ttk.Label(lblfr_text,text = "                                                                                                                                      ", font = ("Arial",15) ,foreground = "red", justify = "left")
lbl_word_alert.grid(row = 1, column = 0)
lbl_activity = ttk.Label(lblfr_activity, text = "Extracurricular Activity: *", font = ("Arial", 15))
lbl_type = ttk.Label(lblfr_activity, text = "Type: *", font = ("Arial",15))
lbl_time_period = ttk.Label(lblfr_activity, text = "No of years involved: *", font = ("Arial",15))
lbl_grade = ttk.Label(lblfr_activity, text = "Grade (former grade - later grade): *", font = ("Arial",15))
lbl_week = ttk.Label(lblfr_activity, text = "Time spent per week(in hours): *", font = ("Arial",15))
lbl_award = ttk.Label(lblfr_activity, text = "Any distinction or award received : ", font = ("Arial",15))
general_description = tkinter.Text(lblfr_text, width = 70, height = 10, bg = "black", fg = "white", wrap = "word")
general_description.configure(insertbackground= "white")#to make the cursor white so that we can keep track of it
general_description.bind("<Key>", length_of_text)
txt_word_count = ttk.Entry(lblfr_text, width = 10)
txt_word_count.grid(row = 2, column = 0)
txt_activity = ttk.Entry(lblfr_activity)
txt_type = ttk.Entry(lblfr_activity)
txt_time_period = ttk.Entry(lblfr_activity)
txt_grade = ttk.Entry(lblfr_activity)
txt_week = ttk.Entry(lblfr_activity)
txt_award = ttk.Entry(lblfr_activity)
tree_2 = ttk.Treeview(page3, columns = ("type","years","grade","time_week","award"))
tree_2.heading('#0', text="Extracurricular Activity")
tree_2.heading("type", text="Type")
tree_2.heading("years", text="No. of years ")
tree_2.heading("grade", text = "Grade")
tree_2.heading("time_week", text = "Time spentper week(in hrs)")
tree_2.heading("award", text="Distinction or Award")

def add():
	if  txt_activity.get() == "" or txt_type.get() == "" or txt_grade.get() == "" or txt_time_period.get() == "" or txt_week == "":
		messagebox.showinfo("Error", "Please enter the minimum required fields(marked by *).")
	else:
		#Creating a table co-curricular activity in the database college_info.db
			
		#c.execute("""CREATE TABLE Extracurricular Activity(
						#"Extracurricular Activity" TEXT
						#"Type" TEXT
						#"No. of years" INTEGER
						#"Grade" INTEGER
						#"Time spent per week(in hrs)" INTEGER
						#"Distinction or Award" TEXT
						#"Description" TEXT
						#)""")general_description.get("1.0", "end-1c")
			
		c.execute("INSERT INTO activity ('Extracurricular Activity','Type', 'No. of years', 'Grade', 'Time spent per week(in hrs)', 'Distinction or Award','Description') VALUES (?,?,?,?,?,?,?)", ( txt_activity.get(), txt_type.get(),txt_time_period.get(),txt_grade.get(),txt_week.get(),txt_award.get(),general_description.get("1.0", "end-1c")))
		conn.commit()
		tree_2.insert("", "end", text=txt_activity.get(), values=(txt_type.get(),txt_time_period.get(),txt_grade.get(),txt_week.get(),txt_award.get(),general_description.get("1.0", "end-1c")))
		messagebox.showinfo("Update", "Successfully added to the college_info database.")
			
btn_add = ttk.Button(lblfr_activity,text = "Add", command = add)
btn_remove = ttk.Button(lblfr_activity, text = "Delete", command = remove)	
lblfr_activity.grid(row = 0, column = 0, sticky = "w")
lblfr_text.grid(row = 0, column = 0, sticky = 'e')
general_description.grid(row = 0, column = 0)
lbl_activity.grid(row = 0, column = 0)
lbl_type.grid(row = 1, column = 0)
lbl_time_period.grid(row = 2, column = 0)
lbl_grade.grid(row = 3, column = 0)
lbl_week.grid(row = 4, column = 0)
lbl_award.grid(row = 5, column = 0)
txt_activity.grid(row = 0, column = 1)
txt_type.grid(row = 1, column = 1)
txt_time_period.grid(row = 2, column = 1) 
txt_grade.grid(row = 3, column = 1)
txt_week.grid(row = 4, column = 1) 
txt_award.grid(row = 5, column = 1)
tree_2.grid(row = 6, column = 0)
btn_add.grid(row = 6, column = 0)
btn_remove.grid(row = 6, column = 1)

# College application deadlines tab interior
# activity tab interior



root.mainloop()