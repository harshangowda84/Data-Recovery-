import tkinter as tk
import customtkinter as ctk
import importlib.util
from main_page import MainPage

# Dynamically import login_and_case_gui
spec = importlib.util.spec_from_file_location("login_and_case_gui", "login_and_case_gui.py")
login_and_case_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(login_and_case_module)
LoginWindow = login_and_case_module.LoginWindow
CaseSelectionWindow = login_and_case_module.CaseSelectionWindow

# NOTE: Run this script from the gui directory:
#   cd d:\Data Recovery\gui
#   python launcher.py

def start_main_app(case_info):
    # Destroy the Tkinter root window
    root.destroy()
    # Start the main forensic app
    win = ctk.CTk()
    MainPage(win)
    win.mainloop()

def on_login(username):
    root.title('Case Selection')
    CaseSelectionWindow(root, username, start_main_app)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Forensic Recovery Tool - Login')
    LoginWindow(root, on_login)
    root.mainloop()
