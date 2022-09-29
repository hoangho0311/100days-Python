import tkinter

window = tkinter.Tk()
window.title("My first Gui")
window.minsize(500, 200)

myLb= tkinter.Label(text="I am label")
myLb.pack()

def text():
    data = input.get()
    myLb.config(text=data)

button = tkinter.Button(text="alo", command=text)
button.pack()

input = tkinter.Entry(width=15)
input.pack()

text= tkinter.Text(width=50, height=5)
text.pack()
text.focus()

window.mainloop()

# def add(*n):
#     for x in n:
#         print(x)
#
# add(1,12,3)

#
# def calculate(**kw):
#     print(kw)
#
# calculate(name = 1, text =2)