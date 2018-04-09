import tkinter
from tkinter import ttk

root = tkinter.Tk()

root.title("Grade tracker")
# tabs
notebook = ttk.Notebook(root)

class Window(object):
    def __init__(self):
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

        # Elements
        lbl_name = ttk.Label(home, text = "What is the subject name?", font = ("Courier", 18))
        lbl_name.grid(row = 1)

        txt_name = ttk.Entry(home, width = 10, font = ("Courier", 18))
        txt_name.grid(row = 2)

        lbl_kind = ttk.Label(home, text = "  What kind of subject is it? \n       AP/Normal/Science", font = ("Courier", 18))
        lbl_kind.grid(row = 3)

        txt_kind = ttk.Entry(home, width = 10, font = ("Courier", 18))
        txt_kind.grid(row = 4)

        lbl_weigh = ttk.Label(home, text = "Please enter the grading scale. \n    Assignment    Test    Rest", font = ("Courier", 18))
        lbl_weigh.grid(row = 5)

        txt_assigment = ttk.Entry(home, width = 5, font = ("Courier", 18))
        txt_assigment.grid(row = 6, column = 0)

        lbl_per1 = ttk.Label(home, text = "%", font = ("Courier", 18))
        lbl_per1.grid(row = 6, column = 1)

        txt_test = ttk.Entry(home, width = 5, font = ("Courier", 18))
        txt_test.grid(row = 6, column = 2)

        lbl_per2 = ttk.Label(home, text = "%", font = ("Courier", 18))
        lbl_per2.grid(row = 6, column = 3)

        txt_rest = ttk.Entry(home, width = 5, font = ("Courier", 18))
        txt_rest.grid(row = 6, column = 4)

        lbl_per3 = ttk.Label(home, text = "%", font = ("Courier", 18))
        lbl_per3.grid(row = 6, column = 5)

        btn_apply = ttk.Button(home, text = "Apply", command = exit)
        btn_apply.grid(row = 7)
        
        
#def insert():
  #  home.insert(end, elements())
app = Window()

#elements()


tkinter.mainloop()
tkinter.destroy()