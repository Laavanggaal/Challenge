from tkinter import *

def factor(n):
   n = int(e.get())
   ans = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           ans.append(d)
           n = n // d
       else:
           d += 1
   if n > 1:
       ans.append(n)
   l['text'] = ans
   
root = Tk()

e = Entry(root, width=20)
b = Button(root, text="Разложить")
l = Label(root, bg='black', fg='white', width=20)

b.bind('<Button-1>', factor)

e.pack()
b.pack()
l.pack()

root.mainloop()
