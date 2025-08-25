from tkinter import messagebox
import importlib

def show_case_prompt():
    response = messagebox.askyesnocancel('Select Case', 'Do you want to create a new case? (Yes)\nOr open an existing case? (No)')
    if response is True:
        create_case = importlib.import_module('create_case')
        create_case.create_case_dialog()
    elif response is False:
        messagebox.showinfo('Case', 'Proceed to open an existing case.')
    else:
        messagebox.showinfo('Case', 'Case selection cancelled.')
