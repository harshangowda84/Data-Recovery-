import tkinter as tk
from tkinter import simpledialog, messagebox
import uuid

def create_case_dialog():
    case_id = str(uuid.uuid4())[:8]
    case_name = f"Case_{case_id}"
    root = tk.Tk()
    root.withdraw()
    dialog = tk.Toplevel()
    dialog.title('Create New Case')
    dialog.geometry('400x270')
    dialog.configure(bg='#f4f4f4')
    # Header
    header = tk.Frame(dialog, bg='#0084e8', height=50)
    header.pack(fill='x')
    header.pack_propagate(False)
    tk.Label(header, text='Create New Case', bg='#0084e8', fg='white', font=('Arial', 16, 'bold')).pack(side='left', padx=20, pady=10)
    # Form Frame
    form = tk.Frame(dialog, bg='white', bd=1, relief='solid')
    form.pack(pady=(20,0), ipadx=10, ipady=10, expand=True)
    # Case ID
    tk.Label(form, text='Case ID:', bg='white', anchor='w', font=('Arial', 10)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
    case_id_entry = tk.Entry(form, bd=1, relief='solid', font=('Arial', 10))
    case_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    case_id_entry.insert(0, case_id)
    # Case Name
    tk.Label(form, text='Case Name:', bg='white', anchor='w', font=('Arial', 10)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
    case_name_entry = tk.Entry(form, bd=1, relief='solid', font=('Arial', 10))
    case_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    case_name_entry.insert(0, case_name)
    # Description
    tk.Label(form, text='Description:', bg='white', anchor='w', font=('Arial', 10)).grid(row=2, column=0, padx=10, pady=10, sticky='ne')
    desc_entry = tk.Text(form, height=2, width=25, bd=1, relief='solid', font=('Arial', 10))
    desc_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    # Button Frame
    btn_frame = tk.Frame(form, bg='white')
    btn_frame.grid(row=3, column=0, columnspan=2, pady=(10,0))
    def submit():
        cid = case_id_entry.get().strip()
        cname = case_name_entry.get().strip()
        desc = desc_entry.get('1.0', tk.END).strip()
        if not cid or not cname:
            messagebox.showerror('Error', 'Case ID and Case Name are required.')
            return
        messagebox.showinfo('Case Created', f'Case ID: {cid}\nCase Name: {cname}\nDescription: {desc}')
        dialog.destroy()
        root.destroy()
    create_btn = tk.Button(btn_frame, text='Create', command=submit, bg='#0084e8', fg='white', font=('Arial', 10, 'bold'), bd=0, activebackground='#005fa3', activeforeground='white')
    create_btn.grid(row=0, column=0, padx=10)
    cancel_btn = tk.Button(btn_frame, text='Cancel', command=lambda: [dialog.destroy(), root.destroy()], bg='#e84141', fg='white', font=('Arial', 10, 'bold'), bd=0, activebackground='#a32f2f', activeforeground='white')
    cancel_btn.grid(row=0, column=1, padx=10)
    dialog.mainloop()

if __name__ == '__main__':
    create_case_dialog()
