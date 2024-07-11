#                                      Password Generator with Python

# import random
# characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
# length = int(input("Enter Password length"))
# password = ""
# for i in range(length+1):
#     password += random.choice(characters)
# print(password)


# import tkinter as tk
# import string
# import random
# def generate_password():
#     password = []
#     for i in range(5):
#         alpha = random.choice(string.ascii_letters)
#         symbol = random.choice(string.punctuation)
#         numbers = random.choice(string.digits)
#         password.append(alpha)
#         password.append(symbol)
#         password.append(numbers)
#         passwords = " ".join(str(x)for x in password)
#         label.config(text=passwords)
# root = tk.Tk()
# root.geometry("400x300")
# button = tk.Button(root, text="Generate Password", command=generate_password)
# button.grid(row=1, column=1)
# label = tk.Label(root, font=("times", 15, "bold"))
# label.grid(row=4, column=2)
# root.mainloop()



# ADD USER INPUT FUNCTION ASK  PASSWORD LENGTH

import tkinter as tk
import string
import random

def generate_password():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError("Length should be at least 1")
        password = []
        for i in range(length):
            alpha = random.choice(string.ascii_letters)
            symbol = random.choice(string.punctuation)
            numbers = random.choice(string.digits)
            password.append(alpha)
            password.append(symbol)
            password.append(numbers)
        passwords = "".join(password)[:length]
        label.config(text=passwords)
    except ValueError:
        label.config(text="Please enter a valid length")

root = tk.Tk()
root.geometry("400x300")

entry_label = tk.Label(root, text="Enter password length:")
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Generate Password", command=generate_password)
button.grid(row=1, column=1, pady=10)

label = tk.Label(root, font=("times", 15, "bold"))
label.grid(row=4, column=1, pady=10)

root.mainloop()
