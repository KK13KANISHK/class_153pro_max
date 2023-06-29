# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:44:47 2023

@author: kanis
"""

from tkinter import *
import random
root = Tk()
obj = Class153(root)

class Class153:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        
        self.entry = Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=20)

        self.password_label = Label(self.root, text="Password Entered: ", font=("Arial", 12))
        self.password_label.pack()

        self.generated_password_label = Label(self.root, text="Generated Password: ", font=("Arial", 12))
        self.generated_password_label.pack(pady=20)
        
        self.generate_button = Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        input_password = self.entry.get()
        self.password_label.config(text="Password Entered: " + input_password)

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
        generated_password = ""
        
        for _ in range(10):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            z = random.randint(0, 9)
            generated_password += chars[x] + chars[y].lower() + str(z)
        
        self.generated_password_label.config(text="Generated Password: " + generated_password)



root.mainloop()