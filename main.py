# ------------------------ IMPORTS --------------------------------------------
import tkinter as tk
import random
from tkinter import messagebox
import pyperclip

# ------------------------ GENERATE PASSWORD ----------------------------------
def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()+"

    pass_letters = [random.choice(letters) for _ in range(random.randint(6, 8))]
    pass_upper = [random.choice(upper) for _ in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(1, 3))]
    pass_special_characters = [random.choice(special_characters) for _ in range(random.randint(1, 2))]

    pass_list = pass_letters + pass_numbers + pass_special_characters + pass_upper
    random.shuffle(pass_list)
    password_txt = "".join(pass_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_txt)
    # messagebox to copy password to clipboard
    ask_clip = messagebox.askyesno("Copy?", f"Copy password to clipboard?")
    if ask_clip == True:
        pyperclip.copy(password_txt)
        messagebox.showinfo("Copy that!", f"Password copied to clipboard.")


# ------------------------ SAVE PASSWORD --------------------------------------
def save_password():
    site_get = website_entry.get()
    username_get = username_entry.get()
    password_get = password_entry.get()

    if site_get == "" or username_get == "" or password_get == "":
        messagebox.showerror("Yikes", "Please fill in all fields")
    else:
        confirm = messagebox.askokcancel(title="Good to go?", message=f"Site: {site_get}\nUsername: {username_get}\nPassword: {password_get}\n\nConfirm?")
        if confirm == True:
            with open("password.txt", "a") as passwords:
                passwords.write(f"{site_get} | {username_get} | {password_get}\n")
                website_entry.delete(0, tk.END)
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                messagebox.showinfo("Saved", "Password Saved")


# ------------------------ UI SETUP -------------------------------------------
window = tk.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg="white")

key_image = tk.PhotoImage(file="key.png")
# Key icon ref: <a href="https://www.flaticon.com/free-icons/key" title="key icons">Key icons created by Freepik -
#               Flaticon</a>


canvas = tk.Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(80, 100, image=key_image,anchor="center")
canvas.grid(row=0, column=1, padx=20, pady=20, columnspan=2)

website = tk.Label(text="Website:",  bg="white")
website.grid(row=1, column=0,)
username = tk.Label(text="Username:",  bg="white")
username.grid(row=2, column=0)
password = tk.Label(text="Password:", bg="white")
password.grid(row=3, column=0)

website_entry = tk.Entry(width=53,bg="white")
website_entry.grid(row=1, column=1, columnspan=2)

username_entry = tk.Entry(width=53,bg="white")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=34,bg="white")
password_entry.grid(row=3, column=1)

generate_password_button = tk.Button(relief="ridge", text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(relief="ridge",text="Add", width=45, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()