from tkinter import *


window = Tk(className=' BankNifty ')


def monday():
    entry = float(e1.get()) * 1.3
    target = entry * 1.14
    stop_loss = entry * 0.85
    v2.delete("1.0", END)
    v2.insert(END,  entry)
    v3.delete("1.0", END)
    v3.insert(END, target)
    v4.delete("1.0", END)
    v4.insert(END, stop_loss)


def tuesday():
    entry = float(e1.get()) * 1.3
    target = entry * 1.15
    stop_loss = entry * 0.85
    v2.delete("1.0", END)
    v2.insert(END,  entry)
    v3.delete("1.0", END)
    v3.insert(END, target)
    v4.delete("1.0", END)
    v4.insert(END, stop_loss)


def wednesday():
    entry = float(e1.get()) * 1.4
    target = entry * 1.2
    stop_loss = entry * 0.8
    v2.delete("1.0", END)
    v2.insert(END,  entry)
    v3.delete("1.0", END)
    v3.insert(END, target)
    v4.delete("1.0", END)
    v4.insert(END, stop_loss)


def thursday():
    entry = float(e1.get()) * 1.5
    target = entry * 1.25
    stop_loss = entry * 0.75
    v2.delete("1.0", END)
    v2.insert(END,  entry)
    v3.delete("1.0", END)
    v3.insert(END, target)
    v4.delete("1.0", END)
    v4.insert(END, stop_loss)


def friday():
    entry = float(e1.get()) * 1.2
    target = entry * 1.1
    stop_loss = entry * 0.9
    v2.delete("1.0", END)
    v2.insert(END,  entry)
    v3.delete("1.0", END)
    v3.insert(END, target)
    v4.delete("1.0", END)
    v4.insert(END, stop_loss)


def close():
    Tk.destroy(window)


B1 = Button(text="Monday", command=monday)
B1.grid(row=0, column=0)

B2 = Button(text="Tuesday", command=tuesday)
B2.grid(row=0, column=1)

b3 = Button(window, text="Wednesday", command=wednesday)
b3.grid(row=0, column=2)

B4 = Button(window, text="Thursday", command=thursday)
B4.grid(row=3, column=0)

B5 = Button(window, text="Friday", command=friday)
B5.grid(row=3, column=1)


L3 = Label(window, text="Entry")
L3.grid(row=1, column=0)
L4 = Label(window, text="Target")
L4.grid(row=1, column=1)
L5 = Label(window, text="StopLoss")
L5.grid(row=1, column=2)
L6 = Label(window, text=">>Enter Current Market Price Here-->>>>>")
L6.grid(row=4, columnspan=2)

B6 = Button(text="Exit", command=close)
B6.grid(row=3, column=2)


e1 = Entry(window)
e1.grid(row=4, column=2)
v2 = Text(window, height=1, width=15)
v2.grid(row=2, column=0)
v3 = Text(window, height=1, width=15)
v3.grid(row=2, column=1)
v4 = Text(window, height=1, width=15)
v4.grid(row=2, column=2)


window.mainloop()
