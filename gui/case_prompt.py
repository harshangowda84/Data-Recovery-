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

    def launch_main_page(case_name):
        import customtkinter as ctk
        from main_page import MainPage
        win = ctk.CTk()
        MainPage(win, case_name)
        win.mainloop()

    def create_case():
        win.destroy()
        import importlib.util, os
        create_case_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'create_case.py'))
        spec = importlib.util.spec_from_file_location('create_case', create_case_path)
        create_case_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(create_case_mod)
        create_case_mod.create_case_dialog(on_case_created=launch_main_page)

    def open_case():
        win.destroy()
        import importlib.util, os
        open_case_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'open_case.py'))
        spec = importlib.util.spec_from_file_location('open_case', open_case_path)
        open_case_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(open_case_mod)
        open_case_mod.open_case_dialog()

    # Both buttons have the same width and height
    button_width = 220
    button_height = 40
    create_btn = ctk.CTkButton(btn_panel, text="Create New Case", font=("Segoe UI", 16, "bold"), fg_color="#008afc", hover_color="#005fa3", text_color="white", width=button_width, height=button_height, command=create_case)
    create_btn.pack(side="left", padx=(32, 24), pady=20)
    open_btn = ctk.CTkButton(btn_panel, text="Open Existing Case", font=("Segoe UI", 16, "bold"), fg_color="#fc3c3c", hover_color="#a30000", text_color="white", width=button_width, height=button_height, command=open_case)
    open_btn.pack(side="left", padx=(24, 32), pady=20)


    win.mainloop()

if __name__ == '__main__':
    show_case_prompt()
