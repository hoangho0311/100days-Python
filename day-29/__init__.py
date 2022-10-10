from tkinter import *
from  tkinter import  messagebox

# Save PASS
def save():
    website = websiteIP.get()
    username= usernameIP.get()
    passw = passwordIP.get()

    if len(website)==0 or len(passw)==0:
        messagebox.showinfo(title="ERROR", message="ERROR")
        return


    messagebox.showinfo(title="SUCCESS", message="OK")

    with open("data.txt", "a") as data:
        data.write(f"{website} | {username} | {passw}\n")
        websiteIP.delete(0,END)
        passwordIP.delete(0, END)

# UI
window = Tk()
window.title("Password")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomatoImg)
canvas.grid(column=2, row=0)

website = Label(text="Website:")
websiteIP = Entry(width=50)
websiteIP.focus()
website.grid(column=1, row=1)
websiteIP.grid(column=2, row=1, columnspan=2)

username = Label(text="Email/Username:")
usernameIP = Entry(width=50)
usernameIP.insert(0, "vku@gmail.com")
username.grid(column=1, row=2)
usernameIP.grid(column=2, row=2, columnspan=2)

password = Label(text="Password:")
passwordIP = Entry(width=35)
password.grid(column=1, row=3)
passwordIP.grid(column=2, row=3)

generatePass = Button(text="Genarate Pass")
generatePass.grid(column=3, row=3)

addBtn = Button(text="add", width=40, command=save)
addBtn.grid(column=2, row=4, columnspan=2)

window.mainloop()