from tkinter import *
import os


def exit():
    root.destroy()


def shutdown():
    n = "shutdown"
    if n == "shutdown":
        os.system("shutdown -s")


def restart():
    n = "restart"
    if n == "restart":
        os.system("shutdown -r")


def logout():
    n = "restart"
    if n == "restart":
        os.system("shutdown -l")


root = Tk()
root.geometry("500x500")
root.maxsize(500, 500)
root.minsize(500, 500)
root.title("Shut, Res and Log btn!!")

lbl = Label(root, text="Shutdown, Restart and Logout Button.", bd="4", relief="raised", fg="red", bg="yellow", font="comicsansms, 19 bold")
lbl.pack()

lbl1 = Label(root, text="✨✨...Star Code with Arshad...👑👑", bg="aqua", fg="red", font="comicsansms, 15 bold", bd="4", relief="raised")
lbl1.pack(side=BOTTOM)


btn1 = Button(root, text="Shutdown", padx=10, pady=10, bg="yellowgreen", font="arial 9 bold", command=shutdown)
btn2 = Button(root, text="Restart", padx=10, pady=10, bg="cyan", font="arial 9 bold", command=restart)
btn3 = Button(root, text="Logout", padx=10, pady=10, bg="purple", font="arial 9 bold", command=logout)
btn4 = Button(root, text="Exit", padx=10, pady=10, bg="tomato", font="arial 9 bold", command=exit)


btn1.place(x=70, y=200)
btn2.place(x=200, y=130)
btn3.place(x=310, y=200)
btn4.place(x=210, y=290)

root.configure( bg="lightpink")

root.mainloop()