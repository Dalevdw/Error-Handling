from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Exception")
root.geometry("400x300")
root.configure(background="steelblue")

#first login screen
def check():
    all_logs = {'Dalevdw':'1234', 'Slime': '9999'}
    my_user = username_ent.get()
    password = password_ent.get()
    if (my_user, password) in all_logs.items():
        messagebox.showinfo("INFO", "CORRECT LOGIN")
        root.withdraw()

        import EHtask2NDfile
        EHtask2NDfile.mainloop()


    else:
        messagebox.showinfo("INFO","INCORRECT LOGIN")

        username_lbl.delete(0,END)
        password_lbl.Entry.delete(0, END)



#top label
login_lbl = Label(root, text="Please enter Login details:",)
login_lbl.configure(background="steelblue")
login_lbl.pack()

#Username label & entry
username_lbl= Label(root, text="Username", height=2)
username_lbl.configure(background="steelblue")
username_lbl.pack()
username_ent = Entry(root, borderwidth=4)
username_ent.pack()
#password label & entry
password_lbl = Label(root, text="Password", height=2)
password_lbl.configure(background="steelblue")
password_lbl.pack()
password_ent = Entry(root, borderwidth=4, show="*")
password_ent.pack()

#Button
login_btn = Button(root, text="Login", height=1,width=10, command=check)
login_btn.pack(side=BOTTOM)


root.mainloop()
