from tkinter import *

root = Tk()
def click(event):
    global scv
    text = event.widget.cget("text")
    if text == "=":
        if scv.get().isdigit():
            v = int(scv.get())
        else:
            try:
                v = eval(s.get())
            except Exception as e:
                v = "Error"
                scv.set("Error")
                s.update()
        scv.set(v)
        s.update()
    elif text == "c":
        scv.set("")
        s.update()
    else:
        scv.set(scv.get() + text)
        s.update()

root.geometry("350x650")
root.minsize(350,650)
root.maxsize(350,650)
root.title("Calculator By - Hackson")
root.wm_iconbitmap("iron-man.png")

scv = StringVar()
scv.set("")
s = Entry(root, textvariable=scv, font="lucida 30 bold")
s.pack(fill=X, padx=10, pady=10, ipadx=20, ipady=10)

f1 = Frame(root, bg="grey")
b = Button(f1, text="9", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="8", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="7", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey")
b = Button(f1, text="6", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="5", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="4", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1= Frame(root, bg="grey")
b = Button(f1, text="3", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="2", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="1", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey")
b = Button(f1, text="-", font="lucida 20 bold", padx=12,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="0", font="lucida 20 bold", padx=12,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="*", font="lucida 20 bold", padx=12,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey")
b = Button(f1, text="/", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="=", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="%", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey")
b = Button(f1, text=".", font="lucida 20 bold", padx=9,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="c", font="lucida 20 bold", padx=10,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="00", font="lucida 20 bold", padx=8,pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

root.mainloop()