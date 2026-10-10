# Aufgabe 4 | Python Texttypen

## 1. Strings erstellen
# Erstelle zwei Strings: first_name und last_name mit deinem Vor- und Nachnamen.
first_name = "Daniela"
last_name = "Torunlar"
age = 45
print("Vorname: ", first_name)        # Vorname:  Daniela
print("Nachname: ", last_name)        # Nachname:  Torunlar
print()

# Erstelle einen mehrzeiligen String namens bio, der dich in zwei Sätzen beschreibt.
# Dreifache Anführungszeichen erlauben Zeilenumbrüche im String. Die Leerzeichen
# am Anfang und Ende sind Absicht, damit wir sie später mit strip() entfernen können.
bio = """  Ich lerne gerade Python und
das ist ein mehrzeiliger String.  """
print("Ausgabe Mehrzeilig (mit überflüssigen Leerzeichen (für später)): ", bio)
# Ausgabe: Ausgabe Mehrzeilig (mit überflüssigen Leerzeichen (für später)):    Ich lerne gerade Python und
#          das ist ein mehrzeiliger String.
print()

## 2. Zeichen ansprechen und Strings schneiden (Slicing)
# Gib das erste Zeichen von first_name und das letzte Zeichen von last_name aus.
print("Erstes Zeichen Vorname: ", first_name[0])        # Erstes Zeichen Vorname:  D
print("Letztes Zeichen Nachname: ", last_name[-1])      # Letztes Zeichen Nachname:  r
print()

# Schneide "bio" so zu, dass nur die ersten 10 Zeichen ausgegeben werden.
print("Ausgabe erste 10 Zeichen: ", bio[0:10])        # Ausgabe erste 10 Zeichen:    Ich lern
# Das Zählen beginnt bei 0, das Ende (10) zählt nicht mehr mit: es werden die Positionen 0 bis 9 ausgegeben.
# Kürzer geht auch bio[:10]. Die ersten zwei Zeichen sind Leerzeichen aus dem bio-Text.
print()

## 3. Durch einen String iterieren
# Gib mit einer for-Schleife jedes Zeichen von first_name in einer neuen Zeile aus.
# Die Einrückung zeigt, was zur Schleife gehört. Pro Buchstabe läuft die Schleife einmal.
for char in first_name:
    print("Ausgabe jedes Buchstabens von Vorname einzeln und untereinander: ", char)
# Ausgabe: sieben Zeilen, jeweils mit dem Text davor und dann D, a, n, i, e, l, a
print()

## 4. Länge eines Strings
# Gib die Länge von "bio" mit der Funktion len() aus.
# len() zählt alle Zeichen, auch Leerzeichen und den Zeilenumbruch.
print('Länge von "bio" ausgeben: ', len(bio))        # Länge von "bio" ausgeben:  64
print()

## 5. Teilstrings prüfen
# Prüfe, ob das Wort "Python" in bio vorkommt, und gib das Ergebnis aus.
print('Kommt das Wort Python in "bio" vor?', "Python" in bio)        # Kommt das Wort Python in "bio" vor? True
print()

# Prüfe, ob das Wort "Java" nicht in bio vorkommt, und gib das Ergebnis aus.
# Mit "not in" prüft Python das Gegenteil von "in": True heißt "Java kommt nicht vor".
# Zum Vergleich: "Java" in bio ergäbe False.
print('Kommt das Wort Java nicht in "bio" vor? ', "Java" not in bio)        # Kommt das Wort Java nicht in "bio" vor?  True
print()

## 6. Strings verändern
# Wandle first_name in Großbuchstaben und last_name in Kleinbuchstaben um.
print("Vorname in Großbuchstaben: ", first_name.upper())          # Vorname in Großbuchstaben:  DANIELA
print("Nachname in Kleinbuchstaben: ", last_name.lower())        # Nachname in Kleinbuchstaben:  torunlar
print()

# Entferne überflüssige Leerzeichen in bio und ersetze jedes "Python" durch "coding".
# Zwei Methoden werden hintereinander mit einem Punkt verkettet und von links nach rechts ausgeführt:
# Erst entfernt strip() die Leerzeichen am Rand und gibt einen neuen String zurück,
# auf diesem neuen String ersetzt dann replace() "Python" durch "coding".
print('Ersetze jedes Python in "bio" durch coding und entferne überflüssige Leerzeichen:' +  bio.strip().replace("Python", "coding"))
# Ausgabe: Ersetze jedes Python in "bio" durch coding und entferne überflüssige Leerzeichen: Ich lerne gerade coding und
#          das ist ein mehrzeiliger String.
print()

# Teile bio in eine Liste von Wörtern auf und gib das Ergebnis aus.
# split() erwartet nur das Trennzeichen (hier das Leerzeichen), nicht die Wörter selbst.
# Falsch wäre: bio.split("Ich", "lerne", "gerade", "Python") ergibt TypeError
print('Der Satz in "bio" als Liste:', bio.split(" "))
# Ausgabe: Der Satz in 'bio' als Liste:  ['', '', 'Ich', 'lerne', 'gerade', 'Python', 'und\ndas', 'ist', 'ein', 'mehrzeiliger', 'String.', '', '']
# Die leeren '' kommen von den Leerzeichen am Rand, 'und\ndas' vom Zeilenumbruch.
# bio.split() ohne Klammerinhalt trennt an jedem Leerraum und lässt die leeren Einträge weg.
print()

## 7. Strings verknüpfen
# Verbinde first_name und last_name zu einem String full_name, mit einem Leerzeichen dazwischen.
# Gib den vollständigen Namen aus.
# Das Komma in print() trennt zwei Werte und setzt dazwischen selbst ein Leerzeichen.
print("Strings verknüpft (Vollständiger Name): ", first_name, last_name)             # Strings verknüpft (Vollständiger Name):  Daniela Torunlar
# Mit + werden Strings direkt aneinandergehängt, das Leerzeichen muss man selbst mitgeben.
print("Strings verknüpft (Vollständiger Name): ", last_name + ", " + first_name)    # Strings verknüpft (Vollständiger Name):  Torunlar, Daniela
print()

## 8. String-Formatierung
# Gib mit einem f-String aus:
# "Hallo mein Name ist {full_name} und ich liebe Python!"
# full_name entsteht mit + aus Vorname, Leerzeichen und Nachname.
full_name = first_name + " " + last_name
# Das f steht direkt vor dem Anführungszeichen, ohne Klammer. Variablen in {} werden eingesetzt.
print(f"Hallo mein Name ist {full_name} und ich liebe Python!")        # Hallo mein Name ist Daniela Torunlar und ich liebe Python!
print()

# Gib mit der Methode format() aus:
# "Mein Vorname ist {} und ich bin {} Jahre jung."
# Die {} sind Platzhalter für Vorname und dein Alter.
# format() hängt mit einem Punkt direkt hinter dem String, nicht als eigene Funktion davor.
# Mit benannten Platzhaltern: {name} wird durch name=... ersetzt.
print("Mein Vorname lautet {name} und ich bin {age} Jahre jung.".format(name=first_name, age=age))    # Mein Vorname lautet Daniela und ich bin 45 Jahre jung.

# Mit leeren Platzhaltern: die Werte werden der Reihe nach eingesetzt, ohne Namen.
print("Mein Vorname lautet: {} und ich bin {} Jahre jung.".format(first_name, age))                   # Mein Vorname lautet: Daniela und ich bin 45 Jahre jung.
print()

## 9. Sonderzeichen maskieren (Escape)
# Erstelle einen String, der ein doppeltes und ein einfaches Anführungszeichen enthält.
# Beispiel: Er sagt: "Python's Syntax ist super einfach!"
# Der Backslash \ vor einem " macht es zum normalen Text. Das ' braucht hier keinen,
# weil der String selbst in doppelten Anführungszeichen steht.
print("Er sagt: \"Python's Syntax ist super einfach!\"")        # Er sagt: "Python's Syntax ist super einfach!"
print()

## Bonus
# Gib "bio" zentriert innerhalb von 50 Zeichen aus (String-Methode).
# bio ist 64 Zeichen lang, also länger als 50. Dann lässt center() den Text unverändert.
print(bio.center(50))
# Ausgabe:   Ich lerne gerade Python und
#          das ist ein mehrzeiliger String.
print()

# Mit einem Füllzeichen als zweiter Angabe sieht man, wie center() arbeitet.
print(first_name.center(50, "-"))        # ---------------------Daniela----------------------
print()

# Zähle, wie oft der Buchstabe "a" in first_name vorkommt (hier statt in full_name).
# count() unterscheidet Groß- und Kleinschreibung. Gezählt werden nur kleine "a".
print(first_name.count("a"))        # 2
