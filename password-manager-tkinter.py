from tkinter import *
from tkinter import messagebox
import secrets


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
email = "abc@example.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, 'end')
    password_entry.focus()
    # Generate a random string with 10 characters
    random_string = secrets.token_hex(5)
    password_entry.insert(0, random_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    web = website_entry.get()
    user_email = email_entry.get()
    password = password_entry.get()

    if not len(web) or not len(user_email) or not len(password):
        messagebox.showinfo(title="Error", message="You have left one or more fields empty. Please fill all fields.")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are your details.\nEmail: {user_email} \nPassword: {password}")
        if is_ok:
            with open('Day-29/data.txt', 'a') as f:
                f.write(f'{web} | {user_email} | {password}')
                f.write('\n')
                f.close()
                website_entry.delete(0,'end')
                email_entry.delete(0,'end')
                password_entry.delete(0,'end')
                website_entry.focus()
                email_entry.insert(0,email)
            messagebox.showinfo(title="Success", message="Password is saved.")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=20, bg=YELLOW)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, email)

password = Label(text="Password: ")
password.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=add_password)
add_btn.grid(row=4, column=1)


window.mainloop()