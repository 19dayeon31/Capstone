import tkinter
from tkinter import ttk

root = tkinter.Tk()

root.title("Grade tracker")
# tabs
notebook = ttk.Notebook(root)

# Functions
def tabs():
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

    notebook.pack(expand = 1, fill = "both")

tabs()
# Visualization
#lbl_name = tkinter.Label(root, text = "What is the subject name?", font = ("Courier", 23))
#lbl_name.config(height = 5)
#lbl_name.grid(row = 0)

#txt_name = tkinter.Entry(root, width = 10, font = ("Courier", 23))
#txt_name.grid(row = 1)

#btn_continue = tkinter.Button(root, text = "Continue", command = subject_type)
#btn_continue.grid(row = 2)



tkinter.mainloop()
tkinter.destroy()