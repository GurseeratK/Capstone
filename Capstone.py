import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3 
from sqlite3 import Error
# use text files method to store information and find ways to update it successfully 
# for weekend, if can upload image of yourself
root = tkinter.Tk()
root.title("College Application Tracker")
root.configure(background = "lightgrey")
#root.resizable(False, False)
#conn = sqlite3.connect("pythonsqlite3.db") 
#c = conn.cursor()
nb = ttk.Notebook(root, width = 1380, height = 730)
nb.grid(row = 1, column = 0 )
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
nb.add(page1, text="Profile")
nb.add(page2, text ="College Application Deadlines")
nb.add(page3, text="Extracurricular Activities")
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
lblfr_college = ttk.LabelFrame(page2, text = "College Information") # Information labelframe - top
lbl_index = ttk.Label(lblfr_college,text = "Index no.")
lbl_name = ttk.Label(lblfr_college, text = "Name of College: *", font = ("Arial", 15))
lbl_tuition_fees = ttk.Label(lblfr_college, text = "Tuition fees: *", font = ("Arial",15))
lbl_accomodation_cost = ttk.Label(lblfr_college, text = "Accomodation cost: ", font = ("Arial",15))
lbl_program = ttk.Label(lblfr_college, text = "Program applied:*", font = ("Arial",15))
lbl_rank_sw = ttk.Label(lblfr_college, text = "Competitiveness(out of 10): ", font = ("Arial",15))
lbl_location = ttk.Label(lblfr_college, text = "Location: ", font = ("Arial",15))
lbl_requirements = ttk.Label(lblfr_college, text = "Requirements:*",font =("Arial",15))
lbl_doc_deadline = ttk.Label(lblfr_college, text = "Documents submission deadline:(mm/dd/yyyy)*",font =("Arial",15))
lbl_application_deadline = ttk.Label(lblfr_college, text = "Application submission deadline:(mm/dd/yyyy)*",font =("Arial",15))
txt_index = ttk.Entry(lblfr_college)
txt_name = ttk.Entry(lblfr_college)
txt_tuition_fees = ttk.Entry(lblfr_college)
txt_accomodation_cost = ttk.Entry(lblfr_college)
txt_rank_sw = ttk.Entry(lblfr_college)
txt_program = ttk.Entry(lblfr_college)
txt_location = ttk.Entry(lblfr_college)
txt_requirements = ttk.Entry(lblfr_college)
txt_doc = ttk.Entry(lblfr_college)
txt_app = ttk.Entry(lblfr_college)
# Functions
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

# Activity widgets
lblfr_activity = ttk.LabelFrame(page3, text = "Extracurricular Inforamtion")
lblfr_text = ttk.LabelFrame(page3, text = "Description(in less than 100 words):") #
lbl_word_alert = ttk.Label(lblfr_text,text = "                                                                                                                                      ", font = ("Arial",15) ,foreground = "red", justify = "left")
lbl_activity = ttk.Label(lblfr_activity, text = "Extracurricular Activity: *", font = ("Arial", 15))
lbl_type = ttk.Label(lblfr_activity, text = "Type: *", font = ("Arial",15))
lbl_sch_years = ttk.Label(lblfr_activity, text = "School years involved in activity: *", font = ("Arial",15))
lbl_years = ttk.Label(lblfr_activity, text = "No. of years involved in activity: *", font = ("Arial",15))
lbl_hrs_per_wk = ttk.Label(lblfr_activity, text = "Time spent per week (in hours): *", font = ("Arial",15))
lbl_wks_per_yr = ttk.Label(lblfr_activity, text = "Weeks spent per year : ", font = ("Arial",15))
lbl_status = ttk.Label(lblfr_activity,text = "Status([A]ctive/[U]nactive): ",font = ("Arial",15))
lbl_index_2 = ttk.Label(lblfr_activity,text = "Index no.", font = ("Arial",15))
txt_index_2 = ttk.Entry(lblfr_activity)
txt_activity = ttk.Entry(lblfr_activity)
txt_type = ttk.Entry(lblfr_activity)
txt_sch_years = ttk.Entry(lblfr_activity)
txt_years = ttk.Entry(lblfr_activity)
txt_hrs_per_wk= ttk.Entry(lblfr_activity)
txt_wks_per_yr= ttk.Entry(lblfr_activity)
txt_status = ttk.Entry(lblfr_activity)
general_description = tkinter.Text(lblfr_text, width = 70, height = 10, bg = "black", fg = "white", wrap = "word") #
general_description.configure(insertbackground= "white")#to make the cursor white so that we can keep track of it
general_description.bind("<Key>", length_of_text) #
general_description.grid(row = 0, column = 0)
txt_word_count = ttk.Entry(lblfr_text, width = 10)
txt_word_count.grid(row = 2, column = 0)
#Treeview

tree = ttk.Treeview(page2, selectmode ="browse",columns = ("College","Fees","Accomo.","Program","Rank","Location","Requirements","doc","app"))
scrollbar_horizontal = ttk.Scrollbar(page2, orient='horizontal', command = tree.xview)    
tree.heading("#0", text="IDX")
tree.column("#0",width=50)
tree.heading("College",text = "College")
tree.heading("Fees", text="Tuition fees")
tree.column("Fees",width = 100)
tree.column("Accomo.",width = 150)
tree.heading("Accomo.", text="Accomodation cost")
tree.heading("Program", text = "Program")
tree.heading("Rank", text="Competitiveness")
tree.column("Rank",width = 100)
tree.heading("Location", text = "Location")
tree.heading("Requirements", text = "Requirements")
tree.heading("doc",text="Doc deadline")
tree.heading("app",text="App deadline")
tree.column("doc",width =100)
tree.column("app",width =100)
tree.column("Location",width =150)

tree_2 = ttk.Treeview(page3, columns = ("activity","type","sch_years","years","hrs_per_wk","wk_per_yr","status","description"))
tree_2.heading("#0", text="IDX")
tree_2.heading("activity", text="Activity")
tree_2.heading("type", text="Type")
tree_2.heading("sch_years", text = "School years")
tree_2.heading("years", text = "No. of years")
tree_2.heading("hrs_per_wk", text="hrs/wk")
tree_2.heading("wk_per_yr",text = "wks/yr")
tree_2.heading("status",text = "Status (Active/Unactive)")
tree_2.column("#0",width = 50)
tree_2.column("sch_years",width = 100)
tree_2.column("years",width = 100)
tree_2.column("hrs_per_wk",width = 100)
tree_2.column("wk_per_yr",width = 100)
tree_2.column("status",width = 150)
tree_2.heading("description",text = "Description")
tree_2.column("description",width = 350)

#Grid for activity tab(page 3)
lblfr_activity.grid(row = 0, column = 0, sticky = "w")
lblfr_text.grid(row = 0, column = 0, sticky = 'ne') #
lbl_activity.grid(row = 0, column = 0)
lbl_type.grid(row = 1, column = 0)
lbl_sch_years.grid(row = 2, column = 0)
lbl_years.grid(row = 3, column = 0)
lbl_hrs_per_wk.grid(row = 4, column = 0)
lbl_wks_per_yr.grid(row = 5, column = 0)
lbl_status.grid(row = 6, column = 0)
lbl_index_2.grid(row = 7, column = 0)
txt_activity.grid(row = 0, column = 1)
txt_type.grid(row = 1, column = 1)
txt_sch_years.grid(row = 2, column = 1) 
txt_years.grid(row = 3, column = 1)
txt_hrs_per_wk.grid(row = 4, column = 1) 
txt_wks_per_yr.grid(row = 5, column = 1)
txt_status.grid(row = 6, column = 1)
txt_index_2.grid(row = 7, column = 1)
tree_2.grid(row = 1, column = 0, rowspan = 10)
lbl_word_alert.grid(row = 1, column = 0)

# Grid for college tab
lblfr_college.grid(row = 0, column = 0, sticky = "nw")
lbl_name.grid(row = 0, column = 0)
lbl_tuition_fees.grid(row = 1, column = 0)
lbl_accomodation_cost.grid(row = 2, column = 0)
lbl_rank_sw.grid(row = 3, column = 0)
lbl_program.grid(row = 4, column = 0)
lbl_location.grid(row = 5, column = 0)
lbl_requirements.grid(row = 6, column = 0)
lbl_doc_deadline.grid(row =7, column = 0)
lbl_application_deadline.grid(row = 8, column = 0)
lbl_index.grid(row = 9, column = 0)
txt_name.grid(row = 0, column = 1)
txt_tuition_fees.grid(row = 1, column = 1)
txt_accomodation_cost.grid(row = 2, column = 1) 
txt_rank_sw.grid(row = 3, column = 1)
txt_program.grid(row = 4, column = 1) 
txt_location.grid(row = 5, column = 1)
txt_requirements.grid(row = 6, column = 1)
tree.grid(row = 1, column = 0, rowspan = 10)
txt_doc.grid(row =7, column = 1)
txt_app.grid(row = 8, column = 1)
txt_index.grid(row = 9, column = 1)

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        #print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    create_connection("pythonsqlite3.db")
 
# creating two tables in pythonsqlite3 database
def return_conn(db_file):
    
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
    
def create_table(conn, create_table_sql):
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main_to_create_table():
    database = "pythonsqlite3.db"
    
    sql_create_college_info_table = """ CREATE TABLE IF NOT EXISTS college_info (
                                        "IDX" integer PRIMARY KEY,
                                        "name" text NOT NULL,
                                        "tuition fees" text,
                                        "accomodation cost" text,
                                        "program" text,
                                        "competitiveness" text,
                                        "location" text,
                                        "requirements" text,
                                        "document submission deadline" text,
                                        "application deadline" text
                                    ); """
 
    sql_create_activity_table = """CREATE TABLE IF NOT EXISTS extracurricular_activities (
                                   "IDX" integer PRIMARY KEY,
                                    "activity" text NOT NULL,
                                    "type" text,
                                    "school years" numeric,
                                    "years" integer NOT NULL,
                                    "hours per week" integer NOT NULL,
                                    "weeks per year" integer NOT NULL,
                                    "status" text NOT NULL,
                                    "description" text 
                                );"""
 #                                    "description" text added
 
    # create a database connection
    conn = return_conn(database)
    if conn is not None:
        # create college_info table
        create_table(conn, sql_create_college_info_table)
        # create activity table
        create_table(conn, sql_create_activity_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main_to_create_table()
    
def create_activity(conn, activity_entry):
    sql = " INSERT INTO extracurricular_activities('IDX','activity','type','school years','years','hours per week','weeks per year','status','description') VALUES(?,?,?,?,?,?,?,?,?)" #,'description')
    cur = conn.cursor()
    cur.execute(sql, activity_entry)
    conn.commit()
    return cur.lastrowid # to return the index
def create_college_info(conn, college_entry):
 
    sql = " INSERT INTO college_info('IDX','name','tuition fees','accomodation cost','program','competitiveness','location','requirements','document submission deadline','application deadline') VALUES(?,?,?,?,?,?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, college_entry)
    conn.commit()
    return cur.lastrowid
    
def read_from_database_1():
    database = "pythonsqlite3.db"
    conn = return_conn(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM college_info")
    rows = cur.fetchall()
    for row in rows:
    	tree.insert("", "end", text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

read_from_database_1()

def read_from_database_2():
	database = "pythonsqlite3.db"
	conn = return_conn(database)
	cur = conn.cursor()
	cur.execute("SELECT * FROM extracurricular_activities")
	rows = cur.fetchall()
	for row in rows:
		tree_2.insert("", "end", text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

read_from_database_2()

def main_to_insert_in_table_2():
	database = "pythonsqlite3.db"
 
    # create a database connection
	conn = return_conn(database)
	with conn:
		activity_1 = (txt_index_2.get(),txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0", "end-1c"))#,description.get("1.0", "end-1c"))
		create_activity(conn, activity_1)
		tree_2.insert("","end",text = txt_index_2.get(),values =(txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0", "end-1c")))#,description.get("1.0", "end-1c")))
		messagebox.showinfo("Update","Successfully added to database.")
 		
def main_to_insert_in_table():
	database = "pythonsqlite3.db"
 # create a database connection
	conn = return_conn(database)
	with conn:
		college_1 =(txt_index.get(),txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get())
		create_college_info(conn, college_1)
		tree.insert("", "end", text=txt_index.get(), values=(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get()))
		messagebox.showinfo("Update", "Successfully added to database.")

def selected_item(a): 
	database = "pythonsqlite3.db"
	conn = return_conn(database)
	cur = conn.cursor()
	idx =  tree.item(tree.focus())['text']
	txt_index.delete(0,"end")
	txt_index.insert(0,idx)
	sql = cur.execute("SELECT * FROM college_info where IDX=?",(txt_index.get(),))
	for item in sql:
		name = item[1]
		tuition_fees = item[2]
		accomodation_cost= item[3]
		program= item[4]
		competitiveness=item[5]
		location= item[6]
		requirements= item[7]
		doc = item[8]
		app = item[9]
	conn.commit()
	txt_name.delete(0,"end")
	txt_tuition_fees.delete(0,"end")
	txt_accomodation_cost.delete(0,"end")
	txt_program.delete(0,"end")
	txt_rank_sw.delete(0,"end")
	txt_location.delete(0,"end")
	txt_requirements.delete(0,"end")
	txt_doc.delete(0,"end")
	txt_app.delete(0,"end")
	txt_tuition_fees.insert(0,tuition_fees)
	txt_name.insert(0,name)
	txt_accomodation_cost.insert(0,accomodation_cost)
	txt_program.insert(0,program)
	txt_rank_sw.insert(0,competitiveness)
	txt_location.insert(0,location)
	txt_requirements.insert(0,requirements)
	txt_doc.insert(0,doc)
	txt_app.insert(0,app)

def selected_item_2(a):
	database = "pythonsqlite3.db"
	conn = return_conn(database)
	cur = conn.cursor()
	idx_2 =  tree_2.item(tree_2.focus())['text']
	txt_index_2.delete(0,"end")
	txt_index_2.insert(0,idx_2)
	sql = cur.execute("SELECT * FROM extracurricular_activities where IDX=?",(txt_index_2.get(),))
	for item in sql:
		activity = item[1]
		type = item[2]
		sch_years= item[3]
		years= item[4]
		hrs_per_wk=item[5]
		wks_per_year= item[6]
		status= item[7]
		description = item[8]
	conn.commit()
	
	txt_activity.delete(0,"end")
	txt_type.delete(0,"end")
	txt_sch_years.delete(0,"end")
	txt_years.delete(0,"end")
	txt_hrs_per_wk.delete(0,"end")
	txt_wks_per_yr.delete(0,"end")
	txt_status.delete(0,"end")
	#general_description.delete(1.0,"end") #txt_description.delete(0,"end")
	txt_activity.insert(0,activity)
	txt_type.insert(0,type)
	txt_sch_years.insert(0,sch_years)
	txt_years.insert(0,years)
	txt_hrs_per_wk.insert(0,hrs_per_wk)
	txt_wks_per_yr.insert(0,wks_per_year)
	txt_status.insert(0,status)
	general_description.delete(1.0,"end")
	general_description.insert("end",description) # insert into decription
	text = general_description.get("1.0", "end-1c").split(" ")
	txt_word_count.delete(0,"end")
	txt_word_count.insert(0, "{}".format(len(text)))
	#length_of_text()
	#txt_description.insert(0,description)
	
tree.bind('<<TreeviewSelect>>', selected_item)
tree_2.bind('<<TreeviewSelect>>', selected_item_2)

def delete_college(conn, IDX):
	sql = "DELETE FROM college_info WHERE IDX=?"
	cur = conn.cursor()
	cur.execute(sql, (IDX,))

def delete_activity(conn, IDX):
	sql = "DELETE FROM extracurricular_activities WHERE IDX=?"
	cur = conn.cursor()
	cur.execute(sql, (IDX,))

def delete_all_colleges(conn):
    sql = "DELETE FROM college_info"
    cur = conn.cursor()
    cur.execute(sql)

def delete_all_activities(conn):
    sql = "DELETE FROM extracurricular_activities"
    cur = conn.cursor()
    cur.execute(sql)

def main_to_delete():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		tree.delete(tree.selection())
		delete_college(conn,txt_index.get())

def main_to_delete_2():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		tree_2.delete(tree_2.selection())
		delete_activity(conn,txt_index_2.get())
	
def main_to_delete_all():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		database = "pythonsqlite3.db"
		for i in tree.get_children():
			tree.delete(i)
		delete_all_colleges(conn)
		
def main_to_delete_all_2():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		database = "pythonsqlite3.db"
		for i in tree_2.get_children():
			tree_2.delete(i)
		delete_all_activities(conn)
		
def update_college(conn, college_entry):
    sql = '''UPDATE college_info
              SET 'name' = ? ,
                  'tuition fees' = ? ,
                  'accomodation cost' = ?,
                  'program' = ?,
                  'competitiveness'=?,
                  'location'=?,
                  'requirements'=?,
                  'document submission deadline'=?,
                  'application deadline'=?
              WHERE IDX = ? '''
    cur = conn.cursor()
    cur.execute(sql, college_entry)
    tree.item(tree.selection(), text=txt_index.get(), values=(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get()))
#'IDX','activity','type','school years','years','hours per week','weeks per year','status

def update_activity(conn, activity_entry):
    sql = '''UPDATE extracurricular_activities
              SET 'activity' = ? ,
                  'type' = ? ,
                  'school years' = ?,
                  'years' = ?,
                  'hours per week'=?,
                  'weeks per year'=?,
                  'status'=?,
                  'description'=?
              WHERE IDX = ? '''
    cur = conn.cursor()
    cur.execute(sql, activity_entry)
    		#tree_2.insert("","end",text = txt_index_2.get(),values =(txt_activity.get(),txt_type.get(),txt_school_years.get(),txt_years.get(),txt_hr_wk.get(),txt_wk_yr.get(),txt_status.get()))#,description.get("1.0", "end-1c")))
	
    tree_2.item(tree_2.selection(),text = txt_index_2.get(),values =(txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0", "end-1c"),txt_index_2.get()))#,description.get("1.0", "end-1c")))

def main_update():
    database = "pythonsqlite3.db"
    # create a database connection
    conn = return_conn(database)
    with conn:
        update_college(conn,(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get(),txt_index.get()))
        
def main_update_2():
    database = "pythonsqlite3.db"
    # create a database connection
    conn = return_conn(database)
    with conn:
        update_activity(conn,(txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0", "end-1c"),txt_index_2.get()))#,description.get("1.0", "end-1c")))

btn_insertion_2 = ttk.Button(lblfr_activity,text = "Add to Database",command =main_to_insert_in_table_2)
btn_insertion_2.grid(row = 8, column = 4)
btn_delete_2 = ttk.Button(lblfr_activity,text ="Delete",command = main_to_delete_2)
btn_delete_all_2 = ttk.Button(lblfr_activity,text ="Delete All",command = main_to_delete_all_2)
btn_delete_all_2.grid(row = 8, column = 5)
btn_delete_2.grid(row = 8, column = 6)
btn_update_2 = ttk.Button(lblfr_activity,text = "Update",command = main_update_2)
btn_update_2.grid(row = 8, column = 7)

# Grid for college tab(page 2)
btn_insertion = ttk.Button(lblfr_college,text = "Add to Database",command =main_to_insert_in_table)
btn_insertion.grid(row = 10, column = 0)
btn_delete = ttk.Button(lblfr_college,text ="Delete",command = main_to_delete)
btn_delete_all = ttk.Button(lblfr_college,text ="Delete All",command = main_to_delete_all)
btn_delete_all.grid(row = 10, column = 1)
btn_delete.grid(row = 10, column = 2)
btn_update = ttk.Button(lblfr_college,text = "Update",command = main_update)
btn_update.grid(row = 10, column = 3)
    
root.mainloop()





        


 























