import customtkinter as ctk
import uuid
from tkinter import messagebox
import importlib.util
import os
case_manager_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cases/case_manager.py'))
spec = importlib.util.spec_from_file_location('case_manager', case_manager_path)
case_manager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(case_manager)
CaseManager = case_manager.CaseManager

def create_case_dialog():
    case_id = str(uuid.uuid4())[:8]
    case_name = f"Case_{case_id}"
    win = ctk.CTk()
    win.title('Create New Case')
    win.geometry('540x480')
    win.resizable(False, False)
    win.configure(fg_color="#f7f7f7")

    # Header with icon
    header_frame = ctk.CTkFrame(win, fg_color="#f7f7f7")
    header_frame.pack(pady=(24, 0))
    header_icon = ctk.CTkLabel(header_frame, text="\U0001F4C8", font=("Segoe UI", 32), text_color="#008afc")
    header_icon.pack(side="left", padx=(0, 12))
    header = ctk.CTkLabel(header_frame, text='Create New Case', font=('Segoe UI', 24, 'bold'), text_color='#008afc')
    header.pack(side="left")

    # Form Frame (card)
    form = ctk.CTkFrame(win, fg_color='white', corner_radius=18)
    form.pack(pady=(18, 24), padx=32, fill='x')

    # Investigator Name
    inv_icon = ctk.CTkLabel(form, text="\U0001F464", font=("Segoe UI", 18), text_color="#008afc")
    inv_icon.grid(row=0, column=0, sticky='e', padx=(18, 6), pady=(22, 12))
    inv_label = ctk.CTkLabel(form, text='Investigator Name:', font=('Segoe UI', 14, 'bold'), text_color='#222')
    inv_label.grid(row=0, column=1, sticky='e', padx=(0, 12), pady=(22, 12))
    inv_entry = ctk.CTkEntry(form, font=('Segoe UI', 14), width=260, placeholder_text='Enter investigator name')
    inv_entry.configure(fg_color='white', text_color='black', placeholder_text_color='#888')
    inv_entry.grid(row=0, column=2, padx=(0, 18), pady=(22, 12))

    # Case ID
    cid_icon = ctk.CTkLabel(form, text="\U0001F194", font=("Segoe UI", 18), text_color="#008afc")
    cid_icon.grid(row=1, column=0, sticky='e', padx=(18, 6), pady=(12, 12))
    cid_label = ctk.CTkLabel(form, text='Case ID:', font=('Segoe UI', 14, 'bold'), text_color='#222')
    cid_label.grid(row=1, column=1, sticky='e', padx=(0, 12), pady=(12, 12))
    cid_entry = ctk.CTkEntry(form, font=('Segoe UI', 14), width=260)
    cid_entry.configure(fg_color='white', text_color='black', placeholder_text_color='#888')
    cid_entry.grid(row=1, column=2, padx=(0, 18), pady=(12, 12))
    cid_entry.insert(0, case_id)

    # Case Name
    cname_icon = ctk.CTkLabel(form, text="\U0001F4D6", font=("Segoe UI", 18), text_color="#008afc")
    cname_icon.grid(row=2, column=0, sticky='e', padx=(18, 6), pady=(12, 12))
    cname_label = ctk.CTkLabel(form, text='Case Name:', font=('Segoe UI', 14, 'bold'), text_color='#222')
    cname_label.grid(row=2, column=1, sticky='e', padx=(0, 12), pady=(12, 12))
    cname_entry = ctk.CTkEntry(form, font=('Segoe UI', 14), width=260)
    cname_entry.configure(fg_color='white', text_color='black', placeholder_text_color='#888')
    cname_entry.grid(row=2, column=2, padx=(0, 18), pady=(12, 12))
    cname_entry.insert(0, case_name)

    # Case Description
    desc_icon = ctk.CTkLabel(form, text="\U0001F4DD", font=("Segoe UI", 18), text_color="#008afc")
    desc_icon.grid(row=3, column=0, sticky='ne', padx=(18, 6), pady=(12, 18))
    desc_label = ctk.CTkLabel(form, text='Case Description:', font=('Segoe UI', 14, 'bold'), text_color='#222')
    desc_label.grid(row=3, column=1, sticky='ne', padx=(0, 12), pady=(12, 18))
    desc_entry = ctk.CTkTextbox(form, font=('Segoe UI', 14), width=260, height=90, border_width=2, border_color="#b0b0b0")
    desc_entry.configure(fg_color='white', text_color='black')
    desc_entry.grid(row=3, column=2, padx=(0, 18), pady=(12, 18))
    desc_entry.insert('1.0', 'Enter case description...')

    # Button Frame
    btn_frame = ctk.CTkFrame(form, fg_color='white')
    btn_frame.grid(row=4, column=0, columnspan=3, pady=(8, 18))
    def submit():
        inv = inv_entry.get().strip()
        cid = cid_entry.get().strip()
        cname = cname_entry.get().strip()
        desc = desc_entry.get('1.0', 'end').strip()
        if not inv or not cid or not cname:
            messagebox.showerror('Error', 'Investigator Name, Case ID, and Case Name are required.')
            return
        # Make description optional
        if desc == 'Enter case description...' or not desc:
            desc = ''
        try:
            manager = CaseManager()
            manager.save_case(cid, cname, inv, desc)
            messagebox.showinfo('Case Created', f'Investigator: {inv}\nCase ID: {cid}\nCase Name: {cname}\nDescription: {desc}')
        except Exception as e:
            messagebox.showerror('Database Error', f'Failed to save case: {e}')
        win.destroy()
    create_btn = ctk.CTkButton(btn_frame, text='Create', command=submit, font=('Segoe UI', 14, 'bold'), fg_color='#008afc', hover_color='#005fa3', text_color='white', width=120)
    create_btn.pack(side='left', padx=(0, 18))
    def cancel():
        win.destroy()
        import importlib.util, os
        case_prompt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'case_prompt.py'))
        spec = importlib.util.spec_from_file_location('case_prompt', case_prompt_path)
        case_prompt_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(case_prompt_mod)
        case_prompt_mod.show_case_prompt()
    cancel_btn = ctk.CTkButton(btn_frame, text='Cancel', command=cancel, font=('Segoe UI', 14, 'bold'), fg_color='#fc3c3c', hover_color='#a30000', text_color='white', width=120)
    cancel_btn.pack(side='left')

    win.mainloop()

if __name__ == '__main__':
    create_case_dialog()
