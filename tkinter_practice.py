from tkinter import *
from tkinter import ttk


root = Tk()
bill_entry_frame = ttk.Frame(root, padding=10)
bill_entry_frame.grid()
ttk.Entry(bill_entry_frame).grid(column=0, row=0)
ttk.Button(bill_entry_frame)