import tkinter as tk
from tkinter import messagebox

letters = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plain_text, key):
    cipher_text = ''
    for letter in plain_text:
        if not letter == ' ':
            index = letters.find(letter.lower())
            if index == -1:
                cipher_text += letter
            else:
                new_index = (index + key) % 26
                cipher_text += letters[new_index]
        
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ''
    for letter in cipher_text:
        if not letter == ' ':
            index = letters.find(letter.lower())
            if index == -1:
                plain_text += letter
            else:
                new_index = (index - key) % 26
                plain_text += letters[new_index]
    return plain_text

def process_text(mode):
    text = entry_text.get("1.0", "end-1c")
    try:
        key = int(entry_key.get())
        if mode == 0:
            result_text = encrypt(text, key)
        else:
            result_text = decrypt(text, key)
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result_text)
    except ValueError:
        messagebox.showerror("Error", "Key must be an integer")

# Create the GUI window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

# Create widgets
label_text = tk.Label(root, text="Enter text to process:")
label_text.grid(row=0, column=0, padx=10, pady=10)

entry_text = tk.Text(root, height=5, width=50)
entry_text.grid(row=0, column=1, padx=10, pady=10)

label_key = tk.Label(root, text="Enter key (integer):")
label_key.grid(row=1, column=0, padx=10, pady=10)

entry_key = tk.Entry(root, width=10)
entry_key.grid(row=1, column=1, padx=10, pady=10)

button_encrypt = tk.Button(root, text="Encrypt", command=lambda: process_text(0))
button_encrypt.grid(row=2, column=0, padx=20,pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=lambda: process_text(1))
button_decrypt.grid(row=2, column=2, padx=30,pady=10)

output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main GUI loop
root.mainloop()
