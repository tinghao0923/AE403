# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:42:06 2024

@author: baoch
"""

import tkinter as tk

def click():
    tk.messagebox.showinfo(title='提示',message='click')
window = tk.Tk()
window.title("my window")
window.geometry('300x300')
label = tk.Label(window,text='text')
label.pack()
entry = tk.Entry(window,width = 20)
entry.pack()
button = tk.Button(window,text='點我',command= click)
button.pack()
window.mainloop()