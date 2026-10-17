import tkinter as tk
from tkinter import messagebox
import random
import string
import os

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Key Generator")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#F3F4F6")

        # Cryptographically secure random engine selection
        self.crypto_rand = random.SystemRandom()

        # UI Header Layout
        header = tk.Label(root, text="LockBox Local Vault", bg="#1E3A8A", fg="white", font=("Arial", 16, "bold"), pady=10)
        header.pack(fill="x")

        # Visual Grid Input Frame Container
        form_frame = tk.Frame(root, bg="#F3F4F6", padx=20, pady=20)
        form_frame.pack(fill="both", expand=True)

        # Application Form Fields
        tk.Label(form_frame, text="Website / Service Name:", bg="#F3F4F6", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.site_entry = tk.Entry(form_frame, width=30, font=("Arial", 10))
        self.site_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Username / Email Address:", bg="#F3F4F6", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        self.user_entry = tk.Entry(form_frame, width=30, font=("Arial", 10))
        self.user_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Password Length Limit:", bg="#F3F4F6", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        self.length_slider = tk.Scale(form_frame, from_=8, to=32, orient="horizontal", bg="#F3F4F6", highlightthickness=0)
        self.length_slider.set(16)  # Standard secure safe default setting
        self.length_slider.grid(row=2, column=1, sticky="ew", pady=5, padx=5)

        tk.Label(form_frame, text="Generated Password Vault:", bg="#F3F4F6", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
        self.pass_entry = tk.Entry(form_frame, width=30, font=("Arial", 10, "bold"), fg="#111827")
        self.pass_entry.grid(row=3, column=1, pady=5, padx=5)

        # Operational Control Buttons Layout Action Matrix
        btn_frame = tk.Frame(root, bg="#F3F4F6", pady=10)
        btn_frame.pack(fill="x")

        gen_btn = tk.Button(btn_frame, text="Generate Secure Key", bg="#2563EB", fg="white", font=("Arial", 10, "bold"), padx=10, command=self.generate_secure_password)
        gen_btn.pack(side="left", padx=25)

        save_btn = tk.Button(btn_frame, text="Commit Entry to Vault", bg="#10B981", fg="white", font=("Arial", 10, "bold"), padx=10, command=self.save_credentials)
        save_btn.pack(side="right", padx=25)

        # Bottom Data Viewing Area Logs Container box
        log_label = tk.Label(root, text="Active local storage location: passwords.txt", bg="#E5E7EB", fg="#4B5563", font=("Arial", 9, "italic"), pady=5)
        log_label.pack(fill="x", side="bottom")

    def generate_secure_password(self):
        """Builds strong cryptographic passwords using standard random modules safely."""
        length = self.length_slider.get()
        
        # Combine string sets for strict password criteria pools
        pool = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        
        # Guard clause: ensure password includes minimum diverse structures
        while True:
            password = "".join(self.crypto_rand.choice(pool) for _ in range(length))
            if (any(c.isupper() for c in password) and 
                any(c.islower() for c in password) and 
                any(c.isdigit() for c in password) and 
                any(c in "!@#$%^&*()-_=+" for c in password)):
                break

        # Display the result to the entry slot cleanly
        self.pass_entry.delete(0, tk.END)
        self.pass_entry.insert(0, password)

    def save_credentials(self):
        """Appends validated profile input blocks safely out to local text assets."""
        site = self.site_entry.get().strip()
        user = self.user_entry.get().strip()
        pswd = self.pass_entry.get().strip()

        if not site or not user or not pswd:
            messagebox.showwarning("Incomplete Fields", "Please make sure all input boxes are completely filled out first!")
            return

        try:
            # Open local target file in safe append ('a') operations protocol mode
            with open("passwords.txt", "a", encoding="utf-8") as file:
                file.write(f"Website : {site}\nUsername: {user}\nPassword: {pswd}\n" + "-"*40 + "\n")
            
            # Wipe input entry visuals to confirm successful storage save execution updates
            self.site_entry.delete(0, tk.END)
            self.user_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)
            
            messagebox.showinfo("Vault Success", f"Credentials for '{site}' have been successfully stored in passwords.txt!")
        except Exception as err:
            messagebox.showerror("IO Write Failure Error", f"Unable to commit storage parameters payload to text layer: {err}")

if __name__ == "__main__":
    app_window = tk.Tk()
    app_instance = PasswordManagerApp(app_window)
    app_window.mainloop()
