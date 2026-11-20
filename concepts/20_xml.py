import xml.etree.ElementTree as ET 

try :
     movies = ET.parse("movies.xml")
except ET.ParseError:
    print("xml kaputt")
    
    
#print(type(movies))

root = movies.getroot()      #root : wurzel, anfangsknoten

# aufgabe 1 : alle filmtitel ausgeben
print("---alle filmtitel---")
for m in root.iter("movie"):
     title = m.find("title").text
     print(title)

#aufgabe 2 : filme ab 2014 ausgeben
print("---filme ab 2014---")
for m in root.iter("movie"):
     year = int(m.find("year").text)
     if year >=2014:
          title = m.find("title").text
          print(f"{title}({year})")

# aufgabe 3 : durchschnittliche bewertung ausgeben
print("---bewertung---")
ratings = []

for m in root.iter("movie"):
     rating_val = float(m.find("rating").text)
     ratings.append(rating_val)

if ratings:
   avarage = sum(ratings) / len(ratings)
   print(f"{avarage:.2f}")


# aufgabe 4 : alle filme von christopher Nolan ausgeben

# aufgabe 5 : alle filme länger als 150 minuten ausgeben

# aufgabe 6 : regisseure ohne duplikate auflisten

# aufgabe 7 : filmtitel nach anfangbuchstaben filtern 

# aufgabe 8 : anzahl der animationfilme ausgeben 
