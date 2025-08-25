import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
for subdir in ['auth', 'cases', 'engine', 'analysis', 'reporting']:
    sys.path.append(os.path.join(project_root, subdir))
from engine.recovery_engine import RecoveryEngine
from analysis.metadata_analyzer import MetadataAnalyzer
from analysis.advanced_analyzer import AdvancedAnalyzer
import tkinter as tk
from tkinter import messagebox, filedialog, Listbox

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Forensic Recovery Tool')
        self.recovery_engine = None
        self.deleted_files = []
        self.metadata_analyzer = MetadataAnalyzer()
        self.advanced_analyzer = AdvancedAnalyzer()
        self.setup_ui()

    def setup_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)
        tk.Button(frame, text='Load Disk Image', command=self.load_image).pack()
        self.listbox = Listbox(frame, width=60)
        self.listbox.pack()
        self.listbox.bind('<<ListboxSelect>>', self.display_metadata)
        tk.Button(frame, text='Recover Selected File', command=self.recover_file).pack()
        self.metadata_text = tk.Text(frame, height=10, width=60)
        self.metadata_text.pack()
        tk.Button(frame, text='Show Timeline', command=self.show_timeline).pack()
        tk.Button(frame, text='Generate Report', command=self.generate_report).pack()
    def generate_report(self):
        from reporting.report_generator import ReportGenerator
        output_path = filedialog.asksaveasfilename(title='Save Report', defaultextension='.pdf', filetypes=[('PDF Files', '*.pdf')])
        if not output_path:
            return
        case_name = 'Active Case'  # Placeholder, integrate with case management if needed
        analyst = 'Analyst'        # Placeholder, integrate with login if needed
        findings = []
        for f in self.deleted_files:
            findings.append(f)
        report_gen = ReportGenerator()
        report_gen.generate_pdf(case_name, analyst, findings, output_path)
        messagebox.showinfo('Report', f'Report saved to {output_path}')

    def load_image(self):
        img_path = filedialog.askopenfilename(title='Select Disk Image', filetypes=[('Image Files', '*.img;*.dd')])
        if img_path:
            self.recovery_engine = RecoveryEngine(img_path)
            self.deleted_files = self.recovery_engine.scan_deleted_files()
            self.listbox.delete(0, tk.END)
            for f in self.deleted_files:
                self.listbox.insert(tk.END, f'{f["name"]} ({f["size"]} bytes)')

    def recover_file(self):
        selection = self.listbox.curselection()
        if selection and self.recovery_engine:
            file_metadata = self.deleted_files[selection[0]]
            output_dir = filedialog.askdirectory(title='Select Output Directory')
            if output_dir:
                success = self.recovery_engine.recover_file(file_metadata, output_dir)
                if success:
                    messagebox.showinfo('Recovery', 'File recovered successfully')
                else:
                    messagebox.showerror('Recovery Failed', 'Could not recover file')

    def display_metadata(self, event):
        selection = self.listbox.curselection()
        if selection and self.recovery_engine:
            file_metadata = self.deleted_files[selection[0]]
            file_path = file_metadata["name"]
            self.metadata_text.delete(1.0, tk.END)
            try:
                mac = self.metadata_analyzer.extract_mac_times(file_path)
                file_hash = self.metadata_analyzer.calculate_hash(file_path)
                exif = self.metadata_analyzer.extract_exif(file_path)
                signature = self.advanced_analyzer.analyze_signature(file_path)
                self.metadata_text.insert(tk.END, f"MAC Times: {mac}\n")
                self.metadata_text.insert(tk.END, f"SHA-256: {file_hash}\n")
                self.metadata_text.insert(tk.END, f"EXIF: {exif}\n")
                self.metadata_text.insert(tk.END, f"File Signature: {signature}\n")
            except Exception as e:
                self.metadata_text.insert(tk.END, f"Metadata unavailable: {e}\n")

    def show_timeline(self):
        timestamps = []
        for f in self.deleted_files:
            try:
                mac = self.metadata_analyzer.extract_mac_times(f["name"])
                timestamps.append(mac)
            except Exception:
                continue
        self.advanced_analyzer.plot_timeline(timestamps)

if __name__ == '__main__':
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()