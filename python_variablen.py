# Aufgabe 1 | Python Variablen

# ---------------------------------------------------------------
# 1. Variablen erstellen
# ---------------------------------------------------------------
# Python erkennt den Datentyp selbst, und zwar daran, WIE der Wert geschrieben ist:
#   "Text"  (Anführungszeichen)  -> str   (Zeichenkette)
#   44      (ganze Zahl)         -> int
#   1.65    (Zahl mit Punkt)     -> float (Kommazahl, immer Punkt statt Komma!)
#   True / False                 -> bool

name = "Daniela"
age = 44
height = 1.65

# Tipp zu Namen: Für Variablen- und Funktionsnamen nur a-z, Zahlen und Unterstrich
# nutzen, keine Umlaute oder ß. In Texten (in Anführungszeichen) sind sie kein Problem.

# ---------------------------------------------------------------
# 2. Variablen ausgeben
# ---------------------------------------------------------------
# print() zeigt etwas im Terminal an. Ohne print() sieht man nichts.

print (name)
print (age)
print (height)

# f-String: Das f direkt vor den Anführungszeichen sagt Python:
# "Schau in den Text bei {} nach Variablen und setz ihren Wert ein"
# Ohne f bleibt {name} einfach nur Text

print(f"Hallo {name}")    # Hallo Daniela
print("Hallo {name}")     # Hallo {name}


# ---------------------------------------------------------------
# 3. Datentypen prüfen
# ---------------------------------------------------------------
# type() liefert den Datentyp, print() zeigt ihn an.
# Es zeigt, was wirklich gespeichert ist. Beispiel: age = "44" (mit Anführungszeichen)
# wäre ein str, kein int. Dann würde age + 1 einen Fehler geben.

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))    # <class 'float'>

# ---------------------------------------------------------------
# 4. Umwandeln (Casting)
# ---------------------------------------------------------------
# Python ändert Typen nie von allein, das machen wir mit str(), int() oder float().
# Warum hier nötig? Text und Zahl lassen sich nicht mit + zusammenkleben:
# "ich bin " + 44 gäbe einen Fehler. Erst nach str(age) ist es Text.

age_str = str(age)    # aus der Zahl 44 wird der Text "44"
print("Mein Name ist " + name + " und ich bin " + age_str + " Jahre alt.")

# Alternative Ausgabe mit f-String: Hier braucht man kein str(), weil Python
# die Zahl beim Einsetzen selbst in Text umwandelt.

print(f"Mein Name ist {name} und ich bin {age} Jahre alt.")

# ---------------------------------------------------------------
# 5. Funktionen und globale Variablen
# ---------------------------------------------------------------
# def (von "define") erstellt eine Funktion: ein Block mit Befehlen, der einen Namen
# hat und beliebig oft aufgerufen werden kann, wie ein Rezept.
#   - () hinter dem Namen und der Doppelpunkt am Ende der Zeile sind Pflicht
#   - Die eingerückten Zeilen (4 Leerzeichen) gehören zur Funktion
#   - def legt die Funktion nur an. Ausgeführt wird sie erst beim Aufruf: begruessen()

def begruessen():
    print(f"Hallo {name}!")

begruessen()    # Aufruf. Ohne diese Zeile passiert nichts!

# Globale und lokale Variablen, wie Zettel:
#   - Variable AUSSERHALB einer Funktion = Zettel am schwarzen Brett (global).
#     Jeder darf ihn LESEN, auch die Funktion oben (sie liest name).
#   - Variable INNERHALB einer Funktion = Zettel in der Schublade der Funktion (lokal).
#     Nach der Funktion ist er weg.
#
# Problem: Schreibt man in einer Funktion  message = "neu", legt Python einen NEUEN
# Zettel in der Schublade an. Der am schwarzen Brett bleibt unverändert.
# Mit dem Schlüsselwort global sagt man Python: "Nimm den Zettel am schwarzen Brett":
#
#   message = "alt"
#
#   def aendern():
#       global message
#       message = "neu"
#
#   aendern()
#   print(message)    # neu
#
# Hinweis: Zum bloßen Lesen braucht man global nicht, nur zum Verändern.
# Profis vermeiden global meistens und nutzen stattdessen Funktionen mit return.

# ---------------------------------------------------------------
# Bonus: Globale Variable ändern
# ---------------------------------------------------------------
# Schritt 1: Variable AUSSERHALB der Funktion anlegen (Zettel am schwarzen Brett)
global_message = "Das ist die ursprüngliche Nachricht"

# Schritt 2: Funktion, die die globale Variable verändert
def change_message():
    global global_message    # "Nimm den Zettel am schwarzen Brett, leg keinen neuen an"
    global_message = "Die Nachricht wurde in der Funktion geändert"

# Schritt 3: Vorher ausgeben (noch die ursprüngliche Nachricht)
print(global_message)

# Schritt 4: Funktion aufrufen, erst jetzt wird die Nachricht geändert
change_message()

# Schritt 5: Nachher ausgeben (jetzt die geänderte Nachricht)
print(global_message)

