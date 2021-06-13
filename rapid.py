from tkinter import *
import random

root = Tk()
root.title('Rapid Roll Number selecter')
root.geometry('220x200')
root.configure(background='black')

item_label = Label(root)
random_no_label = Label(root, bg="black", fg="cyan", font=12)


def random_func():
    section_List = ["A", "B", "C", "D", "E"]
    random_RollNumber = random.randint(1, 50)
    random_Section = random.randint(0, 4)
    random_no_label["text"] = "Roll Number " + \
        str(random_RollNumber) + " From Section " + \
        section_List[random_Section]


button = Button(root, text="Which student should answer?",
                command=random_func, bg="yellow", fg="black")
button.place(relx=0.5, rely=0.4, anchor=CENTER)

random_no_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
