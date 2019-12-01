from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global f
    root.title("untitled - Notepad")
    f = None
    ta.delete(1.0, END)

def openfile():
    global f
    f = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if f == "":
        f = None
    else:
        root.title(os.path.basename(f) + " - Notepad")
        ta.delete(1.0, END)
        f2 = open(f, "r")
        ta.insert(1.0, f2.read())
        f2.close()


def savefile():
    global  f
    if f == None:
        f = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

        if f == "":
            f = None
        else:
            f4 = open(f,"w")
            f4.write(ta.get(1.0, END))
            f4.close()
            root.title(os.path.basename(f) + " - Notepad")
    else:
        f4 = open(f, "w")
        f4.write(ta.get(1.0, END))
        f4.close()


def cut():
    ta.event_generate(("<<cut>>"))

def copy():
    ta.event_generate(("<<copy>>"))

def past():
    ta.event_generate(("<<past>>"))

def about():
    showinfo("About", "This is a notepad Created By Hackson Company")

if __name__ == '__main__':

    root = Tk()
    root.geometry("644x588")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("iron-man.png")

    ta = Text(root, font="lucida 13")
    f = None

    m = Menu(root)
    fm = Menu(m, tearoff=0)
    fm.add_command(label="New", command=newfile)
    fm.add_command(label="Open", command=openfile)
    fm.add_command(label="Save", command=savefile)
    fm.add_separator()
    fm.add_command(label="Exit", command=quit)
    m.add_cascade(label="File", menu=fm)


    em = Menu(m, tearoff=0)
    em.add_command(label="Cut", command=cut)
    em.add_command(label="Copy", command=copy)
    em.add_command(label="past", command=past)

    m.add_cascade(label="Edit", menu=em)

    hm = Menu(m, tearoff=0)
    hm.add_command(label="About Notepade", command=about)
    m.add_cascade(label="Help", menu=hm)

    root.config(menu=m)
    ta.pack(fill = BOTH, expand=True)

    sb = Scrollbar(ta)
    sb.pack(side=RIGHT, fill=Y)
    sb.config(command=ta.yview)
    ta.config(yscrollcommand=sb.set)


    root.mainloop()