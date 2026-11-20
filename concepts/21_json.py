import json 

with open("firma.json","r",encoding="utf-8") as datei :
    daten = json.load(datei)

print(daten)


# aufgabe 1 : gesamtgehalt berechnen
gesmtgehalt = 0
for abteilung in daten["abteilungen"] :
    for mitarbeiter in abteilung["mitarbeiter"] :
        gesamtgehalt += mitarbeiter["gehalt"]

print(f"gesamtgehalt: {gesamtgehalt}euro")


# aufgabe 2 : python-spezialisten finden

# aufgabe 3 : gehalt im marketing erhöhen(+10%)

with open("firma_aktualiesieren.json", "w"encoding="utf-8") as ziel:
     json.dump(daten,ziel,ensure_ascii=False, indent=4)