



import customtkinter as ctk
import os
import platform
if platform.system() == "Windows":
    import win32file

import psutil
import win32file

class MainPage:
    def __init__(self, win):
        self.win = win
        self.win.title('Data Reviver - Forensic Analysis Tool - Investigation_20250821 (Case ID: 1498B1FD)')
        self.win.geometry('1250x750')

        import customtkinter as ctk

        class MainPage:
            def __init__(self, win):
                self.win = win
                self.win.title('Data Reviver - Forensic Analysis Tool - Investigation_20250821 (Case ID: 1498B1FD)')
                self.win.geometry('1250x750')
                self.win.resizable(True, True)

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
                self.refresh_btn = ctk.CTkButton(self.left_panel, text="⟳ Refresh Drives", font=("Segoe UI", 18, "bold"), fg_color="#008afc", hover_color="#005fa3", text_color="white", height=40)
                self.refresh_btn.pack(fill='x', pady=(8,12), padx=8)
                self.drive_list = ctk.CTkFrame(self.left_panel, fg_color="#f7f7f7", corner_radius=8)
                self.drive_list.pack(fill='both', expand=True, padx=8, pady=(0,8))
                # Example drives
                for drive in ["C: LocalDisk (NTFS)", "D: New Volume (NTFS)"]:
                    ctk.CTkLabel(self.drive_list, text=drive, font=("Segoe UI", 15, "bold"), text_color="#005fa3", anchor='w').pack(fill='x', padx=12, pady=6)

                # Right panel (scan + files)
                self.right_panel = ctk.CTkFrame(self.main_frame, fg_color="#eaf3fc")
                self.right_panel.pack(side='left', fill='both', expand=True, padx=(12,8), pady=(8,8))
                self.right_panel.pack_propagate(False)

                # Blue scan header
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
                # Table body (empty)
                self.table_body = ctk.CTkFrame(self.file_table, fg_color="#f7f7f7")
                self.table_body.pack(fill='both', expand=True, padx=8, pady=(0,8))

                # Status bar
                self.status_bar = ctk.CTkFrame(self.win, fg_color="#b6d6f2", height=28)
                self.status_bar.pack(fill='x', side='bottom')
                ctk.CTkLabel(self.status_bar, text="Role: Administrator  Permissions: Full system access, user management, case creation/deletion  Login: 07:56:40", font=("Segoe UI", 13), text_color="#005fa3").pack(side='left', padx=12)


        # Main layout
        self.main_frame = ctk.CTkFrame(self.win, fg_color="#eaf3fc")
        self.main_frame.pack(fill='both', expand=True)

        # Left panel (drives)
        self.left_panel = ctk.CTkFrame(self.main_frame, fg_color="#eaf3fc", width=320)
        self.left_panel.pack(side='left', fill='y', padx=(8,0), pady=(8,8))
        self.left_panel.pack_propagate(False)
        self.refresh_btn = ctk.CTkButton(self.left_panel, text="⟳ Refresh Drives", font=("Segoe UI", 18, "bold"), fg_color="#008afc", hover_color="#005fa3", text_color="white", height=40)
        self.refresh_btn.pack(fill='x', pady=(8,12), padx=8)
        self.drive_list = ctk.CTkFrame(self.left_panel, fg_color="#f7f7f7", corner_radius=8)
        self.drive_list.pack(fill='both', expand=True, padx=8, pady=(0,8))
        # List real drives
        self.list_drives()

    def list_drives(self):
        # Clear previous drive labels
        for widget in self.drive_list.winfo_children():
            widget.destroy()
        drives = []
        external_drives = []
        if platform.system() == "Windows":
            bitmask = win32file.GetLogicalDrives()
            for i in range(26):
                if bitmask & (1 << i):
                    drive_letter = chr(65 + i) + ":\\"
                    try:
                        drive_type = win32file.GetDriveType(drive_letter)
                        # 2: Removable, 3: Fixed, 4: Network, 5: CD-ROM, 6: RAM Disk
                        if drive_type == win32file.DRIVE_REMOVABLE:
                            external_drives.append(drive_letter)
                        else:
                            drives.append(drive_letter)
                    except Exception:
                        continue
        else:
            # For Linux/Mac, show mount points in /media or /Volumes
            for mount_dir in ["/media", "/Volumes"]:
                if os.path.exists(mount_dir):
                    for d in os.listdir(mount_dir):
                        external_drives.append(os.path.join(mount_dir, d))
        # Show drives
        for drive in drives:
            ctk.CTkLabel(self.drive_list, text=f"{drive} (Fixed)", font=("Segoe UI", 15, "bold"), text_color="#005fa3", anchor='w').pack(fill='x', padx=12, pady=6)
        for drive in external_drives:
            ctk.CTkLabel(self.drive_list, text=f"{drive} (External)", font=("Segoe UI", 15, "bold"), text_color="#008afc", anchor='w').pack(fill='x', padx=12, pady=6)

        # Right panel (scan + files)
        self.right_panel = ctk.CTkFrame(self.main_frame, fg_color="#eaf3fc")
        self.right_panel.pack(side='left', fill='both', expand=True, padx=(12,8), pady=(8,8))
        self.right_panel.pack_propagate(False)

        # Blue scan header
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
        # Table body (empty)
        self.table_body = ctk.CTkFrame(self.file_table, fg_color="#f7f7f7")
        self.table_body.pack(fill='both', expand=True, padx=8, pady=(0,8))

        # Status bar
        self.status_bar = ctk.CTkFrame(self.win, fg_color="#b6d6f2", height=28)
        self.status_bar.pack(fill='x', side='bottom')
        ctk.CTkLabel(self.status_bar, text="Role: Administrator  Permissions: Full system access, user management, case creation/deletion  Login: 07:56:40", font=("Segoe UI", 13), text_color="#005fa3").pack(side='left', padx=12)


def main_page():
    win = ctk.CTk()
    MainPage(win)
    win.mainloop()

if __name__ == '__main__':
    main_page()

def main_page():
    win = ctk.CTk()
    MainPage(win)
    win.mainloop()

if __name__ == '__main__':
    main_page()
