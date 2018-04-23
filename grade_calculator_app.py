import tkinter
from tkinter import ttk
import pickle
from tkinter import messagebox

root = tkinter.Tk()
root.resizable(width = False, height = False) # Keeping the window size constant

root.title("Grade tracker")

# Tabs
notebook = ttk.Notebook(root)

# Creating tabs
home = ttk.Frame(notebook)
sem_1 = ttk.Frame(notebook)
sem_2 = ttk.Frame(notebook)
exam = ttk.Frame(notebook)

# Setting tab names
notebook.add(home, text = "Home")
notebook.add(sem_1, text = "Semester 1")
notebook.add(sem_2, text = "Semester 2")
notebook.add(exam, text = "Exam")

notebook.grid(row = 0)

# Dictionary/List
basic_info = {}
topics_sem1 = []
topics_sem2 = []


# Functions for buttons
def update_listbox():    
  for topic in topics_sem1:
    lb_topic.insert("end", topic)
  for topic2 in topics_sem2:
    lb_topic2.insert("end", topic2)

def update_listbox_delete():
  lb_topic.delete(0, "end")
  lb_topic2.delete(0, "end")

# Home
def save():
  pickle.dump(basic_info, open("basic_info.dat", "wb")) # saving the data

def apply_subject():
  if txt_name.get() != " " and txt_kind.get() != " " and txt_assigment.get() != " " and txt_test.get() != " " and txt_rest.get() != " " and (int(txt_assigment.get()) + int(txt_test.get()) + int(txt_rest.get()) == 100):
    key = txt_name.get()
    value = [txt_kind.get(), txt_assigment.get(), txt_test.get(), txt_rest.get()]
    basic_info[key] = value
    save()
    messagebox.showinfo("Saved", "The data is applied.")
    txt_assigment.delete(0, "end")
    txt_name.delete(0, "end")
    txt_kind.delete(0, "end")
    txt_test.delete(0, "end")
    txt_rest.delete(0, "end") # clearing textboxes
    print(basic_info)
  else:
    messagebox.showinfo("Not complete", "Please check the values entered.\n The grading scale should add up to 100.")

# Sem_1
def add_topic_1():
  if txt_topic.get() != " ":
    topics_sem1.append(txt_topic.get())
    #txt_topic.get() = [] # Creating list for treeview update
    update_listbox_delete()
    update_listbox()
    txt_topic.delete(0, "end")
    print(topics_sem1)
  else:
    messagebox.showinfo("Blank", "Please enter a topic name.")

def insert_treeview():
  selection = lb_topic.curselection()
  if selection:
    tree_main.insert('', 0, text = txt_info_name.get(), values = (txt_info_type.get(), txt_info_per.get() + " %", txt_info_grade.get()))
    txt_info_name.delete(0, "end")
    txt_info_type.delete(0, "end")
    txt_info_per.delete(0, "end")
    txt_info_grade.delete(0, "end")
  else: 
    messagebox.showwarning("Select", "Please select a topic then apply.")

def delete_1():
  topic = lb_topic.get("active")
  topics_sem1.remove(topic)
  update_listbox_delete()
  update_listbox()

# Sem_2
def add_topic_2():
  if txt_topic.get() != " ":
    topics_sem2.append(txt_topic2.get())
    update_listbox_delete()
    update_listbox()
    txt_topic2.delete(0, "end")
    print(topics_sem2)
  else:
    messagebox.showinfo("Blank", "Please enter a topic name.")

def insert_treeview_2():
  pass

def delete_2():
  topic = lb_topic2.get("active")
  topics_sem2.remove(topic)
  update_listbox_delete()
  update_listbox()





# TAB-HOME
# Elements
lbl_name = ttk.Label(home, text = "What is the subject name?", font = ("Courier", 18))
lbl_name.grid(row = 1, column = 0, columnspan = 7)

txt_name = ttk.Entry(home, width = 10, font = ("Courier", 18))
txt_name.grid(row = 2, column = 0, columnspan = 7)

lbl_kind = ttk.Label(home, text = "  What kind of subject is it? \n       AP/Normal/Science", font = ("Courier", 18))
lbl_kind.grid(row = 3, column = 0, columnspan = 7)

txt_kind = ttk.Entry(home, width = 10, font = ("Courier", 18))
txt_kind.grid(row = 4, column = 0, columnspan = 7)

lbl_weigh = ttk.Label(home, text = "Please enter the grading scale. \nAssignment    Test      Rest", font = ("Courier", 18))
lbl_weigh.grid(row = 5, column = 0, columnspan = 7)

txt_assigment = ttk.Entry(home, width = 5, font = ("Courier", 18))
txt_assigment.grid(row = 6, column = 1)

lbl_per1 = ttk.Label(home, text = "%", font = ("Courier", 18))
lbl_per1.grid(row = 6, column = 2)

txt_test = ttk.Entry(home, width = 5, font = ("Courier", 18))
txt_test.grid(row = 6, column = 3)

lbl_per2 = ttk.Label(home, text = "%", font = ("Courier", 18))
lbl_per2.grid(row = 6, column = 4)

txt_rest = ttk.Entry(home, width = 5, font = ("Courier", 18))
txt_rest.grid(row = 6, column = 5)

lbl_per3 = ttk.Label(home, text = "%", font = ("Courier", 18))
lbl_per3.grid(row = 6, column = 6)

btn_apply = ttk.Button(home, text = "Apply", command = apply_subject)
btn_apply.grid(row = 7, column = 7)




# TAB-SEMESTER 1
lblfr = ttk.Labelframe(root)

lblfr_info = ttk.LabelFrame(sem_1, text = "Information") # Information labelframe - top
lblfr_info.grid(row = 0, column = 0, rowspan = 5, columnspan = 20, sticky = 'W')

lbl_info_name = ttk.Label(lblfr_info, text = "Assignment Name: ", font = ("Courier", 15))
lbl_info_name.grid(row = 0, column = 0)

txt_info_name = ttk.Entry(lblfr_info, width = 15, font = ("Courier", 15))
txt_info_name.grid(row = 0, column = 1)

lbl_info_type = ttk.Label(lblfr_info, text = "Type: ", font = ("Courier", 15))
lbl_info_type.grid(row = 1, column = 0)

txt_info_type = ttk.Entry(lblfr_info, width = 15, font = ("Courier", 15))
txt_info_type.grid(row = 1, column = 1)

lbl_info_per = ttk.Label(lblfr_info, text = "%: ", font = ("Courier", 15))
lbl_info_per.grid(row = 2, column = 0)

txt_info_per = ttk.Entry(lblfr_info, width = 15, font = ("Courier", 15))
txt_info_per.grid(row = 2, column = 1)

lbl_info_grade = ttk.Label(lblfr_info, text = "Grade: ", font = ("Courier", 15))
lbl_info_grade.grid(row = 3, column = 0)

txt_info_grade = ttk.Entry(lblfr_info, width = 15, font = ("Courier", 15))
txt_info_grade.grid(row = 3, column = 1)

btn_info_apply = ttk.Button(lblfr_info, text = "Apply", command = insert_treeview)
btn_info_apply.grid(row = 3, column = 2)

txt_topic = ttk.Entry(sem_1, width = 19, font = ("Courier", 14)) # TxtEntry - top left
txt_topic.grid(row = 5, column = 0, columnspan = 2, sticky = 'W')

lb_topic = tkinter.Listbox(sem_1, height = 10) # LB - middle left
lb_topic.grid(row = 6, column = 0, rowspan = 7, columnspan = 2, sticky = 'W')

btn_add = tkinter.Button(sem_1, text = "Add Topic", command = add_topic_1)
btn_add.grid(row = 13, column = 0, sticky = 'W')

btn_delete = tkinter.Button(sem_1, text = "Delete", command = delete_1)
btn_delete.grid(row = 13, column = 1, sticky = 'W')

tree = ttk.Treeview(root)# Treeview - middle

tree_main = ttk.Treeview(sem_1, columns = ("Type", "%", "Grade"))
tree_main.grid(row = 5, column = 3, rowspan = 20, sticky = 'N')

tree_main.heading("Type", text = "Type")
tree_main.heading("%", text = "%")
tree_main.heading("Grade", text = "Grade")

lblfr_result = ttk.LabelFrame(sem_1, text = "Results") # Result labelframe - right
lblfr_result.grid(row = 5, column = 4, rowspan = 4, sticky = 'E')

lbl_total_score = ttk.Label(lblfr_result, text = "Total Score: ", font = ("Courier", 20))
lbl_total_score.grid(row = 0, column = 0)

lbl_total_score_result = ttk.Label(lblfr_result, text = "", font = ("Courier", 20))
lbl_total_score_result.grid(row = 1, column = 0)

lbl_final_grade = ttk.Label(lblfr_result, text = "Final Grade: ", font = ("Courier", 20))
lbl_final_grade.grid(row = 2, column = 0)

lbl_final_grade_result = ttk.Label(lblfr_result, text = "", font = ("Courier", 20))
lbl_final_grade_result.grid(row = 3, column = 0)




# TAB-SEMESTER 2
txt_topic2 = ttk.Entry(sem_2, width = 19, font = ("Courier", 14))
txt_topic2.grid(row = 0, column = 0, columnspan = 2, sticky = 'W')

lb_topic2 = tkinter.Listbox(sem_2, height = 10)
lb_topic2.grid(row = 1, column = 0, rowspan = 7, columnspan = 2, sticky = 'W')

btn_add2 = tkinter.Button(sem_2, text = "Add Topic", command = add_topic_2)
btn_add2.grid(row = 8, column = 0, sticky = 'W')

btn_delete2 = tkinter.Button(sem_2, text = "Delete", command = delete_2)
btn_delete2.grid(row = 8, column = 1, sticky = 'W')

tree_main2 = ttk.Treeview(sem_2, columns = ("Type", "%", "Grade"))
tree_main2.grid(row = 0, column = 3, rowspan = 20, sticky = 'N')

tree_main2.heading("Type", text = "Type")
tree_main2.heading("%", text = "%")
tree_main2.heading("Grade", text = "Grade")


lblfr_result2 = ttk.LabelFrame(sem_2, text = "Results")
lblfr_result2.grid(row = 0, column = 4, rowspan = 4, sticky = 'E')

lbl_total_score2 = ttk.Label(lblfr_result2, text = "Total Score: ", font = ("Courier", 20))
lbl_total_score2.grid(row = 0, column = 0)

lbl_total_score_result2 = ttk.Label(lblfr_result2, text = "", font = ("Courier", 20))
lbl_total_score_result2.grid(row = 1, column = 0)

lbl_final_grade2 = ttk.Label(lblfr_result2, text = "Final Grade: ", font = ("Courier", 20))
lbl_final_grade2.grid(row = 2, column = 0)

lbl_final_grade_result2 = ttk.Label(lblfr_result2, text = "", font = ("Courier", 20))
lbl_final_grade_result2.grid(row = 3, column = 0)
        

tkinter.mainloop()
