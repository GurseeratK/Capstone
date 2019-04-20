import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3 
from sqlite3 import Error

root = tkinter.Tk()
root.title("Python Capstone Project")
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
lbl_index = ttk.Label(lblfr_college,text = "IDX")
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
#Treeview
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 13)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=("Noteworthy", 15)) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

tree = ttk.Treeview(page2, selectmode ="browse",columns = ("College","Fees","Accomo.","Program","Rank","Location","Requirements","doc","app"))#style="mystyle.Treeview"
scrollbar_horizontal = ttk.Scrollbar(page2, orient='horizontal', command = tree.xview)    

tree.heading('#0', text="IDX")
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
                                    "school years" integer,
                                    "years" integer NOT NULL,
                                    "hours per week" integer NOT NULL,
                                    "weeks per year" integer NOT NULL,
                                    "status" text NOT NULL,
                                    "description" text
                                );"""
 
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
    sql = " INSERT INTO extracurricular_activities('IDX','activity','type','school years','years','hours per week','weeks per year','status','description') VALUES(?,?,?,?,?,?,?,?,?)"
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
def read_from_database():
    database = "pythonsqlite3.db"
    conn = return_conn(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM college_info")
    rows = cur.fetchall()
    for row in rows:
    	tree.insert("", "end", text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

read_from_database()

def main_to_insert_in_table():
	database = "pythonsqlite3.db"
 
    # create a database connection
	conn = return_conn(database)
	with conn:
        # create a new project
		#activity_1 = (txt_index.get(),txt_activity.get(),txt_type.get(),txt_school_years.get(),txt_years.get(),txt_hr_wk.get(),txt_wk_yr.get(),txt_status.get(),txt_description.get())#
		#create_activity(conn, activity_1)
 
        # tasks
		college_1 =(txt_index.get(),txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get())
        #college_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
 
        # create tasks
		create_college_info(conn, college_1)
		tree.insert("", "end", text=txt_index.get(), values=(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get()))
		messagebox.showinfo("Update", "Successfully added to database.")

       # create_college_info(conn, college_2)

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

tree.bind('<<TreeviewSelect>>', selected_item)
def delete_college(conn, IDX):
	
	sql = "DELETE FROM college_info WHERE IDX=?"
	cur = conn.cursor()
	cur.execute(sql, (IDX,))


def delete_all_colleges(conn):
    sql = "DELETE FROM college_info"
    cur = conn.cursor()
    cur.execute(sql)
	
def main_to_delete():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		tree.delete(tree.selection())
		delete_college(conn,txt_index.get())

def main_to_delete_all():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		database = "pythonsqlite3.db"
		for i in tree.get_children():
			tree.delete(i)
		delete_all_colleges(conn)
		
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

    
def main_update():
    database = "pythonsqlite3.db"
 
    # create a database connection
    conn = return_conn(database)
    with conn:
        update_college(conn, (txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get(),txt_index.get()))
        
btn_insertion = ttk.Button(lblfr_college,text = "Add to Database",command =main_to_insert_in_table)
btn_insertion.grid(row = 6, column = 4)
btn_delete = ttk.Button(lblfr_college,text ="Delete",command = main_to_delete)
btn_delete_all = ttk.Button(lblfr_college,text ="Delete All",command = main_to_delete_all)
btn_delete_all.grid(row = 6, column = 5)
btn_delete.grid(row = 6, column = 6)
btn_update = ttk.Button(lblfr_college,text = "Update",command = main_update)
btn_update.grid(row = 6, column = 7)
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

#if __name__ == '__main__':
	#main_to_insert_in_table()    


#if __name__ == '__main__':
   # main()
root.mainloop()





        #delete_all_activities(conn)
#if __name__ == '__main__':
	#main_to_delete()

def update_college(conn, college_entry):
    sql = """ UPDATE college_info
              SET 'name' = ? ,
                  'tuition fees' = ? ,
                  'accomodation cost' = ?
                  'program' = ?
                  'competitiveness'=?
                  'location'=?
                  'requirements'=?
                  'document submission deadline'=?
                  'application deadline'=?
              WHERE IDX = ?"""
    cur = conn.cursor()
    cur.execute(sql, college_entry)
    
def main_update():
    database = "pythonsqlite3.db"
 
    # create a database connection
    conn = return_conn(database)
    with conn:
        update_college(conn, (txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get(),txt_index.get()))

 






















#for row in c.fetchall():
	#print(row)
# -----  end



        	
#code for word count

