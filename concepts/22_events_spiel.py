import tkinter as tk
import random

def bewege_ziel():
    x = random.randint(20,380)
    y = random.randint(20,380)
    canvas.coords(ziel, x - 15, y - 15, x+ 15,y + 15 )

def treffer(event):
    aktuelle_punkte = punkte.get() + 1
    punkte.set(aktuelle_punkte)
    bewege_ziel()

# hauptfenster erstellen
fenster=tk.Tk()
fenster.geometry("400x400")

# tkinter - variablen für den spielzustand
punkte = tk.IntVar(value=0)
restzeit = tk.IntVar(value=20)

# spielfläche erstellen(canvas)
canvas = tk.Canvas(fenster, bg="lightblue")
canvas.pack(fill=tk.BOTH, expand=True)

ziel = canvas.create_oval(185,185,215,215,fill="red")
canvas.tag_bind(ziel, "<Button-1>", treffer)


fenster.mainloop()