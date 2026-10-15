# Aufgabe 7 | Python Listen

## 1. Eine Liste erstellen und ausgeben
# Erstelle eine Liste mit 5 Elementen (zum Beispiel deine Lieblingsfrüchte, Zahlen
# oder irgendwelche Dinge, die du magst).
# Gib die Liste auf dem Bildschirm aus.
dinge_die_ich_mag = ["Lernen", "Musik", "Reisen", "gute Gespräche", "Spiele"]
print(dinge_die_ich_mag)
print()

## 2. Zugriff über Index und negativen Index
# Gib das erste Element, das letzte Element und mindestens ein Element über einen
# negativen Index aus (zum Beispiel my_list[-2]).
print("Ersten, mittleren und letzten Eintrag der Liste ausgeben", 
      dinge_die_ich_mag[0], 
      dinge_die_ich_mag[-3], 
      dinge_die_ich_mag[-1])
print()

# Ergänzung zu 2.
# Der erste Index ist 0, der letzte ist -1. Negative Indizes zählen von hinten (-2 ist der vorletzte).
# Bei 5 Elementen sind die Indizes 0 bis 4 und -1 bis -5 gültig.
# Gibt es den Index nicht (zum Beispiel dinge_die_ich_mag[10]), bricht das Programm
# mit einem IndexError ab.

## 2a. Zusatz: Fehler beim Zugriff vermeiden
# Einen Index, den es vielleicht nicht gibt, prüfen wir vorher mit len().
# Bei 5 Elementen ist 4 der größte gültige Index, deshalb index < len(...).
# Diese Prüfung gilt für Indizes von 0 an, negative Indizes prüft sie nicht.
index = 10
if index < len(dinge_die_ich_mag):
    print(dinge_die_ich_mag[index])
else:
    print("Diesen Index gibt es nicht")      # Diesen Index gibt es nicht
print()


## 3. Eine Liste schneiden (Slicing)
# Gib einen Ausschnitt der Liste aus (zum Beispiel die Elemente von Index 1 bis 3).
# Gib alles vom Anfang bis Index 2 aus und alles von Index 2 bis zum Ende.
print("Index 1 bis 3:", dinge_die_ich_mag[1:4])          # Index 1 bis 3: ['Musik', 'Reisen', 'gute Gespräche']
print("Anfang bis Index 2:", dinge_die_ich_mag[:3])      # Anfang bis Index 2: ['Lernen', 'Musik', 'Reisen']
print("Index 2 bis Ende:", dinge_die_ich_mag[2:])        # Index 2 bis Ende: ['Reisen', 'gute Gespräche', 'Spiele']
print()

# Ergänzung zu 3.
# liste[von:bis]: Der Anfang zählt mit, das Ende nicht. [1:4] sind also Index 1, 2 und 3.
# Fehlt eine Angabe, geht es bis zum Anfang beziehungsweise Ende: [:3] und [2:].
# Slicing verändert die Liste nicht, es liefert eine neue Liste.
# Dieselbe Schreibweise gibt es bei Strings (Aufgabe 4).


## 4. Prüfen, ob ein Element vorkommt
# Prüfe mit dem Schlüsselwort in (zum Beispiel if "apple" in my_list:), ob ein
# bestimmtes Element in der Liste steckt.
# Gib eine Meldung aus, ob das Element gefunden wurde oder nicht.
if "Musik" in dinge_die_ich_mag:
    print("Musik wurde gefunden")         # Musik wurde gefunden
else:
    print("Musik wurde nicht gefunden")

if "Sport" in dinge_die_ich_mag:
    print("Sport wurde gefunden")
else:
    print("Sport wurde nicht gefunden")   # Sport wurde nicht gefunden 😅
print()

# Ergänzung zu 4.
# Worauf du achten musst:
# 1. Der ganze Eintrag muss passen. "gute" in dinge_die_ich_mag ergibt False, obwohl
#    "gute Gespräche" in der Liste steckt. Bei Listen wird jedes Element als Ganzes verglichen.
#    Bei einem String wäre es anders, dort sucht "in" auch Teile ("gute" in "gute Gespräche" ist True).
# 2. Groß- und Kleinschreibung zählt. "musik" in dinge_die_ich_mag ergibt False.


## 5. Elemente hinzufügen
# Füge mit append() ein neues Element am Ende der Liste hinzu.
# Füge mit insert() ein Element an einer bestimmten Stelle (Index) ein.
dinge_die_ich_mag.append("Lesen")
print("Nach append:", dinge_die_ich_mag)      # Nach append: ['Lernen', 'Musik', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']

dinge_die_ich_mag.insert(1, "Kochen")
print("Nach insert:", dinge_die_ich_mag)      # Nach insert: ['Lernen', 'Kochen', 'Musik', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']
print()

# Ergänzung zu 5.
# Wichtiger Unterschied zu Strings:
# Bei Strings schreibt man bio = bio.strip(), weil sich Strings nicht verändern lassen und das
# Ergebnis neu gespeichert werden muss. Bei Listen ändern append() und insert() die Liste direkt.
# Falsch wäre: dinge_die_ich_mag = dinge_die_ich_mag.append("Lesen"). append() gibt nichts
# zurück (None), die Liste wäre danach weg.
# Ab hier arbeiten alle weiteren Teile mit der veränderten Liste (7 Elemente).


## 6. Elemente ändern
# Ändere den Wert eines bestimmten Elements über seinen Index.
# Ändere mehrere Elemente auf einmal, indem du einem Ausschnitt etwas zuweist
# (zum Beispiel my_list[1:3] = ["neu1", "neu2"]).
dinge_die_ich_mag[0] = "Programmieren"
print("Index 0 geändert:", dinge_die_ich_mag)      # Index 0 geändert: ['Programmieren', 'Kochen', 'Musik', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']

dinge_die_ich_mag[1:3] = ["Tanzen", "Singen"]
print("Index 1 und 2 geändert:", dinge_die_ich_mag)      # Index 1 und 2 geändert: ['Programmieren', 'Tanzen', 'Singen', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']
print()

# Ergänzung zu 6.
# Steht dinge_die_ich_mag[0] in print() oder rechts vom =, wird gelesen.
# Steht es links vom =, wird geschrieben.
# Beim Slice-Zuweisen muss die neue Liste nicht gleich lang sein: Mit mehr oder weniger
# Einträgen wird die Liste länger oder kürzer. Bei einem einzelnen Index wird immer
# genau ein Element ersetzt.



## 7. Elemente entfernen
# Entferne ein bestimmtes Element über seinen Wert mit remove().
# Entferne ein Element an einem bestimmten Index mit pop().
# Leere die gesamte Liste mit clear() (oder zeige es an einer temporären Liste).
dinge_die_ich_mag.remove("Singen")
print("Nach remove:", dinge_die_ich_mag)      # Nach remove: ['Programmieren', 'Tanzen', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']

entfernt = dinge_die_ich_mag.pop(1)
print("Mit pop entfernt:", entfernt)          # Mit pop entfernt: Tanzen
print("Nach pop:", dinge_die_ich_mag)         # Nach pop: ['Programmieren', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']

temp_liste = ["a", "b", "c"]
temp_liste.clear()
print("Nach clear:", temp_liste)              # Nach clear: []
print()

# Ergänzung zu 7.
# Nach remove() rückt alles eine Stelle nach vorne.
# Kommt der Wert mehrfach vor, fliegt nur der erste raus.
# remove() nimmt den Wert, pop() nimmt die Position.
# pop() gibt das entfernte Element zurück, ohne Angabe entfernt es das letzte.
# clear() leert die ganze Liste. Hier an einer extra Liste gezeigt,
# damit dinge_die_ich_mag für die nächsten Teile gefüllt bleibt.


## 7a. Zusatz: Fehler beim Entfernen vermeiden
# remove() mit einem Wert, der nicht in der Liste steckt, gibt einen ValueError.
# Deshalb prüfen wir vorher mit "in", ob der Wert vorkommt.
if "Sport" in dinge_die_ich_mag:
    dinge_die_ich_mag.remove("Sport")
else:
    print("Sport ist nicht in der Liste, deshalb wird nichts entfernt")      # Sport ist nicht in der Liste, deshalb wird nichts entfernt
print()


## 8. Eine Liste kopieren
# Erstelle mit list.copy() oder Slicing ([:]) eine Kopie deiner Liste.
# Ändere danach die ursprüngliche Liste und gib beide Listen aus,
# um zu prüfen, dass sie unabhängig voneinander sind.
kopie = dinge_die_ich_mag.copy()
kopie_slice = dinge_die_ich_mag[:]
dinge_die_ich_mag.append("Wandern")
print("Original:", dinge_die_ich_mag)         # Original: ['Programmieren', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen', 'Wandern']
print("Kopie mit copy():", kopie)             # Kopie mit copy(): ['Programmieren', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']
print("Kopie mit [:]:", kopie_slice)          # Kopie mit [:]: ['Programmieren', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen']
print()

# Ergänzung zu 8.
# copy() und [:] legen eine neue, eigene Liste an.
# kopie = dinge_die_ich_mag wäre keine Kopie, sondern nur ein zweiter Name für dieselbe Liste
# (siehe Operatoren, Teil 5). Eine Änderung am Original würde dann auch in kopie auftauchen.
# Prüfen lässt sich das mit is: kopie is dinge_die_ich_mag ergibt False.


## 9. Listen verbinden und erweitern
# Erstelle zwei getrennte Listen und verbinde sie auf zwei Arten:
# mit dem Operator + (zum Beispiel list_a + list_b)
# und mit extend() (zum Beispiel list_a.extend(list_b)).
list_a = ["Tee", "Kaffee"]
list_b = ["Kakao", "Saft"]

zusammen = list_a + list_b
print("Mit +:", zusammen)                     # Mit +: ['Tee', 'Kaffee', 'Kakao', 'Saft']
print("list_a danach:", list_a)               # list_a danach: ['Tee', 'Kaffee']

list_a.extend(list_b)
print("Mit extend:", list_a)                  # Mit extend: ['Tee', 'Kaffee', 'Kakao', 'Saft']
print("list_b danach:", list_b)               # list_b danach: ['Kakao', 'Saft']
print()

# Ergänzung zu 9.
# list_a + list_b baut eine neue Liste und verändert keine der beiden. Das Ergebnis muss
# in einer Variablen gespeichert werden (hier: zusammen).
# list_a.extend(list_b) hängt die Elemente von list_b hinten an list_a an und verändert list_a.
# Wie bei append() schreibt man kein list_a = davor.
# append() hängt ein Element an. list_a.append(list_b) würde die ganze Liste als ein Element
# einfügen: ['Tee', 'Kaffee', ['Kakao', 'Saft']] (verschachtelte Liste).


## 10. Sortieren und umkehren
# Sortiere die Liste mit sort().
# Kehre die sortierte Liste mit reverse() um.
# (Optional) Erzeuge mit sorted() eine neue sortierte Liste, ohne die ursprüngliche zu verändern.
list_a.sort()
print("Sortiert:", list_a)                    # Sortiert: ['Kaffee', 'Kakao', 'Saft', 'Tee']

list_a.reverse()
print("Umgekehrt:", list_a)                   # Umgekehrt: ['Tee', 'Saft', 'Kakao', 'Kaffee']

neu_sortiert = sorted(list_a)
print("Neu mit sorted():", neu_sortiert)      # Neu mit sorted(): ['Kaffee', 'Kakao', 'Saft', 'Tee']
print("list_a bleibt:", list_a)               # list_a bleibt: ['Tee', 'Saft', 'Kakao', 'Kaffee']
print()

# Ergänzung zu 10.
# sort() und reverse() verändern die Liste direkt und geben nichts zurück (kein list_a = davor).
# reverse() sortiert nicht, es dreht nur die aktuelle Reihenfolge um.
# sorted(list_a) baut eine neue sortierte Liste und lässt list_a unverändert. Das Ergebnis
# muss in einer Variablen gespeichert werden (hier: neu_sortiert).
# Achtung bei Texten: Python sortiert alle Großbuchstaben vor allen Kleinbuchstaben.
# Aus ["gute Gespräche", "Wandern"] wird beim Sortieren ["Wandern", "gute Gespräche"].


## 11. Zählen und Position finden
# Finde mit count() heraus, wie oft ein bestimmter Wert in der Liste vorkommt.
# Finde mit index() die Position eines bestimmten Werts in der Liste.
farben = ["blau", "rot", "blau", "grün", "blau"]
print("Wie oft blau:", farben.count("blau"))          # Wie oft blau: 3
print("Wie oft gelb:", farben.count("gelb"))          # Wie oft gelb: 0
print("Position von grün:", farben.index("grün"))     # Position von grün: 3
print("Position von blau:", farben.index("blau"))     # Position von blau: 0
print()

# Ergänzung zu 11.
# count() zählt, wie oft ein Wert vorkommt. Kommt er nicht vor, ist das Ergebnis 0 (kein Fehler).
# index() gibt die Position des ersten Treffers zurück. "blau" steht an Index 0, 2 und 4,
# index() liefert deshalb 0.
# Kommt der Wert gar nicht vor, gibt index() einen ValueError. Vorher mit in prüfen, wie bei 7a.
# Beide Methoden verändern die Liste nicht.


## 12. List Comprehension (Bonus)
# Erstelle eine neue Liste, die deine bestehende Liste umwandelt oder filtert
# (zum Beispiel Strings in Großbuchstaben umwandeln, wenn sie eine Bedingung erfüllen).
# Nutze dafür die Schreibweise [Ausdruck for item in my_list if Bedingung].
lange_dinge = [ding.upper() for ding in dinge_die_ich_mag if len(ding) > 6]
print("Lange Einträge in Großbuchstaben:", lange_dinge)     # Lange Einträge in Großbuchstaben: ['PROGRAMMIEREN', 'GUTE GESPRÄCHE', 'WANDERN']
print("Original bleibt:", dinge_die_ich_mag)                # Original bleibt: ['Programmieren', 'Reisen', 'gute Gespräche', 'Spiele', 'Lesen', 'Wandern']
print()

# Ergänzung zu 12.
# Aufbau: [Ausdruck for item in liste if Bedingung]
# Python geht jedes Element der Liste durch (for ding in dinge_die_ich_mag), prüft die Bedingung
# (if len(ding) > 6) und packt nur die passenden Elemente in die neue Liste, und zwar in der Form,
# die der Ausdruck vorne vorgibt (ding.upper()).
# Dasselbe als normale Schleife:
#   lange_dinge = []
#   for ding in dinge_die_ich_mag:
#       if len(ding) > 6:
#           lange_dinge.append(ding.upper())
# Die Originalliste wird nicht verändert, es entsteht immer eine neue Liste.
# Das "if" am Ende kann man weglassen, dann werden alle Elemente umgewandelt.

