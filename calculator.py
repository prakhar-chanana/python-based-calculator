from tkinter import *
import math

ex = ""
total = "t"
m = []


def allClr():
    global ex
    ex = ""
    eq.set(ex)
    b15['state'] = NORMAL


def num(n):
    global ex
    if ex == "0":
        eq.set(str(n))
    elif ex != "0":
        if ex != total:
            eq.set(ex + str(n))
        else:
            eq.set(str(n))
    ex = eq.get()
    b15['state'] = NORMAL


def clr():
    global ex
    try:
        c = ex
        xx = list(c)
        del xx[-1]
        e = ""
        for i in xx:
            e += i
        ex = e
        eq.set(ex)
    except:
        ex = ""
        eq.set("")


def op(cc):
    global ex
    q = list(ex)
    t = ""
    if (q[-1] == "+") or (q[-1] == "-") or (q[-1] == "*") or (q[-1] == "/"):
        q[-1] = str(cc)
        for i in q:
            t += i
        ex = t
        eq.set(ex)
    else:
        eq.set(eq.get() + str(cc))
        ex = eq.get()


def dot():
    global ex
    q = list(ex)
    t = ""
    a = ['+', '-', '*', '/']
    o = 0
    d = 0
    if len(q) == 0:
        q.append('0.')
        for i in q:
            t += i
        ex = t
        eq.set(ex)
    elif (q[-1] == "+") or (q[-1] == "-") or (q[-1] == "*") or (q[-1] == "/"):
        q.append('0.')
        for i in q:
            t += i
        ex = t
        eq.set(ex)
    elif q[-1] != ".":
        if "." in ex:
            for i in range(len(q)):
                for j in range(len(a)):
                    if ex[i] == ".":
                        d = i
                    if ex[i] == a[j]:
                        o = i
            if o > d:
                ex = ex + "."
                eq.set(ex)
        else:
            ex = ex + "."
            eq.set(ex)
    elif q[-1] == ".":
        q[-1] = "."
        for i in q:
            t += i
        ex = t
        eq.set(ex)
    else:
        ex = ex + "."
        eq.set(ex)


def equal():
    global ex, total, m
    try:
        total = str(eval(ex))
        p = ex + ' = ' + total
        eq.set(total)
        ex = total
        b15['state'] = DISABLED
        m.append(p)


    except:
        eq.set("ERROR")
        ex = ""


def mem():
    global m

    def crtLabel():
        Label(tk, textvariable=j, font=('Courier New', 20)).grid(row=r)

    tk = Toplevel()
    tk.geometry("400x400")
    tk.maxsize(400, 400)
    tk.minsize(400, 400)
    tk.title('Memory')
    r = 0
    for i in m:
        j = StringVar()
        j.set(i)
        crtLabel()
        r += 1
    tk.mainloop()


def brac(n):
    global ex
    ex = ex + str(n)
    eq.set(ex)


def sqr():
    global ex, m
    q = list(ex)
    d = ex.count(".")
    o = ""
    if len(q) == 0:
        eq.set("ERROR")
        ex = ""
    elif d == 0:
        a = int(ex)
        s = a * a
        o = 'Sqr({})'.format(a) + ' = ' + str(s)
        ex = str(s)
        eq.set(ex)
        ex = ""
    elif d != 0:
        a = float(ex)
        s = a * a
        o = 'Sqr({})'.format(a) + ' = ' + str(s)
        ex = str(s)
        eq.set(ex)
        ex = ""
    m.append(o)


def sqRoot():
    global ex
    q = list(ex)
    d = ex.count(".")
    if len(q) == 0:
        eq.set("ERROR")
        ex = ""
    elif d == 0:
        a = int(ex)
        s = math.sqrt(a)
        o = 'Sqrt({})'.format(a) + ' = ' + str(s)
        ex = str(s)
        eq.set(ex)
        ex = ""
    elif d != 0:
        a = float(ex)
        s = math.sqrt(a)
        o = 'Sqrt({})'.format(a) + ' = ' + str(s)
        ex = str(s)
        eq.set(ex)
        ex = ""
    m.append(o)


so = Tk()
so.geometry('400x485+200+200')
so.maxsize(400, 485)
so.minsize(400, 485)
so.title('Calculator')

eq = StringVar()
eq.set("")

Label(so, text="Calculator", font=('Courier New', 20)).grid(row=0, columnspan=4)

Entry(so, textvariable=eq, font=('Courier New', 20), width=20).grid(row=1, columnspan=4, ipadx=40, ipady=20)

# 0 t0 9
b7 = Button(so, text='7', font=('Courier New', 20), height=1, width=5, command=lambda: num(7))
b7.grid(row=5, column=0)

b8 = Button(so, text='8', font=('Courier New', 20), height=1, width=5, command=lambda: num(8))
b8.grid(row=5, column=1)

b9 = Button(so, text='9', font=('Courier New', 20), height=1, width=5, command=lambda: num(9))
b9.grid(row=5, column=2)

b4 = Button(so, text='4', font=('Courier New', 20), height=1, width=5, command=lambda: num(4))
b4.grid(row=6, column=0)

b5 = Button(so, text='5', font=('Courier New', 20), height=1, width=5, command=lambda: num(5))
b5.grid(row=6, column=1)

b6 = Button(so, text='6', font=('Courier New', 20), height=1, width=5, command=lambda: num(6))
b6.grid(row=6, column=2)

b1 = Button(so, text='1', font=('Courier New', 20), height=1, width=5, command=lambda: num(1))
b1.grid(row=7, column=0)

b2 = Button(so, text='2', font=('Courier New', 20), height=1, width=5, command=lambda: num(2))
b2.grid(row=7, column=1)

b3 = Button(so, text='3', font=('Courier New', 20), height=1, width=5, command=lambda: num(3))
b3.grid(row=7, column=2)

b0 = Button(so, text='0', font=('Courier New', 20), height=1, width=5, command=lambda: num(0))
b0.grid(row=8, column=1)

# Plus
b10 = Button(so, text='+', font=('Courier New', 20), height=1, width=5, command=lambda: op('+'))
b10.grid(row=7, column=3)

# Minus
b11 = Button(so, text='-', font=('Courier New', 20), height=1, width=5, command=lambda: op('-'))
b11.grid(row=6, column=3)

# Multiply
b12 = Button(so, text='x', font=('Courier New', 20), height=1, width=5, command=lambda: op('*'))
b12.grid(row=5, column=3)

# Divide
b13 = Button(so, text='/', font=('Courier New', 20), height=1, width=5, command=lambda: op('/'))  # u"\u00F7"
b13.grid(row=4, column=3)

# Dot
b14 = Button(so, text='.', font=('Courier New', 20), height=1, width=5, command=dot)
b14.grid(row=8, column=2)

# Equal
b15 = Button(so, text='=', font=('Courier New', 20), height=1, width=5, command=equal)
b15.grid(row=8, column=3)

# Left Parenthesis
b16 = Button(so, text='(', font=('Courier New', 20), height=1, width=5, command=lambda: brac("("))
b16.grid(row=3, column=0)

# Right Parenthesis
b17 = Button(so, text=')', font=('Courier New', 20), height=1, width=5, command=lambda: brac(")"))
b17.grid(row=3, column=1)

# Square
b18 = Button(so, text="Sqr", font=('Courier New', 20), height=1, width=5, command=sqr)
b18.grid(row=4, column=1)

# Square Root
b19 = Button(so, text="Sqrt", font=('Courier New', 20), height=1, width=5, command=sqRoot)
b19.grid(row=4, column=2)

# Cube
# b22 = Button(so, text="Cube", font=('Courier New', 20), height=1, width=11, command=cube)
# b22.grid(row=8, columnspan=2)

# Cube Root
# b23 = Button(so, text="Cbrt", font=('Courier New', 20), height=1, width=11, command=cbRoot)
# b23.grid(row=8, columnspan=2, column=2)

# All Clear
b20 = Button(so, text='AC', font=('Courier New', 20), height=1, width=5, command=allClr)
b20.grid(row=3, column=2)

# Backspace
b21 = Button(so, text=u"\u232B", font=('Courier New', 20), height=1, width=5, command=clr)  # u"\u232B"
b21.grid(row=3, column=3)

# Memory
b24 = Button(so, text='M', font=('Courier New', 20), height=1, width=5, command=mem)
b24.grid(row=4, column=0)

so.mainloop()
