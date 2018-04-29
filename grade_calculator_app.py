import tkinter
from tkinter import ttk
from tkinter import *
import pickle
from tkinter import messagebox


root = tkinter.Tk()
root.resizable(width = False, height = False) # Keeping the window size constant

btn1 = StringVar()
btn2 = StringVar()

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
assignment1 = []
assignment2 = []
test1 = []
test2 = []
rest1 = []
rest2 = []
final_score = 0
final_score2 = 0
overall = 0



# Functions for buttons
# Home
def save():
  pickle.dump(basic_info, open("basic_info.dat", "wb")) # saving the data
  pickle.dump(topics_sem1, open("topics_sem1.dat", "wb"))
  pickle.dump(topics_sem2, open("topics_sem2.dat", "wb"))
  pickle.dump(assignment1, open("assignment1.dat", "wb"))
  pickle.dump(assignment2, open("assignment2.dat", "wb"))
  pickle.dump(test1, open("test1.dat", "wb"))
  pickle.dump(test2, open("test2.dat", "wb"))
  pickle.dump(rest1, open("rest1.dat", "wb"))
  pickle.dump(rest2, open("rest2.dat", "wb"))

def apply_subject():
  if txt_name.get() != " " and txt_kind.get() != " "  and txt_assigment.get() != " " and txt_test.get() != " " and txt_rest.get() != " " and (int(txt_assigment.get()) + int(txt_test.get()) + int(txt_rest.get()) == 100):
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
def apply1():
  #global values
  global final_score
  if txt_info_topic.get() != "" and txt_info_per.get() != "" and txt_info_grade.get() != "":
    topics_sem1.append(txt_info_topic.get())
    if btn1.get() == "Assignment":
      assignment1.append(int(txt_info_per.get()))
    elif btn1.get() == "Test":
      test1.append(int(txt_info_per.get()))
    elif btn1.get() == "Rest":
      rest1.append(int(txt_info_per.get()))
    tree_main.insert('', "end", text = txt_info_name.get(), values = (btn1.get(), txt_info_per.get() + " %", txt_info_grade.get(), txt_info_topic.get()))
    txt_info_topic.delete(0, "end")
    txt_info_name.delete(0, "end")
    txt_info_per.delete(0, "end")
    txt_info_grade.delete(0, "end")
    total_score_a = 0
    total_score_t = 0
    total_score_r = 0
    # final score calculation
    for score_a in assignment1:
      total_score_a += score_a
      final_score_a = total_score_a/len(assignment1)
    for score_t in test1:
      total_score_t += score_t
      final_score_t = total_score_t/len(test1)
    for score_r in rest1:
      total_score_r += score_r
      final_score_r = total_score_r/len(rest1)
    
    # Final Grade
    choice = list(basic_info.keys())
    list_a = basic_info[choice[0]]
    values = list_a[0]
    per_assignment1 = int(list_a[1])/100
    per_test1 = int(list_a[2])/100
    per_rest1 = int(list_a[3])/100
    if not assignment1: # if assignment1 is empty
      final_score_a = 100
    if not test1:
      final_score_t = 100
    if not rest1:
      final_score_r = 100 # set the initial score as 100 if nothing is entered for that type
    final_score = (final_score_a * per_assignment1) + (final_score_t * per_test1) + (final_score_r * per_rest1)
    lbl_total_score_result["text"] = final_score
    if values.upper() == "AP":
      if final_score >= 95:
        lbl_final_grade_result["text"] = "A+"
      elif final_score < 95 and final_score >= 90:
        lbl_final_grade_result["text"] = "A"
      elif final_score < 90 and final_score >= 85:
        lbl_final_grade_result["text"] = "A-"
      elif final_score < 85 and final_score >= 80:
        lbl_final_grade_result["text"] = "B+"
      elif final_score < 80 and final_score >= 70:
        lbl_final_grade_result["text"] = "B"
      elif final_score < 70 and final_score >= 65:
        lbl_final_grade_result["text"] = "B-"
      elif final_score < 65 and final_score >= 60:
        lbl_final_grade_result["text"] = "C+"
      elif final_score < 60 and final_score >= 50:
        lbl_final_grade_result["text"] = "C"
      elif final_score < 50 and final_score >= 45:
        lbl_final_grade_result["text"] = "C-"
      elif final_score < 45 and final_score >= 42:
        lbl_final_grade_result["text"] = "D+"
      elif final_score < 42 and final_score >= 38:
        lbl_final_grade_result["text"] = "D"
      elif final_score < 38 and final_score >= 35:
        lbl_final_grade_result["text"] = "D-"
      else:
        lbl_final_grade_result["text"] = "F"
    elif values.upper() == "NORMAL":
      if final_score >= 97:
        lbl_final_grade_result["text"] = "A+"
      elif final_score < 97 and final_score >= 93:
        lbl_final_grade_result["text"] = "A"
      elif final_score < 93 and final_score >= 90:
        lbl_final_grade_result["text"] = "A-"
      elif final_score < 90 and final_score >= 87:
        lbl_final_grade_result["text"] = "B+"
      elif final_score < 87 and final_score >= 83:
        lbl_final_grade_result["text"] = "B"
      elif final_score < 83 and final_score >= 80:
        lbl_final_grade_result["text"] = "B-"
      elif final_score < 80 and final_score >= 77:
        lbl_final_grade_result["text"] = "C+"
      elif final_score < 77 and final_score >= 73:
        lbl_final_grade_result["text"] = "C"
      elif final_score < 73 and final_score >= 70:
        lbl_final_grade_result["text"] = "C-"
      elif final_score < 70 and final_score >= 67:
        lbl_final_grade_result["text"] = "D+"
      elif final_score < 67 and final_score >= 63:
        lbl_final_grade_result["text"] = "D"
      elif final_score < 63 and final_score >= 60:
        lbl_final_grade_result["text"] = "D-"
      else:
        lbl_final_grade_result["text"] = "F"
    elif values.upper() == "SCIENCE":
      if final_score >= 95:
        lbl_final_grade_result["text"] = "A+"
      elif final_score < 95 and final_score >= 90:
        lbl_final_grade_result["text"] = "A"
      elif final_score < 90 and final_score >= 85:
        lbl_final_grade_result["text"] = "A-"
      elif final_score < 85 and final_score >= 80:
        lbl_final_grade_result["text"] = "B+"
      elif final_score < 80 and final_score >= 75:
        lbl_final_grade_result["text"] = "B"
      elif final_score < 75 and final_score >= 70:
        lbl_final_grade_result["text"] = "B-"
      elif final_score < 70 and final_score >= 65:
        lbl_final_grade_result["text"] = "C+"
      elif final_score < 65 and final_score >= 60:
        lbl_final_grade_result["text"] = "C"
      elif final_score < 60 and final_score >= 55:
        lbl_final_grade_result["text"] = "C-"
      elif final_score < 55 and final_score >= 50:
        lbl_final_grade_result["text"] = "D+"
      elif final_score < 50 and final_score >= 45:
        lbl_final_grade_result["text"] = "D"
      elif final_score < 45 and final_score >= 40:
        lbl_final_grade_result["text"] = "D-"
      else:
        lbl_final_grade_result["text"] = "F"
    save()
  else:
    messagebox.showinfo("Blank", "Please put all the data in.")
#def delete_1():
 # tree_main.selection_remove(items)


# Sem_2
def apply2():
  #global values
  global final_score2
  if txt_info_topic2.get() != "" and txt_info_per2.get() != "" and txt_info_grade2.get() != "":
    topics_sem2.append(txt_info_topic2.get())
    if btn2.get() == "Assignment":
      assignment2.append(int(txt_info_per2.get()))
    elif btn2.get() == "Test":
      test2.append(int(txt_info_per2.get()))
    elif btn2.get() == "Rest":
      rest2.append(int(txt_info_per2.get()))
    tree_main2.insert('', "end", text = txt_info_name2.get(), values = (btn2.get(), txt_info_per2.get() + " %", txt_info_grade2.get()))
    txt_info_topic2.delete(0, "end")
    txt_info_name2.delete(0, "end")
    txt_info_per2.delete(0, "end")
    txt_info_grade2.delete(0, "end")
    total_score_a2 = 0
    total_score_t2 = 0
    total_score_r2 = 0 # initial setting to 0 (for the sepecified final score calculation)
    # final score calculation
    for score_a2 in assignment2:
      total_score_a2 += score_a2
      final_score_a2 = total_score_a2/len(assignment2)
    for score_t2 in test2:
      total_score_t2 += score_t2
      final_score_t2 = total_score_t2/len(test2)
    for score_r2 in rest2:
      total_score_r2 += score_r2
      final_score_r2 = total_score_r2/len(rest2)
    # Final Grade
    choice = list(basic_info.keys())
    list_a = basic_info[choice[0]]
    values = list_a[0]
    per_assignment2 = int(list_a[1])/100
    per_test2 = int(list_a[2])/100
    per_rest2 = int(list_a[3])/100
    if not assignment2: # if assignment1 is empty
      final_score_a2 = 100
    if not test2:
      final_score_t2 = 100
    if not rest2:
      final_score_r2 = 100 # set the initial score as 100 if nothing is entered for that type (for the final score calcution)
    final_score2 = (final_score_a2 * per_assignment2) + (final_score_t2 * per_test2) + (final_score_r2 * per_rest2)
    lbl_total_score_result2["text"] = final_score2
    if values.upper() == "AP":
      if final_score2 >= 95:
        lbl_final_grade_result2["text"] = "A+"
      elif final_score2 < 95 and final_score2 >= 90:
        lbl_final_grade_result2["text"] = "A"
      elif final_score2 < 90 and final_score2 >= 85:
        lbl_final_grade_result2["text"] = "A-"
      elif final_score2 < 85 and final_score2 >= 80:
        lbl_final_grade_result2["text"] = "B+"
      elif final_score2 < 80 and final_score2 >= 70:
        lbl_final_grade_result2["text"] = "B"
      elif final_score2 < 70 and final_score2 >= 65:
        lbl_final_grade_result2["text"] = "B-"
      elif final_score2 < 65 and final_score2 >= 60:
        lbl_final_grade_result2["text"] = "C+"
      elif final_score2 < 60 and final_score2 >= 50:
        lbl_final_grade_result2["text"] = "C"
      elif final_score2 < 50 and final_score2 >= 45:
        lbl_final_grade_result2["text"] = "C-"
      elif final_score2 < 45 and final_score2 >= 42:
        lbl_final_grade_result2["text"] = "D+"
      elif final_score2 < 42 and final_score2 >= 38:
        lbl_final_grade_result2["text"] = "D"
      elif final_score2 < 38 and final_score2 >= 35:
        lbl_final_grade_result2["text"] = "D-"
      else:
        lbl_final_grade_result2["text"] = "F"
    elif values.upper() == "NORMAL":
      if final_score2 >= 97:
        lbl_final_grade_result2["text"] = "A+"
      elif final_score2 < 97 and final_score2 >= 93:
        lbl_final_grade_result2["text"] = "A"
      elif final_score2 < 93 and final_score2 >= 90:
        lbl_final_grade_result2["text"] = "A-"
      elif final_score2 < 90 and final_score2 >= 87:
        lbl_final_grade_result2["text"] = "B+"
      elif final_score2 < 87 and final_score2 >= 83:
        lbl_final_grade_result2["text"] = "B"
      elif final_score2 < 83 and final_score2 >= 80:
        lbl_final_grade_result2["text"] = "B-"
      elif final_score2 < 80 and final_score2 >= 77:
        lbl_final_grade_result2["text"] = "C+"
      elif final_score2 < 77 and final_score2 >= 73:
        lbl_final_grade_result2["text"] = "C"
      elif final_score2 < 73 and final_score2 >= 70:
        lbl_final_grade_result2["text"] = "C-"
      elif final_score2 < 70 and final_score2 >= 67:
        lbl_final_grade_result2["text"] = "D+"
      elif final_score2 < 67 and final_score2 >= 63:
        lbl_final_grade_result2["text"] = "D"
      elif final_score2 < 63 and final_score2 >= 60:
        lbl_final_grade_result2["text"] = "D-"
      else:
        lbl_final_grade_result2["text"] = "F"
    elif values.upper() == "SCIENCE":
      if final_score2 >= 95:
        lbl_final_grade_result2["text"] = "A+"
      elif final_score2 < 95 and final_score2 >= 90:
        lbl_final_grade_result2["text"] = "A"
      elif final_score2 < 90 and final_score2 >= 85:
        lbl_final_grade_result2["text"] = "A-"
      elif final_score2 < 85 and final_score2 >= 80:
        lbl_final_grade_result2["text"] = "B+"
      elif final_score2 < 80 and final_score2 >= 75:
        lbl_final_grade_result2["text"] = "B"
      elif final_score2 < 75 and final_score2 >= 70:
        lbl_final_grade_result2["text"] = "B-"
      elif final_score2 < 70 and final_score2 >= 65:
        lbl_final_grade_result2["text"] = "C+"
      elif final_score2 < 65 and final_score2 >= 60:
        lbl_final_grade_result2["text"] = "C"
      elif final_score2 < 60 and final_score2 >= 55:
        lbl_final_grade_result2["text"] = "C-"
      elif final_score2 < 55 and final_score2 >= 50:
        lbl_final_grade_result2["text"] = "D+"
      elif final_score2 < 50 and final_score2 >= 45:
        lbl_final_grade_result2["text"] = "D"
      elif final_score2 < 45 and final_score2 >= 40:
        lbl_final_grade_result2["text"] = "D-"
      else:
        lbl_final_grade_result2["text"] = "F"
    save()
  else: 
    messagebox.showwarning("Blank", "Please put all the data in.")

#def delete_2():
 # tree_main2.selection_remove()


# Exam
def freedom():
  global final_score
  global final_score2
  global overall
  choice = list(basic_info.keys())
  list_a = basic_info[choice[0]]
  values = list_a[0]
  if txt_exam_score.get() != "":
    if values.upper() == "SCIENCE":
      overall = (final_score * 0.8) + (int(txt_exam_score.get()) * 0.2)
      if overall >= 95:
        lbl_final_grade_result2["text"] = "A+"
      elif overall < 95 and overall >= 90:
        lbl_final_grade_result2["text"] = "A"
      elif overall < 90 and overall >= 85:
        lbl_final_grade_result2["text"] = "A-"
      elif overall < 85 and overall >= 80:
        lbl_final_grade_result2["text"] = "B+"
      elif overall < 80 and overall >= 75:
        lbl_final_grade_result2["text"] = "B"
      elif overall < 75 and overall >= 70:
        lbl_final_grade_result2["text"] = "B-"
      elif overall < 70 and overall >= 65:
        lbl_final_grade_result2["text"] = "C+"
      elif overall < 65 and overall >= 60:
        lbl_final_grade_result2["text"] = "C"
      elif overall < 60 and overall >= 55:
        lbl_final_grade_result2["text"] = "C-"
      elif overall < 55 and overall >= 50:
        lbl_final_grade_result2["text"] = "D+"
      elif overall < 50 and overall >= 45:
        lbl_final_grade_result2["text"] = "D"
      elif overall < 45 and overall >= 40:
        lbl_final_grade_result2["text"] = "D-"
      else:
        lbl_final_grade_result2["text"] = "F"
    elif values.upper() == "NORMAL":
      overall = (final_score * 0.4) + (final_score2 * 0.4) + (int(txt_exam_score.get()) * 0.2)
      if overall >= 97:
        lbl_overall_grade_result["text"] = "A+"
      elif overall < 97 and overall >= 93:
        lbl_overall_grade_result["text"] = "A"
      elif overall < 93 and overall >= 90:
        lbl_overall_grade_result["text"] = "A-"
      elif overall < 90 and overall >= 87:
        lbl_overall_grade_result["text"] = "B+"
      elif overall < 87 and overall >= 83:
        lbl_overall_grade_result["text"] = "B"
      elif overall < 83 and overall >= 80:
        lbl_overall_grade_result["text"] = "B-"
      elif overall < 80 and overall >= 77:
        lbl_overall_grade_result["text"] = "C+"
      elif overall < 77 and overall >= 73:
        lbl_overall_grade_result["text"] = "C"
      elif overall < 73 and overall >= 70:
        lbl_overall_grade_result["text"] = "C-"
      elif overall < 70 and overall >= 67:
        lbl_overall_grade_result["text"] = "D+"
      elif overall < 67 and overall >= 63:
        lbl_overall_grade_result["text"] = "D"
      elif overall < 63 and overall >= 60:
        lbl_overall_grade_result["text"] = "D-"
      else:
        lbl_overall_grade_result["text"] = "F"
  else:
    if values.upper() == "AP":
      overall = (final_score * 0.5) + (final_score2 * 0.5)
      lbl_overall_score_result["text"] = overall
      if overall >= 95:
        lbl_overall_grade_result["text"] = "A+"
      elif overall < 95 and overall >= 90:
        lbl_overall_grade_result["text"] = "A"
      elif overall < 90 and overall >= 85:
        lbl_overall_grade_result["text"] = "A-"
      elif overall < 85 and overall >= 80:
        lbl_overall_grade_result["text"] = "B+"
      elif overall < 80 and overall >= 70:
        lbl_overall_grade_result["text"] = "B"
      elif overall < 70 and overall >= 65:
        lbl_overall_grade_result["text"] = "B-"
      elif overall < 65 and overall >= 60:
        lbl_overall_grade_result["text"] = "C+"
      elif overall < 60 and overall >= 50:
        lbl_overall_grade_result["text"] = "C"
      elif overall < 50 and overall >= 45:
        lbl_overall_grade_result["text"] = "C-"
      elif overall < 45 and overall >= 42:
        lbl_overall_grade_result["text"] = "D+"
      elif overall < 42 and overall >= 38:
        lbl_overall_grade_result["text"] = "D"
      elif overall < 38 and overall >= 35:
        lbl_overall_grade_result["text"] = "D-"
      else:
        lbl_overall_grade_result["text"] = "F"




# TAB-HOME
# Elements
lbl_name = ttk.Label(home, text = "What is the subject name?", font = ("Courier", 18))
lbl_name.grid(row = 1, column = 0, columnspan = 7)

txt_name = ttk.Entry(home, width = 10, font = ("Courier", 18))
txt_name.grid(row = 2, column = 0, columnspan = 7)

lbl_kind = ttk.Label(home, text = "  What kind of subject is it?(Pre-AP is considered as an AP subject) \n                            AP/Normal/Science", font = ("Courier", 18))
lbl_kind.grid(row = 3, column = 0, columnspan = 7)

txt_kind = ttk.Entry(home, width = 10, font = ("Courier", 18))
txt_kind.grid(row = 4, column = 0, columnspan = 7)

lbl_weigh = ttk.Label(home, text = "        Please enter the grading scale. \nAssignment               Test            Rest", font = ("Courier", 18))
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

btn_apply_sub = ttk.Button(home, text = "Apply", command = apply_subject)
btn_apply_sub.grid(row = 7, column = 7)



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

rb_info_type_a = ttk.Radiobutton(lblfr_info, text = "Assignment", value = "Assignment", variable = btn1)
rb_info_type_a.grid(row = 1, column = 1)

rb_info_type_t = ttk.Radiobutton(lblfr_info, text = "Test", value = "Test", variable = btn1)
rb_info_type_t.grid(row = 1, column = 2)

rb_info_type_r = ttk.Radiobutton(lblfr_info, text = "Rest", value = "Rest", variable = btn1)
rb_info_type_r.grid(row = 1, column = 3)

lbl_info_per = ttk.Label(lblfr_info, text = "%: ", font = ("Courier", 15))
lbl_info_per.grid(row = 2, column = 0)

txt_info_per = ttk.Entry(lblfr_info, width = 15, font = ("Courier", 15))
txt_info_per.grid(row = 2, column = 1)

lbl_info_grade = ttk.Label(lblfr_info, text = "Grade: ", font = ("Courier", 15))
lbl_info_grade.grid(row = 3, column = 0)

txt_info_grade = ttk.Entry(lblfr_info, width = 15, font = ("Courier", 15))
txt_info_grade.grid(row = 3, column = 1)

lbl_info_topic = ttk.Label(lblfr_info, text = "Topic: ", font = ("Courier", 15))
lbl_info_topic.grid(row = 4, column = 0)

txt_info_topic = ttk.Entry(lblfr_info, width = 15, font = ("Courier", 15))
txt_info_topic.grid(row = 4, column = 1)

btn_info_apply1 = ttk.Button(lblfr_info, text = "Apply", command = apply1)
btn_info_apply1.grid(row = 4, column = 2)

#lb_topic = tkinter.Listbox(sem_1, height = 10) # LB - middle left
#lb_topic.grid(row = 6, column = 0, rowspan = 7, columnspan = 2, sticky = 'W')

#btn_add = tkinter.Button(sem_1, text = "Add Topic", command = add_topic_1)
#btn_add.grid(row = 13, column = 0, sticky = 'W')

#btn_delete = tkinter.Button(sem_1, text = "Delete", command = delete_1)
#btn_delete.grid(row = 26, column = 3, sticky = 'E')

tree = ttk.Treeview(root)# Treeview - middle

tree_main = ttk.Treeview(sem_1, columns = ("Type", "%", "Grade", "Topic"))
tree_main.grid(row = 5, column = 3, rowspan = 20, sticky = 'N')

tree_main.heading("Type", text = "Type")
tree_main.heading("%", text = "%")
tree_main.heading("Grade", text = "Grade")
tree_main.heading("Topic", text = "Topic")

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
lblfr = ttk.Labelframe(root)

lblfr_info2 = ttk.LabelFrame(sem_2, text = "Information") # Information labelframe - top
lblfr_info2.grid(row = 0, column = 0, rowspan = 5, columnspan = 20, sticky = 'W')

lbl_info_name2 = ttk.Label(lblfr_info2, text = "Assignment Name: ", font = ("Courier", 15))
lbl_info_name2.grid(row = 0, column = 0)

txt_info_name2 = ttk.Entry(lblfr_info2, width = 15, font = ("Courier", 15))
txt_info_name2.grid(row = 0, column = 1)

rb_info_type_a2 = ttk.Radiobutton(lblfr_info2, text = "Assignment", value = "Assignment", variable = btn2)
rb_info_type_a2.grid(row = 1, column = 1)

rb_info_type_t2 = ttk.Radiobutton(lblfr_info2, text = "Test", value = "Test", variable = btn2)
rb_info_type_t2.grid(row = 1, column = 2)

rb_info_type_r2 = ttk.Radiobutton(lblfr_info2, text = "Rest", value = "Rest", variable = btn2)
rb_info_type_r2.grid(row = 1, column = 3)

lbl_info_type2 = ttk.Label(lblfr_info2, text = "Type: ", font = ("Courier", 15))
lbl_info_type2.grid(row = 1, column = 0)

lbl_info_per2 = ttk.Label(lblfr_info2, text = "%: ", font = ("Courier", 15))
lbl_info_per2.grid(row = 2, column = 0)

txt_info_per2 = ttk.Entry(lblfr_info2, width = 15, font = ("Courier", 15))
txt_info_per2.grid(row = 2, column = 1)

lbl_info_grade2 = ttk.Label(lblfr_info2, text = "Grade: ", font = ("Courier", 15))
lbl_info_grade2.grid(row = 3, column = 0)

txt_info_grade2 = ttk.Entry(lblfr_info2, width = 15, font = ("Courier", 15))
txt_info_grade2.grid(row = 3, column = 1)

lbl_info_topic2 = ttk.Label(lblfr_info2, text = "Topic: ", font = ("Courier", 15))
lbl_info_topic2.grid(row = 4, column = 0)

txt_info_topic2 = ttk.Entry(lblfr_info2, width = 15, font = ("Courier", 15))
txt_info_topic2.grid(row = 4, column = 1)

btn_info_apply2 = ttk.Button(lblfr_info2, text = "Apply", command = apply2)
btn_info_apply2.grid(row = 4, column = 2)

#lb_topic2 = tkinter.Listbox(sem_2, height = 10)
#lb_topic2.grid(row = 6, column = 0, rowspan = 7, columnspan = 2, sticky = 'W')

#btn_add2 = tkinter.Button(sem_2, text = "Add Topic", command = add_topic_2)
#btn_add2.grid(row = 13, column = 0, sticky = 'W')

#btn_delete2 = tkinter.Button(sem_2, text = "Delete", command = delete_2)
#btn_delete2.grid(row = 26, column = 3, sticky = 'E')

tree_main2 = ttk.Treeview(sem_2, columns = ("Type", "%", "Grade", "Topic"))
tree_main2.grid(row = 5, column = 3, rowspan = 20, sticky = 'N')

tree_main2.heading("Type", text = "Type")
tree_main2.heading("%", text = "%")
tree_main2.heading("Grade", text = "Grade")
tree_main2.heading("Topic", text = "Topic")


lblfr_result2 = ttk.LabelFrame(sem_2, text = "Results")
lblfr_result2.grid(row = 5, column = 4, rowspan = 4, sticky = 'E')

lbl_total_score2 = ttk.Label(lblfr_result2, text = "Total Score: ", font = ("Courier", 20))
lbl_total_score2.grid(row = 0, column = 0)

lbl_total_score_result2 = ttk.Label(lblfr_result2, text = "", font = ("Courier", 20))
lbl_total_score_result2.grid(row = 1, column = 0)

lbl_final_grade2 = ttk.Label(lblfr_result2, text = "Final Grade: ", font = ("Courier", 20))
lbl_final_grade2.grid(row = 2, column = 0)

lbl_final_grade_result2 = ttk.Label(lblfr_result2, text = "", font = ("Courier", 20))
lbl_final_grade_result2.grid(row = 3, column = 0)



# Exam
lbl_exam_score = ttk.Label(exam, text = "What is your score for the Final Exam?", font = ("Courier", 20))
lbl_exam_score.grid()

lbl_exam_notification = ttk.Label(exam, text = "Just click the button if there is no exam for the subject.", font = ("Courier", 20))
lbl_exam_notification.grid()

txt_exam_score = ttk.Entry(exam, width = 10, font = ("Courier", 20))
txt_exam_score.grid()

btn_freedom = ttk.Button(exam, text = "Freedom!", command = freedom)
btn_freedom.grid()

lbl_overall_score = ttk.Label(exam, text = "Your overall score is:", font = ("Courier", 20))
lbl_overall_score.grid()

lbl_overall_score_result = ttk.Label(exam, text = "", font = ("Courier", 20))
lbl_overall_score_result.grid()

lbl_overall_grade = ttk.Label(exam, text = "Your overall grade is:", font = ("Courier", 20))
lbl_overall_grade.grid()

lbl_overall_grade_result = ttk.Label(exam, text = "", font = ("Courier", 20))
lbl_overall_grade_result.grid()

        

tkinter.mainloop()
