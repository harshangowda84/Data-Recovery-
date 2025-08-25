import customtkinter as ctk
from tkinter import messagebox
import importlib

def show_case_prompt():
    win = ctk.CTk()
    win.title("Case Selection")
    win.geometry("600x340")
    win.resizable(False, False)

    # Header
    header = ctk.CTkLabel(win, text="Select Case", font=("Segoe UI", 22, "bold"), text_color="#008afc")
    header.pack(pady=(24, 8))
    icon = ctk.CTkLabel(win, text="\U0001F4C1", font=("Segoe UI", 36), text_color="#008afc")
    icon.pack()
    desc = ctk.CTkLabel(win, text="Choose an option below to proceed:", font=("Segoe UI", 14), text_color="#222")
    desc.pack(pady=(8, 24))

    # Button panel (centered, with shadow effect)
    btn_panel = ctk.CTkFrame(win, fg_color="white", corner_radius=18, width=540, height=80)
    btn_panel.pack(pady=(0, 32))
    btn_panel.pack_propagate(False)

    def create_case():
        win.destroy()
        create_case_mod = importlib.import_module('create_case')
        create_case_mod.create_case_dialog()

    def open_case():
        win.destroy()
        messagebox.showinfo('Case', 'Proceed to open an existing case.')

    # Both buttons have the same width and height
    button_width = 220
    button_height = 40
    create_btn = ctk.CTkButton(btn_panel, text="Create New Case", font=("Segoe UI", 16, "bold"), fg_color="#008afc", hover_color="#005fa3", text_color="white", width=button_width, height=button_height)
    create_btn.pack(side="left", padx=(32, 24), pady=20)
    open_btn = ctk.CTkButton(btn_panel, text="Open Existing Case", font=("Segoe UI", 16, "bold"), fg_color="#fc3c3c", hover_color="#a30000", text_color="white", width=button_width, height=button_height)
    open_btn.pack(side="left", padx=(24, 32), pady=20)

    win.mainloop()
