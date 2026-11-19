#Aufgabe: Analyse historischer Erdbebendaten
#Themen: CSV-Datei, Dictionary, Funktionen, Tupel, f-Strings, Try-Except
#Entwickeln Sie ein Python-Programm, das globale Erdbebendaten aus einer CSV-Datei einliest, das
#stärkste Erdbeben ermittelt und das Land mit den häufigsten Beben identifiziert.
#Anforderungen:
#Dateiverarbeitung & Fehlerbehandlung:
#• Lesen Sie eine CSV-Datei namens erdbeben.csv mithilfe des csv.reader-Moduls ein.
#• Überspringen Sie die Kopfzeile (Header) der Datei vor der Verarbeitung.
#• Sichern Sie das Programm gegen einen FileNotFoundError ab und geben Sie im
#Fehlerfall eine passende Meldung aus.
#Auswertung des stärksten Erdbebens:
#• Iterieren Sie durch die Datenzeilen (Spalten: Jahr, Land, Region, Magnitude).
#• Ermitteln Sie das Beben mit der höchsten Magnitude.
#• Speichern Sie die Details dieses Bebens (Jahr, Land, Region und Stärke) dynamisch in einem
#Dictionary ab.
#Häufigkeitsanalyse per Hilfsfunktion:
#• Zählen Sie mithilfe eines Dictionaries (land_zaehler), wie oft jedes Land in der Liste
#auftaucht.
#• Schreiben Sie eine separate Funktion finde_max_land(laender_daten), die dieses
#Dictionary auswertet. Die Funktion soll das Land mit den meisten registrierten Beben sowie die
#genaue Anzahl als Tupel zurückgeben.
#Ergebnisausgabe:
#• Geben Sie die Details des stärksten Erdbebens formatiert auf der Konsole aus.
#• Geben Sie direkt darunter aus, welches Land am häufigsten betroffen war und wie viele Beben
#dort gezählt wurden.


############################################################################################################

#LÖSUNG : 


import csv

# Hilfsfunktion: Land mit den meisten Erdbeben finden
def finde_max_land(laender_daten):
    if not laender_daten:
        return None, 0

    max_land = max(laender_daten, key=laender_daten.get)
    max_anzahl = laender_daten[max_land]

    return max_land, max_anzahl


# Dictionary für das stärkste Erdbeben
staerkstes_beben = {
    "jahr": None,
    "land": None,
    "region": None,
    "magnitude": 0
}

# Dictionary zum Zählen der Erdbeben pro Land
land_zaehler = {}

try:
    # CSV-Datei öffnen und einlesen
    with open("erdbeben.csv", "r", encoding="utf-8") as datei:
        reader = csv.reader(datei)

        # Kopfzeile überspringen
        next(reader)

        # Datenzeilen verarbeiten
        for zeile in reader:
            jahr, land, region, magnitude = zeile

            # Magnitude in eine Zahl umwandeln
            magnitude = float(magnitude)

            # Stärkstes Erdbeben ermitteln
            if magnitude > staerkstes_beben["magnitude"]:
                staerkstes_beben = {
                    "jahr": jahr,
                    "land": land,
                    "region": region,
                    "magnitude": magnitude
                }

            # Erdbeben pro Land zählen
            if land in land_zaehler:
                land_zaehler[land] += 1
            else:
                land_zaehler[land] = 1

    # Land mit den meisten Erdbeben ermitteln
    max_land, max_anzahl = finde_max_land(land_zaehler)

    # Ergebnisse ausgeben
    print("\n--- Analyse der Erdbebendaten ---")

    if staerkstes_beben["jahr"] is not None:
        print("\nStärkstes Erdbeben:")
        print(f"Jahr:       {staerkstes_beben['jahr']}")
        print(f"Land:       {staerkstes_beben['land']}")
        print(f"Region:     {staerkstes_beben['region']}")
        print(f"Magnitude:  {staerkstes_beben['magnitude']}")

    if max_land is not None:
        print("\nLand mit den meisten Erdbeben:")
        print(f"Land:       {max_land}")
        print(f"Anzahl:     {max_anzahl} Erdbeben")

    if not land_zaehler:
        print("Die CSV-Datei enthält keine Erdbebendaten.")

except FileNotFoundError:
    print("Fehler: Die Datei 'erdbeben.csv' wurde nicht gefunden.")


    