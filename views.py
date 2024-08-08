import tkinter as tk
from tkinter import messagebox
from controllers import UserController

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Library System")
        self.user_controller = UserController()
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Username").grid(row=0, column=0)
        tk.Label(self.root, text="Password").grid(row=1, column=0)

        self.username_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root, show='*')
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0)
        tk.Button(self.root, text="Register", command=self.register).grid(row=2, column=1)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_controller.login(username, password):
            self.create_library_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_controller.register(username, password):
            messagebox.showinfo("Success", "User registered successfully")
        else:
            messagebox.showerror("Error", "User registration failed")

    def create_library_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Virtual Library").pack()
        # Add more library functionality here

if __name__ == "__main__":
    root = tk.Tk()
    gui = LibraryGUI(root)
    root.mainloop()
