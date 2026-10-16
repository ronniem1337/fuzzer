import tkinter as tk
from tkinter import ttk
import requests as r
import time

def startLabel():
    output.config(text="Fuzzing...")

def error(e):
    output.config(text=e)

def fuzz():
    urls = []
    startLabel()

    try:
        with open(wordlist.get(),"r") as words:
            for word in words:
                res = r.get(url.get()+word.strip())
                if res.status_code != 404:
                    urls.append(url.get()+word+" --> "+str(res.status_code)+"\n")
            words.close()
        output.config(text=urls)
    except:
        output.config(text="Something went wrong.\nPlease check all inputs.")
root = tk.Tk()

url = tk.Entry(root)
wordlist = tk.Entry(root)
label = tk.Label(root, text="url")
output = tk.Label(root, text="",justify="center", width=50)
label2 = tk.Label(root, text = "wordlist")

root.geometry("400x300")
wordlist.grid(column=0, row=4)
output.grid(column=0,row=6)
label2.grid(column=0, row=3)
label.grid(column=0, row=0)
url.grid(column=0, row=1)

ttk.Button(root, text="FUZZ", command=fuzz).grid(column=0, row=5)
root.mainloop()

