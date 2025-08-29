import customtkinter as ctk
from tkinter import messagebox
import random

class LoginWindow:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        self._build_ui()

    def _build_ui(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.root.title("Forensic Access - Digital Evidence Recovery System")
        self.root.geometry("800x600")
        self.root.minsize(600, 450)
        self.root.resizable(True, True)
        bg_canvas = ctk.CTkCanvas(self.root, width=800, height=600, highlightthickness=0, bg='#f7f7f7')
        bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        for i in range(0, 600, 2):
            color = "#f7f7f7"
            if i < 120:
                color = "#eaf3fc"
            elif i < 240:
                color = "#f2f7fc"
            elif i < 400:
                color = "#f7f7f7"
            bg_canvas.create_rectangle(0, i, 800, i+2, fill=color, outline="")
        animated_canvas = ctk.CTkCanvas(self.root, width=800, height=600, highlightthickness=0, bg='#f7f7f7')
        animated_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.circles = []
        for _ in range(12):
            x = random.randint(50, 750)
            y = random.randint(120, 580)
            r = random.randint(12, 28)
            color = random.choice(["#eaf3fc", "#dbeafe", "#b6e0fe", "#f2f7fc"])
            circle = animated_canvas.create_oval(x, y, x+r, y+r, fill=color, outline="")
            self.circles.append((circle, x, y, r, random.choice([-1,1]), random.choice([-1,1])))
        self.animation_id = None
        self.animate(animated_canvas)
        tagline = ctk.CTkLabel(self.root, text="Empowering Digital Investigations. Trusted. Secure. Proven.", font=("Segoe UI", 19, "bold"), text_color="#008afc")
        tagline.place(relx=0.5, rely=0.17, anchor="center")
        divider = ctk.CTkLabel(self.root, text="", fg_color="#e0e0e0", width=800, height=2)
        divider.place(relx=0.5, rely=0.94, anchor="center")
        footer_bg = ctk.CTkFrame(self.root, fg_color="#eaf3fc", corner_radius=12, width=820, height=44)
        footer_bg.place(relx=0.5, rely=0.97, anchor="s")
        footer_icon = ctk.CTkLabel(footer_bg, text="\U0001F6E1", font=("Segoe UI", 20), text_color="#008afc")
        footer_icon.place(relx=0.03, rely=0.5, anchor="w")
        footer = ctk.CTkLabel(footer_bg, text="© 2025 Forensic Access. All rights reserved. | Need help? Contact support@forensicaccess.com", font=("Segoe UI", 14), text_color="#008afc")
        footer.place(relx=0.12, rely=0.5, anchor="w")
        main_frame = ctk.CTkFrame(self.root, fg_color="white", corner_radius=24, width=700, height=340)
        main_frame.place(relx=0.5, rely=0.55, anchor="center")
        branding_frame = ctk.CTkFrame(main_frame, fg_color="#eaf3fc", corner_radius=24, width=260, height=340)
        branding_frame.grid(row=0, column=0, sticky="nswe")
        branding_frame.grid_propagate(False)
        branding_icon = ctk.CTkLabel(branding_frame, text="\U0001F512", text_color="#008afc", font=("Segoe UI", 70))
        branding_icon.place(relx=0.5, rely=0.32, anchor="center")
        branding_title = ctk.CTkLabel(branding_frame, text="FORENSIC ACCESS", font=("Segoe UI", 18, "bold"), text_color="#008afc")
        branding_title.place(relx=0.5, rely=0.62, anchor="center")
        branding_subtitle = ctk.CTkLabel(branding_frame, text="Digital Evidence Recovery System", font=("Segoe UI", 13), text_color="#008afc")
        branding_subtitle.place(relx=0.5, rely=0.75, anchor="center")
        form_frame = ctk.CTkFrame(main_frame, fg_color="white", corner_radius=24, width=440, height=340)
        form_frame.grid(row=0, column=1, sticky="nswe")
        form_frame.grid_propagate(False)
        lock_icon = ctk.CTkLabel(form_frame, text="\U0001F512", text_color="#008afc", font=("Segoe UI", 32))
        lock_icon.grid(row=0, column=0, columnspan=2, pady=(28, 8))
        username_label = ctk.CTkLabel(form_frame, text="Username:", font=("Segoe UI", 15, "bold"), text_color="#222")
        username_label.grid(row=1, column=0, sticky="e", padx=(38, 12), pady=(18, 12))
        self.username_entry = ctk.CTkEntry(form_frame, font=("Segoe UI", 15, "bold"), width=220, placeholder_text="Enter your username")
        self.username_entry.grid(row=1, column=1, padx=(12, 38), pady=(18, 12))
        password_label = ctk.CTkLabel(form_frame, text="Password:", font=("Segoe UI", 15, "bold"), text_color="#222")
        password_label.grid(row=2, column=0, sticky="e", padx=(38, 12), pady=(12, 18))
        self.password_entry = ctk.CTkEntry(form_frame, font=("Segoe UI", 15, "bold"), show="*", width=220, placeholder_text="Enter your password")
        self.password_entry.grid(row=2, column=1, padx=(12, 38), pady=(12, 18))
        button_frame = ctk.CTkFrame(form_frame, fg_color="white")
        button_frame.grid(row=3, column=0, columnspan=2, pady=(8, 28))
        login_btn = ctk.CTkButton(button_frame, text="LOGIN", font=("Segoe UI", 14, "bold"), fg_color="#008afc", hover_color="#005fa3", text_color="white", width=120, command=self.login)
        login_btn.pack(side="left", padx=(0, 18))
        exit_btn = ctk.CTkButton(button_frame, text="EXIT", font=("Segoe UI", 14, "bold"), fg_color="#fc3c3c", hover_color="#a30000", text_color="white", width=120, command=self.root.destroy)
        exit_btn.pack(side="left")
        self.root.after(100, lambda: self.username_entry.focus_set())
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus_set())
        self.password_entry.bind('<Return>', lambda e: self.login())
        tagline.lift()
        footer.lift()

    def animate(self, animated_canvas):
        for i, (circle, x, y, r, dx, dy) in enumerate(self.circles):
            x += dx
            y += dy
            if x < 30 or x > 770: dx = -dx
            if y < 100 or y > 570: dy = -dy
            animated_canvas.coords(circle, x, y, x+r, y+r)
            self.circles[i] = (circle, x, y, r, dx, dy)
        self.animation_id = self.root.after(40, lambda: self.animate(animated_canvas))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin123":
            if self.animation_id:
                self.root.after_cancel(self.animation_id)
            self.root.destroy()
            from case_prompt import show_case_prompt
            show_case_prompt()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
if __name__ == '__main__':
    root = ctk.CTk()
    LoginWindow(root, lambda: None)
    root.mainloop()
