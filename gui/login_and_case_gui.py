import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auth.auth_manager import AuthManager
from cases.case_manager import CaseManager
import tkinter as tk
from tkinter import simpledialog, messagebox

class LoginWindow:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        self.auth = AuthManager()
        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        tk.Label(self.frame, text='Username:').grid(row=0, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)
        tk.Label(self.frame, text='Password:').grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show='*')
        self.password_entry.grid(row=1, column=1)
        tk.Button(self.frame, text='Login', command=self.login).grid(row=2, column=0)
        tk.Button(self.frame, text='Register', command=self.register).grid(row=2, column=1)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth.verify_user(username, password):
            self.frame.destroy()
            self.on_success(username)
        else:
            messagebox.showerror('Login Failed', 'Invalid credentials')

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth.register_user(username, password):
            messagebox.showinfo('Registration', 'User registered successfully')
        else:
            messagebox.showerror('Registration Failed', 'Username already exists')

class CaseSelectionWindow:
    def __init__(self, root, username, on_case_selected):
        self.root = root
        self.username = username
        self.on_case_selected = on_case_selected
        self.case_manager = CaseManager()
        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        tk.Label(self.frame, text=f'Welcome, {self.username}').pack()
        tk.Button(self.frame, text='Create New Case', command=self.create_case).pack()
        tk.Label(self.frame, text='Select Case:').pack()
        self.case_listbox = tk.Listbox(self.frame)
        self.case_listbox.pack()
        self.refresh_cases()
        tk.Button(self.frame, text='Open Case', command=self.open_case).pack()

    def refresh_cases(self):
        self.case_listbox.delete(0, tk.END)
        cases = self.case_manager.get_cases()
        for case in cases:
            self.case_listbox.insert(tk.END, f"{case[0]}: {case[1]} (Analyst: {case[2]})")

    def create_case(self):
        case_name = simpledialog.askstring('New Case', 'Enter case name:')
        if case_name:
            self.case_manager.create_case(case_name, self.username)
            self.refresh_cases()

    def open_case(self):
        selection = self.case_listbox.curselection()
        if selection:
            case_info = self.case_listbox.get(selection[0])
            self.frame.destroy()
            self.on_case_selected(case_info)
        else:
            messagebox.showerror('No Selection', 'Please select a case to open')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Forensic Recovery Tool - Login')
    def on_login(username):
        root.title('Case Selection')
        CaseSelectionWindow(root, username, lambda case: messagebox.showinfo('Case Selected', f'Active case: {case}'))
    LoginWindow(root, on_login)
    root.mainloop()
