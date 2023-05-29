# -*- coding: utf-8 -*-
"""
Created on Mon May 20 20:39:32 2023

@author: debli
"""

import tkinter as tk
import pyshorteners

def shorten_url():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(long_url)
    result_label.config(text="Shortened URL: " + shortened_url)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")
window.geometry("400x200")  # Set the window size
window.configure(bg="black")  # Set the background color of the window

# Create the URL input field
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Create the "Shorten URL" button
button = tk.Button(window, text="Shorten URL", command=shorten_url, bg="yellow", fg="black")
button.pack(pady=5)

# Create the label to display the shortened URL
result_label = tk.Label(window, text="", bg='black', fg='yellow')
result_label.pack(pady=10)

# Run the GUI main loop
window.mainloop()
