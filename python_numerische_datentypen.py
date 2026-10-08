# Aufgabe 3 | Python numerische Datentypen

# Importieren von dem Modul random
import random

# Integer (ganze Zahl)
int_value1 = 10
int_value2 = -5
int_value3 = 0

# Ausgaben
print("Beispiele Integer")                                          #Beispiele Integer
print("Positiver Integer:", int_value1, "Typ:", type(int_value1))   #Positiver Integer: 10 Typ: <class 'int'>
print("Negativer Integer:", int_value2, "Typ:", type(int_value2))   #Negativer Integer: -5 Typ: <class 'int'>
print("Null:", int_value3, "Typ:", type(int_value3))                #Null: 0 Typ: <class 'int'>

# Floating (Dezimalzahl)
float_value1 = 3.14
float_value2 = -0.5
float_value3 = 10.0

# Ausgaben
print()                                                                     #Erzeugt eine Leerzeile
print("\nBeispiele Float")                                                  #Beispiele Float, \n erzeugt auch eine Leerzeile (zusammen mit print() also zwei)
print("Positiver Float:", float_value1, "Typ:", type(float_value1))         #Positiver Float: 3.14 Typ: <class 'float'>
print("Negativer Float:", float_value2, "Typ:", type(float_value2))         #Negativer Float: -0.5 Typ: <class 'float'>
print("Ganze Zahl mit Komma:", float_value3, "Typ:", type(float_value3))    #Ganze Zahl mit Komma: 10.0 Typ: <class 'float'>

# Komplexe Zahlen
complex_value1 = 2 + 3j
complex_value2 = -1 + 4j
complex_value3 = 0 + 1j

# Ausgaben
print()
print("Beispiele komplexe Zahlen")                                          #Beispiele komplexe Zahlen
print("Komplexe Zahl 1:", complex_value1, "Typ:", type(complex_value1))     #Komplexe Zahl 1: (2+3j) Typ: <class 'complex'>
print("Komplexe Zahl 2:", complex_value2, "Typ:", type(complex_value2))     #Komplexe Zahl 2: (-1+4j) Typ: <class 'complex'>
print("Komplexe Zahl 3:", complex_value3, "Typ:", type(complex_value3))     #Komplexe Zahl 3: 1j Typ: <class 'complex'>

# Zugriff auf den Realteil und den Imaginärteil einer komplexen Zahl
# .real liefert den Realteil, .imag den Imaginärteil (ohne das j).
# Beide Teile sind immer Kommazahlen, deshalb 2.0 statt 2.
print()
print("Zugriff auf den Real- und Imaginärteil")                                                                  #Zugriff auf den Real- und Imaginärteil
print("Der reale Teil von", complex_value1, "ist", complex_value1.real)                                          #Der reale Teil von (2+3j) ist 2.0
print("Der imaginäre Teil von", complex_value1, "ist", complex_value1.imag)                                      #Der imaginäre Teil von (2+3j) ist 3.0
print("Bei dem Beispiel 'Komplexe Zahl 3' (0 + 1j) haben wir mit", complex_value3.imag, "nur den imaginären Teil.")   #Bei dem Beispiel 'Komplexe Zahl 3' (0 + 1j) haben wir mit 1.0 nur den imaginären Teil.

# Zufallsmodul
# Die Zufallszahlen ändern sich bei jedem Start. Die Zahlen in den
# Kommentaren sind nur Beispiele.
print()
print("Zufallsmodul: 🎲")                                                #Zufallsmodul: 🎲

# Eine zufällige ganze Zahl zwischen 1 und 10 generieren
random_int = random.randint(1, 10)
print("Zufällige Zahl zwischen 1 und 10:", random_int)                  #Zufällige Zahl zwischen 1 und 10: 7

# Eine zufällige Dezimalzahl zwischen 0.0 und 1.0 generieren
random_float = random.random()
print("Zufällige Dezimalzahl zwischen 0.0 und 1.0:", random_float)      #Zufällige Dezimalzahl zwischen 0.0 und 1.0: 0.7382914653

# Zufällige Zahl auf 2 Nachkommastellen runden
print("Gerundet:", round(random_float, 2))                              #Gerundet: 0.74

# Alternativ mit f. Das f vor den Anführungszeichen erlaubt dir,
# Variablen in geschweifte Klammern zu setzen.
# Das :.2f bedeutet: "als Kommazahl mit 2 Nachkommastellen"
print(f"Gerundet: {random_float:.2f}")                                  #Gerundet: 0.74

# Unterschied zwischen den beiden Wegen: round(zahl, 2)
# ändert die Zahl selbst. Du kannst mit dem gerundeten
# Wert danach weiterrechnen.
# :.2f ändert nur die Anzeige. Die Zahl dahinter bleibt unverändert.

# Eine zufällige Dezimalzahl zwischen zwei Werten generieren (hier 5 und 10)
random_uniform = random.uniform(5, 10)
print("Zufällige Dezimalzahl zwischen 5 und 10:", random_uniform)       #Zufällige Dezimalzahl zwischen 5 und 10: 8.274619305

# Einen Würfelwurf simulieren (ganze Zahl zwischen 1 und 6)
dice_roll = random.randint(1, 6)
print("Würfelwurf:", dice_roll)                                         #Würfelwurf: 4
