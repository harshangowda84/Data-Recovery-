import customtkinter as ctk
from tkinter import messagebox
from case_prompt import show_case_prompt
import random

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def main():
    root = ctk.CTk()
    root.title("Forensic Access - Digital Evidence Recovery System")
    root.geometry("800x600")
    root.minsize(600, 450)
    root.resizable(True, True)

    # Subtle background gradient using Canvas
    bg_canvas = ctk.CTkCanvas(root, width=800, height=600, highlightthickness=0, bg='#f7f7f7')
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

    # Animated floating circles (background only)
    import random
    animated_canvas = ctk.CTkCanvas(root, width=800, height=600, highlightthickness=0, bg='#f7f7f7')
    animated_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    circles = []
    for _ in range(12):
        x = random.randint(50, 750)
        y = random.randint(120, 580)
        r = random.randint(12, 28)
        color = random.choice(["#eaf3fc", "#dbeafe", "#b6e0fe", "#f2f7fc"])
        circle = animated_canvas.create_oval(x, y, x+r, y+r, fill=color, outline="")
        circles.append((circle, x, y, r, random.choice([-1,1]), random.choice([-1,1])))
    animation_id = None
    def animate():
        nonlocal animation_id
        for i, (circle, x, y, r, dx, dy) in enumerate(circles):
            x += dx
            y += dy
            if x < 30 or x > 770: dx = -dx
            if y < 100 or y > 570: dy = -dy
            animated_canvas.coords(circle, x, y, x+r, y+r)
            circles[i] = (circle, x, y, r, dx, dy)
        animation_id = root.after(40, animate)
    animate()

    # Enhanced Tagline under header
    tagline = ctk.CTkLabel(root, text="Empowering Digital Investigations. Trusted. Secure. Proven.", font=("Segoe UI", 19, "bold"), text_color="#008afc")
    tagline.place(relx=0.5, rely=0.17, anchor="center")

    # Divider line above footer
    divider = ctk.CTkLabel(root, text="", fg_color="#e0e0e0", width=800, height=2)
    divider.place(relx=0.5, rely=0.94, anchor="center")

    # Enhanced Footer with wider background and better alignment
    footer_bg = ctk.CTkFrame(root, fg_color="#eaf3fc", corner_radius=12, width=820, height=44)
    footer_bg.place(relx=0.5, rely=0.97, anchor="s")
    footer_icon = ctk.CTkLabel(footer_bg, text="\U0001F6E1", font=("Segoe UI", 20), text_color="#008afc")
    footer_icon.place(relx=0.03, rely=0.5, anchor="w")
    footer = ctk.CTkLabel(footer_bg, text="© 2025 Forensic Access. All rights reserved. | Need help? Contact support@forensicaccess.com", font=("Segoe UI", 14), text_color="#008afc")
    footer.place(relx=0.12, rely=0.5, anchor="w")

    # Main container frame (centered, wide)
    main_frame = ctk.CTkFrame(root, fg_color="white", corner_radius=24, width=700, height=340)
    main_frame.place(relx=0.5, rely=0.55, anchor="center")

    # Branding panel (left side)
    branding_frame = ctk.CTkFrame(main_frame, fg_color="#eaf3fc", corner_radius=24, width=260, height=340)
    branding_frame.grid(row=0, column=0, sticky="nswe")
    branding_frame.grid_propagate(False)
    # Logo or illustration (lock icon)
    branding_icon = ctk.CTkLabel(branding_frame, text="\U0001F512", text_color="#008afc", font=("Segoe UI", 70))
    branding_icon.place(relx=0.5, rely=0.32, anchor="center")
    branding_title = ctk.CTkLabel(branding_frame, text="FORENSIC ACCESS", font=("Segoe UI", 18, "bold"), text_color="#008afc")
    branding_title.place(relx=0.5, rely=0.62, anchor="center")
    branding_subtitle = ctk.CTkLabel(branding_frame, text="Digital Evidence Recovery System", font=("Segoe UI", 13), text_color="#008afc")
    branding_subtitle.place(relx=0.5, rely=0.75, anchor="center")

    # Login form panel (right side)
    form_frame = ctk.CTkFrame(main_frame, fg_color="white", corner_radius=24, width=440, height=340)
    form_frame.grid(row=0, column=1, sticky="nswe")
    form_frame.grid_propagate(False)

    # Lock icon above form
    lock_icon = ctk.CTkLabel(form_frame, text="\U0001F512", text_color="#008afc", font=("Segoe UI", 32))
    lock_icon.grid(row=0, column=0, columnspan=2, pady=(28, 8))

    # Username
    username_label = ctk.CTkLabel(form_frame, text="Username:", font=("Segoe UI", 15, "bold"), text_color="#222")
    username_label.grid(row=1, column=0, sticky="e", padx=(38, 12), pady=(18, 12))
    username_entry = ctk.CTkEntry(form_frame, font=("Segoe UI", 15, "bold"), width=220, placeholder_text="Enter your username")
    username_entry.grid(row=1, column=1, padx=(12, 38), pady=(18, 12))

    # Password
    password_label = ctk.CTkLabel(form_frame, text="Password:", font=("Segoe UI", 15, "bold"), text_color="#222")
    password_label.grid(row=2, column=0, sticky="e", padx=(38, 12), pady=(12, 18))
    password_entry = ctk.CTkEntry(form_frame, font=("Segoe UI", 15, "bold"), show="*", width=220, placeholder_text="Enter your password")
    password_entry.grid(row=2, column=1, padx=(12, 38), pady=(12, 18))

    # Buttons (horizontal, below inputs)
    button_frame = ctk.CTkFrame(form_frame, fg_color="white")
    button_frame.grid(row=3, column=0, columnspan=2, pady=(8, 28))
    login_btn = ctk.CTkButton(button_frame, text="LOGIN", font=("Segoe UI", 14, "bold"), fg_color="#008afc", hover_color="#005fa3", text_color="white", width=120, command=lambda: login())
    login_btn.pack(side="left", padx=(0, 18))
    exit_btn = ctk.CTkButton(button_frame, text="EXIT", font=("Segoe UI", 14, "bold"), fg_color="#fc3c3c", hover_color="#a30000", text_color="white", width=120, command=root.destroy)
    exit_btn.pack(side="left")

    # Focus and Keyboard Navigation
    root.after(100, lambda: username_entry.focus_set())
    username_entry.bind('<Return>', lambda e: password_entry.focus_set())
    password_entry.bind('<Return>', lambda e: login())

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "admin123":
            if animation_id:
                root.after_cancel(animation_id)
            root.destroy()
            show_case_prompt()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    # Lift widgets above the animated canvas
    tagline.lift()
    footer.lift()

    root.mainloop()

if __name__ == '__main__':
    main()
