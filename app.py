import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

app = tk.Tk()

app.title("Поисковая строка")
app.configure(background="#d2e8d1")
style = ttk.Style()
style.configure("Label", background="#d2e8d1", font="20")
style.configure("G.TRadiobutton", background="#d2e8d1")

search_label = ttk.Label(app, text="Введите поисковый запрос", style="Label")
search_label.grid(row=1, column=0)

search_field = ttk.Entry(app, width=50)
search_field.grid(row=1, column=1)

search_engine = IntVar()
search_engine.set(1)

def search():
    if search_field.get().strip() != "":
        if search_engine.get() == 1:
            webbrowser.open("https://www.google.com/search?q=" + search_field.get())
        elif search_engine.get() == 2:
            webbrowser.open("https://yandex.ru/search/?text=" + search_field.get())


def searchBtn():
    search()


def searchEnt(event):
    search()


google_rad = ttk.Radiobutton(app, text='Искать в Google', variable=search_engine, value=1, style="G.TRadiobutton")
google_rad.grid(row=2, column=1, sticky=W)
yandex_rad = ttk.Radiobutton(app, text='Искать в Яндекс', variable=search_engine, value=2, style="G.TRadiobutton")
yandex_rad.grid(row=2, column=1, sticky=E)


search_button = ttk.Button(app, width=15, text="Поехали", command=searchBtn)
search_button.grid(row=1, column=2)

search_field.bind("<Return>", searchEnt)
search_field.focus()

app.mainloop()