# Aufgabe 5 | Python Boolean Type

## 1. Truthy-Werte
# Gib mit bool() für diese fünf Werte aus, ob sie als True oder False ausgewertet werden:
# den String "Hallo", die Zahl 42, die Kommazahl 3.14, die Liste [1, 2, 3]
# und das Dictionary {"name": "Daniela"}.
# Schreib hinter jede Zeile als Kommentar, was du erwartest, BEVOR du das Programm startest.
# Danach prüfst du, ob du richtig lagst.
print(bool("Hallo"))  
print(bool(42))
print(bool(3.14))      #bei allen kommt True
print(bool([1,2,3]))
print(bool({"name": "Daniela"}))
print()

## 2. Falsy-Werte
# Mach dasselbe für diese Werte: "" (leerer String), 0, 0.0, [] (leere Liste),
# () (leeres Tupel), {} (leeres Dictionary) und None.
# Auch hier: erst raten, dann ausführen.
# Frage an dich: Was haben alle diese Werte gemeinsam?
print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool([]))     #bei allen kommt False
print(bool(()))
print(bool({}))
print(bool(None))
print()

## 3. Der Stolperstein
# Gib bool("0") und bool("False") aus. Das sind Strings, keine Zahl und kein Boolean.
# Überleg vorher: True oder False? Schreib in einen Kommentar, warum das so ist.
# Tipp: Schau dir noch mal an, wann ein String als True ausgewertet wird.
print(bool("0"))        # True
print(bool("False"))    # True
print()

## 4. Truthy/Falsy mit if/else
# Erstelle eine Variable shopping_list mit einer leeren Liste.
# Schreib ein if/else, das "Die Einkaufsliste ist leer" ausgibt, wenn die Liste leer ist,
# und sonst "Die Einkaufsliste hat Einträge".
# Wichtig: Du darfst NICHT len() oder == benutzen. Die Liste selbst ist die Bedingung.
# Danach setzt du in die Liste "Milch" und "Brot" ein und führst das Programm noch mal aus.
shopping_list = []
if shopping_list:
    print("Die Einkaufsliste hat Einträge")
else:
    print("Die Einkaufsliste ist leer")        # Die Einkaufsliste ist leer
print()

## 5. Eigene Prüfung bauen
# Erstelle drei Variablen: username = "", age = 0, favorite_color = "Lila".
# Schreib für jede Variable ein eigenes if/else, das ausgibt, ob ein Wert vorhanden ist
# oder nicht (zum Beispiel "Benutzername fehlt" / "Benutzername vorhanden").
# Überleg vorher, welche der drei Ausgaben "fehlt" sagen wird.
username = ""
age = 0
favorite_color = "lila"

if username:
    print("Benutzername vorhanden")
else:
    print("Benutzername fehlt")     #Benutzername fehlt
print()

if age:
    print("Alter vorhanden")
else:
    print("Alter fehlt")    #Alter fehlt
print()

if favorite_color:
    print("Lieblingsfarbe vorhanden")   #Lieblingsfarbe vorhanden
else:
    print("Lieblingsfarbe fehlt")
print()

## 6. Bonus: Wann hilft Truthy/Falsy, wann nicht?
# Setze age = 0 (ein echtes Alter, zum Beispiel für ein neugeborenes Baby).
# Prüfe mit  if age:  ob ein Alter angegeben wurde. Was passiert?
# Schreib in einen Kommentar, warum das hier zu einem Denkfehler führt
# und was du stattdessen prüfen könntest. (Hinweis: Es gibt einen speziellen Wert,
# der "nichts angegeben" ausdrückt. Er steht in der Falsy-Liste aus Aufgabe 2.)
age = 0
if age:
    print("Alter angegeben")
else:
    print("Alter fehlt")        # Alter fehlt (Denkfehler, 0 ist ein echtes Alter)
print()

age = 0
if age is not None:
    print("Alter angegeben")    # Alter angegeben
else:
    print("Alter fehlt")
print()

age = None
if age is not None:
    print("Alter angegeben")
else:
    print("Alter fehlt")        # Alter fehlt

