import tkinter
from tkinter import ttk
import pickle
from tkinter import messagebox

root = tkinter.Tk()

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

# Dictionary
data = {}




# TAB-HOME
# Functions for buttons
def apply():
  if txt_name.get() != "" and txt_kind.get() != "" and txt_assigment.get() != "" and txt_test.get() != "" and txt_rest.get() != "":
    key = txt_name.get()
    value = [txt_kind.get(), txt_assigment.get(), txt_test.get(), txt_rest.get()]
    data[key] = value
    pickle.dump(data, open("data.dat", "wb")) # saving the data
    txt_assigment.delete(0, "end")
    txt_name.delete(0, "end")
    txt_kind.delete(0, "end")
    txt_test.delete(0, "end")
    txt_rest.delete(0, "end") # clearing textboxes
    messagebox.showinfo("Saved", "The data is applied.")
    print(data)
  else:
    messagebox.showinfo("Not complete", "Please enter all the values in.")


#class Window(object):
#   def __init__(self, command_a):


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

btn_apply = ttk.Button(home, text = "Apply", command = apply)
btn_apply.grid(row = 7, column = 7)




# TAB-SEMESTER 1
lblfr = ttk.Labelframe(root)

lblfr_result = ttk.LabelFrame(sem_1, text = "Results")
lblfr_result.grid(rowspan = 1, columnspan = 1)

tree = ttk.Treeview(root)

tree_main = ttk.Treeview(sem_1, columns = ("Test name", "Type", "%", "Grade"))
tree_main.grid()

tree_main.heading("Test name", text = "Test name")
tree_main.heading("Type", text = "Type")
tree_main.heading("%", text = "%")
tree_main.heading("Grade", text = "Grade")



        
# Instance
#app = Window(apply)

tkinter.mainloop()
tkinter.destroy()