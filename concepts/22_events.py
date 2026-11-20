import tkinter as tk # Toolkit Interface

# Plattformübergreifend
# Widgets: Fenster (Tk), Schaltflächen (Buttons), Beschriftungen (Labels)
# Layout-Manager: pack(), grid()

# Eventhandler:
def klick_handler(event):
    aktueller_wert = zaehler.get() + 1
    zaehler.set(aktueller_wert)
    label.config(text=f"Der Button wurde {aktueller_wert} mal geklickt!")

fenster = tk.Tk()
fenster.title("Eventhandler-Übung")
fenster.geometry("300x250")

zaehler = tk.IntVar(value=0)

# Widgets erstellen
label = tk.Label(fenster, text="Der Button wurde noch nicht geklickt.", pady=20)
button = tk.Button(fenster, text="Klick mich")

# Widgets im Fenster anordnen
label.pack()
button.pack()

# Registrierung: Eventhandler an den Button binden
button.bind("<Button-1>", klick_handler)

# Endlossschleife, Eventlistener
fenster.mainloop()
 