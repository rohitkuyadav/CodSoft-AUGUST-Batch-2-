"""
Made by: Rohit Kumar Yadav
Date: 08-08-2023
"""
#importing modules
import tkinter as tk
from tkinter import messagebox
from tkinter import *


# Root window 
main = tk.Tk()
main.title('To-Do List')
main.geometry("400x250")
# To-Do List (Listbox widget)
tasks = tk.Listbox(main, height=10, width=50)
tasks.pack()

# Entry box to add new task
entry = tk.Entry(main) 
entry.pack()


def add_task():
    task = entry.get()
    if task != "":
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = tasks.curselection()[0]
        tasks.delete(task_index)
    except:
        messagebox.showwarning("Warning", "No task selected.")

p1 = PhotoImage(file = 'icon1.png')

# Setting icon of master window
main.iconphoto(False, p1)
# Menu bar
menu_bar = tk.Menu(main)


# Buttons
btn_add_task = tk.Button(main, text="Add Task", command=add_task)
btn_add_task.pack()

btn_delete_task = tk.Button(main, text="Delete Task", command=delete_task)
btn_delete_task.pack()

# Display menu bar 
main.config(menu=menu_bar)

main.mainloop()