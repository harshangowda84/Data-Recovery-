
import customtkinter as ctk
from tkinter import messagebox
import importlib.util, os

def open_case_dialog():
    case_manager_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cases/case_manager.py'))
    spec = importlib.util.spec_from_file_location('case_manager', case_manager_path)
    case_manager_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(case_manager_mod)
    CaseManager = case_manager_mod.CaseManager
    manager = CaseManager()
    cases = manager.get_cases()

    win = ctk.CTk()
    win.title('Open Existing Case')
    win.geometry('700x400')
    win.resizable(False, False)
    win.configure(fg_color="#f7f7f7")

    header = ctk.CTkLabel(win, text='Open Existing Case', font=('Segoe UI', 24, 'bold'), text_color='#008afc')
    header.pack(pady=(24, 8))

    main_frame = ctk.CTkFrame(win, fg_color='white', corner_radius=18)
    main_frame.pack(pady=(8, 18), padx=32, fill='both', expand=True)

    # Left: Search and case list
    left_frame = ctk.CTkFrame(main_frame, fg_color='white', corner_radius=12, width=280)
    left_frame.pack(side='left', fill='y', padx=(0, 18), pady=12)
    left_frame.pack_propagate(False)

    search_entry = ctk.CTkEntry(left_frame, font=('Segoe UI', 13), width=220, placeholder_text='Search by name or ID')
    search_entry.pack(pady=(12, 8), padx=18)

    case_listbox = ctk.CTkScrollableFrame(left_frame, fg_color='white', corner_radius=8, width=240, height=220)
    case_listbox.pack(padx=18, pady=(0, 12), fill='y', expand=True)

    # Right: Details panel
    details_frame = ctk.CTkFrame(main_frame, fg_color='#f7f7f7', corner_radius=12, width=340)
    details_frame.pack(side='left', fill='both', expand=True, padx=(0, 0), pady=12)
    details_frame.pack_propagate(False)

    details_label = ctk.CTkLabel(details_frame, text='Select a case to view details.', font=('Segoe UI', 15), text_color='#222')
    details_label.pack(pady=(32, 12), padx=18)

    def show_details(case):
        cid = case[1]
        cname = case[2]
        inv = case[3]
        desc = case[4] if case[4] else '(No description)'
        details_label.configure(text=f"Case Name: {cname}\nCase ID: {cid}\nInvestigator: {inv}\nDescription: {desc}")

        # Add Open button to launch main page with selected case name
        if hasattr(details_frame, 'open_btn') and details_frame.open_btn:
            details_frame.open_btn.destroy()
        def open_main():
            win.destroy()
            import customtkinter as ctk
            from main_page import MainPage
            main_win = ctk.CTk()
            MainPage(main_win, cname)
            main_win.mainloop()
        details_frame.open_btn = ctk.CTkButton(details_frame, text='Open This Case', font=('Segoe UI', 14, 'bold'), fg_color='#008afc', hover_color='#005fa3', text_color='white', width=180, command=open_main)
        details_frame.open_btn.pack(pady=(18, 8))

    case_buttons = []
    def populate_list(filter_text=None):
        for btn in case_buttons:
            btn.destroy()
        case_buttons.clear()
        for case in cases:
            cid = case[1]
            cname = case[2]
            inv = case[3]
            if filter_text:
                if filter_text.lower() not in cname.lower() and filter_text.lower() not in cid.lower():
                    continue
            btn = ctk.CTkButton(case_listbox, text=f"{cname} (ID: {cid})", font=('Segoe UI', 13), fg_color='#eaf3fc', hover_color='#b6e0fe', text_color='#008afc', width=220, command=lambda c=case: show_details(c))
            btn.pack(fill='x', pady=4)
            case_buttons.append(btn)
    populate_list()

    def on_search(*args):
        filter_text = search_entry.get().strip()
        populate_list(filter_text)
    search_entry.bind('<KeyRelease>', on_search)

    # Back button
    def go_back():
        win.destroy()
        case_prompt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'case_prompt.py'))
        if os.path.exists(case_prompt_path):
            spec = importlib.util.spec_from_file_location('case_prompt', case_prompt_path)
            case_prompt_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(case_prompt_mod)
            case_prompt_mod.show_case_prompt()

    back_btn = ctk.CTkButton(win, text='Back', font=('Segoe UI', 13, 'bold'), fg_color='#fc3c3c', hover_color='#a30000', text_color='white', width=100, command=go_back)
    back_btn.place(relx=0.04, rely=0.06)

    win.mainloop()

if __name__ == '__main__':
    open_case_dialog()
