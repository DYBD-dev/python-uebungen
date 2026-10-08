# Aufgabe 2 | Python Datentypen

## Implizite Typisierung (Python bestimmt den Typ automatisch)
# Variablen definieren
first_name = "Alice"
last_name = "Müller"
age = 25
height = 1.65
is_student = True

# Ausgabe
print("Vorname:", first_name)        # Vorname: Alice
print("Name:", last_name)            # Name: Müller
print("Alter:", age)                 # Alter: 25
print("Größe:", height)              # Größe: 1.65
print("Student/in:", is_student)     # Student/in: True

# Abfrage Typ
print("Der Typ 'Vorname' ist ", type(first_name))   #<class 'str'>
print("Der Typ 'Name' ist ", type(last_name))       #<class 'str'>
print("Der Typ 'Alter' ist ", type(age))            #<class 'int'>
print("Der Typ 'Größe' ist ", type(height))         #<class 'float'>
print("Der Typ 'Student/in' ist", type(True))       #<class 'bool'>

## Typsicherheit bei Operationen
# Folgendes Beispiel führt zu einem Fehler, weil zwischen Text und Zahl weder ein Komma noch ein + steht.
# Entfernen Sie das Kommentarzeichen, um den Fehler anzuzeigen.
#print("Nächstes Jahr wirst du " ((age) + 1) "Jahre alt sein.") # SyntaxError: invalid syntax. Is this intended to be part of the string?

# Richtig (Kommas trennen die Teile, print() wandelt die Zahl selbst in Text um):
print("Nächstes Jahr wirst du ", ((age) + 1), "Jahre alt sein.")
#Alternativ (mit +, dann muss die Zahl mit str() selbst in Text umgewandelt werden):
print("Nächstes Jahr wirst du " + str(age +1), "Jahre alt sein.")

## Explizite Typisierung (Casting-Beispiel: Eingabeaufforderung)
#Die Situation: Wenn ein Programm später etwas von einem Menschen abfragt 
#(mit input()), kommt die Antwort immer als Text an. Auch wenn jemand 30 tippt,
#ist das für Python erst einmal der Text "30" und keine Zahl.

user_input = "30"                                                   # sieht aus wie eine Zahl, ist aber Text
user_age = int(user_input)                                          # jetzt ist es wirklich eine Zahl
print("Nächstes Jahr wirst du", user_age + 1, "Jahre alt sein")     # 31

# Explizite Typisierung (Casting-Beispiele)
x = 10.5
y = int(x)       # Umwandlung in Integer (Nachkommastelle wird abgeschnitten)
z = float(10)    # Umwandlung in Float

print("Integer aus Float:", y)    # 10
print("Float aus Integer:", z)    # 10.0

# Anwendungsbeispiel: Preis mit Mengenangabe (Eingaben kommen als Text)
price_input = "4.50"      # Preis pro Stück, als Text eingegeben
amount_input = "3"        # Anzahl, als Text eingegeben

price = float(price_input)     # Text -> Kommazahl, damit wir rechnen können
amount = int(amount_input)     # Text -> ganze Zahl
total = price * amount         # 13.5

print("Gesamtpreis: " + str(total) + " Euro")    # Zahl -> Text, damit + funktioniert
print("Gerundet auf ganze Euro:", int(total))    # 13 (abgeschnitten)

# Zusätzliches Learning: Runden mit round()
# int() schneidet die Nachkommastellen nur ab, round() rundet wirklich.
print(int(10.7))       # 10 (abgeschnitten)
print(round(10.7))     # 11 (gerundet)

# Achtung bei genau .5: Python rundet zur nächsten geraden Zahl
print(round(2.5))      # 2 (2 ist gerade)
print(round(3.5))      # 4 (4 ist gerade)
print(round(13.5))     # 14 (14 ist gerade)

# Mit einer zweiten Zahl gibst du an, auf wie viele Nachkommastellen gerundet wird
pi = 3.14159
print(round(pi, 2))    # 3.14
print(round(pi, 3))    # 3.142
print(round(pi, 0))    # 3.0 (bleibt ein Float, round(pi) ohne 0 ergibt die Integer-Zahl 3)

