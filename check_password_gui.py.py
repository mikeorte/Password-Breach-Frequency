import hashlib
import requests
import tkinter as tk
from tkinter import messagebox

def is_password_pwned(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            lines = response.text.splitlines()

        hash_dict = {}
        for line in lines:
            hash_suffix, count = line.split(':')
            hash_dict[hash_suffix] = int(count)

        return hash_dict.get(suffix, 0)

    except requests.RequestException as e:
        messagebox.showerror("Error", f"An error occurred while connecting to the HIBP API: {e}")
        return -1

def check_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Password cannot be empty.")
        return

    pwned_count = is_password_pwned(password)

    if pwned_count == -1:
        return
    elif pwned_count > 0:
        messagebox.showinfo("Result", f"Your password hash has appeared {pwned_count:,} times in known data breaches.")
    else:
        messagebox.showinfo("Result", "Your password hash has not appeared in a known data breach.")

def create_gui():
    root = tk.Tk()
    root.title("Password Pwned Checker")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Enter Password:")
    label.grid(row=0, column=0, pady=5)

    global password_entry
    password_entry = tk.Entry(frame, show='*', width=30)
    password_entry.grid(row=0, column=1, pady=5)

    check_button = tk.Button(frame, text="Check Password", command=check_password)
    check_button.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
