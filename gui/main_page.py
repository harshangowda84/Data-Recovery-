"""
Required packages:
	pip install customtkinter
	pip install pywin32
"""
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import platform
try:
	import win32file
except ImportError:
	win32file = None

class MainPage:
	def __init__(self, win, case_name=None):
		self.win = win
		title = f'Data Reviver - Forensic Analysis Tool'
		if case_name:
			title += f' - {case_name}'
		self.win.title(title)
		self.win.geometry('1250x750')
		self.win.resizable(True, True)
		self.setup_ui()

	def setup_ui(self):
		# Top menu bar
		self.menu_bar = ctk.CTkFrame(self.win, fg_color="#b6d6f2", height=32)
		self.menu_bar.pack(fill='x', side='top')
		ctk.CTkLabel(self.menu_bar, text="DR", font=("Segoe UI", 16, "bold"), text_color="#005fa3", width=40).pack(side='left', padx=(8,0))
		for name in ["File", "Tools", "Analysis", "Help"]:
			ctk.CTkLabel(self.menu_bar, text=name, font=("Segoe UI", 15), text_color="#005fa3", width=80).pack(side='left', padx=(0,0))

		# Main layout
		self.main_frame = ctk.CTkFrame(self.win, fg_color="#eaf3fc")
		self.main_frame.pack(fill='both', expand=True)

		# Left panel (drives)
		self.left_panel = ctk.CTkFrame(self.main_frame, fg_color="#eaf3fc", width=320)
		self.left_panel.pack(side='left', fill='y', padx=(8,0), pady=(8,8))
		self.left_panel.pack_propagate(False)
		self.refresh_btn = ctk.CTkButton(self.left_panel, text="⟳ Refresh Drives", font=("Segoe UI", 18, "bold"), fg_color="#008afc", hover_color="#005fa3", text_color="white", height=40, command=self.list_drives)
		self.refresh_btn.pack(fill='x', pady=(8,12), padx=8)
		self.drive_list = ctk.CTkFrame(self.left_panel, fg_color="#f7f7f7", corner_radius=8)
		self.drive_list.pack(fill='both', expand=True, padx=8, pady=(0,8))
		self.list_drives()

		# Main panel (scan + files)
		self.right_panel = ctk.CTkFrame(self.main_frame, fg_color="#eaf3fc")
		self.right_panel.pack(side='left', fill='both', expand=True, padx=(12,8), pady=(8,8))
		self.right_panel.pack_propagate(False)

		# Large scan header
		self.scan_header = ctk.CTkFrame(self.right_panel, fg_color="#008afc", height=80, corner_radius=8)
		self.scan_header.pack(fill='x', padx=8, pady=(8,0))
		self.scan_header.pack_propagate(False)
		ctk.CTkLabel(self.scan_header, text="🔍 Start Scan", font=("Segoe UI", 38, "bold"), text_color="white").pack(side='left', padx=32)

		# Search bar and options
		self.search_frame = ctk.CTkFrame(self.right_panel, fg_color="#eaf3fc")
		self.search_frame.pack(fill='x', padx=8, pady=(8,0))
		self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Search files...", font=("Segoe UI", 15), width=600)
		self.search_entry.pack(side='left', padx=(8,0), pady=8)
		self.show_system_chk = ctk.CTkCheckBox(self.search_frame, text="Show system files and unknown types", font=("Segoe UI", 13))
		self.show_system_chk.pack(side='right', padx=(0,12), pady=8)

		# File table
		self.file_table = ctk.CTkFrame(self.right_panel, fg_color="#f7f7f7", corner_radius=8)
		self.file_table.pack(fill='both', expand=True, padx=8, pady=(0,8))
		self.file_table.pack_propagate(False)
		# Table header
		header = ctk.CTkFrame(self.file_table, fg_color="#eaf3fc")
		header.pack(fill='x', padx=8, pady=(8,0))
		for col, w in zip(["Name", "Type", "Size", "Last Modified", "Path", "Chance of Recovery"], [180, 80, 80, 140, 220, 160]):
			ctk.CTkLabel(header, text=col, font=("Segoe UI", 15, "bold"), text_color="#008afc", width=w, anchor='w').pack(side='left', padx=2)
		# Table body
		self.table_body = ctk.CTkFrame(self.file_table, fg_color="#f7f7f7")
		self.table_body.pack(fill='both', expand=True, padx=8, pady=(0,8))

		# Status bar
		self.status_bar = ctk.CTkFrame(self.win, fg_color="#b6d6f2", height=28)
		self.status_bar.pack(fill='x', side='bottom')
		ctk.CTkLabel(self.status_bar, text="Role: Administrator  Permissions: Full system access, user management, case creation/deletion  Login: 07:56:40", font=("Segoe UI", 13), text_color="#005fa3").pack(side='left', padx=12)

	def list_drives(self):
		# Clear previous drive labels
		for widget in self.drive_list.winfo_children():
			widget.destroy()
		drives = []
		external_drives = []
		if platform.system() == "Windows" and win32file:
			bitmask = win32file.GetLogicalDrives()
			for i in range(26):
				if bitmask & (1 << i):
					drive_letter = chr(65 + i) + ":\\"
					try:
						drive_type = win32file.GetDriveType(drive_letter)
						if drive_type == win32file.DRIVE_REMOVABLE:
							external_drives.append(drive_letter)
						else:
							drives.append(drive_letter)
					except Exception:
						continue
		else:
			for mount_dir in ["/media", "/Volumes"]:
				if os.path.exists(mount_dir):
					for d in os.listdir(mount_dir):
						external_drives.append(os.path.join(mount_dir, d))
		for drive in drives:
			ctk.CTkLabel(self.drive_list, text=f"{drive} (Fixed)", font=("Segoe UI", 15, "bold"), text_color="#005fa3", anchor='w').pack(fill='x', padx=12, pady=6)
		for drive in external_drives:
			ctk.CTkLabel(self.drive_list, text=f"{drive} (External)", font=("Segoe UI", 15, "bold"), text_color="#008afc", anchor='w').pack(fill='x', padx=12, pady=6)

if __name__ == '__main__':
	win = ctk.CTk()
	MainPage(win)
	win.mainloop()
