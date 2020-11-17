from tkinter import*
from tkinter import messagebox
window = Tk()
window.title("Exception")
window.geometry("400x300")
window.configure(background="steelblue")


#tatus feedback
def status():

    amount = int(qua_ent.get())

    if amount >= 3000:
        messagebox.showinfo("Congratulations", "You qualify to go to Malaysia")

    elif amount < 3000:
        messagebox.showerror("Info", "Please deposit more funds for this excursion.")


#check qualification btn & entry
qua_ent = Entry(window,borderwidth=4)
qua_ent.pack()
qua_btn = Button(window,text="Check qualification", command=status)
qua_btn.pack()

window.mainloop()
