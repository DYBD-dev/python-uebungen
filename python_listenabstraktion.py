# Aufgabe 8 | Python Listenabstraktion (List Comprehension)

## 1. Zahlen quadrieren
# Erstelle eine Liste mit den Quadraten der Zahlen von 1 bis 5.
# Mach es zuerst mit einer normalen for-Schleife und dann mit einer List Comprehension.
quadrate = []
for zahl in range(1, 6):
    quadrate.append(zahl * zahl)
print("Mit Schleife:", quadrate)                            # Mit Schleife: [1, 4, 9, 16, 25]

quadrate_kurz = [zahl * zahl for zahl in range(1, 6)]
print("Mit List Comprehension:", quadrate_kurz)             # Mit List Comprehension: [1, 4, 9, 16, 25]
print()

# Ergänzung zu 1.
# Aufbau: [Ausdruck for item in iterierbares_objekt]
# Vorne steht, was in die neue Liste kommt (zahl * zahl), dahinter, woher die Elemente kommen
# (for zahl in range(1, 6)). Die eckigen Klammern sagen Python: "Das Ergebnis ist eine Liste."
# Die leere Liste am Anfang und das append() fallen weg, das erledigt die List Comprehension selbst.
# range(1, 6) geht von 1 bis 5, die 6 gehört nicht mehr dazu.


## 2. Texte in Großbuchstaben umwandeln
# Erstelle aus einer Liste mit Namen eine neue Liste, in der alle Namen in Großbuchstaben stehen.
namen = ["anna", "ben", "clara", "david"]
namen_gross = [name.upper() for name in namen]
print("Original:", namen)                                   # Original: ['anna', 'ben', 'clara', 'david']
print("Großbuchstaben:", namen_gross)                       # Großbuchstaben: ['ANNA', 'BEN', 'CLARA', 'DAVID']
print()

# Ergänzung zu 2.
# Der Ausdruck vorne darf auch eine Methode sein (name.upper()), nicht nur eine Rechnung.
# upper() verändert den Text nicht, sondern gibt einen neuen zurück (Strings sind unveränderbar).
# Auch die Originalliste bleibt unverändert, es entsteht immer eine neue Liste.
# Der Name nach "for" (hier name) ist frei wählbar, ein sprechender Name ist aber leichter zu lesen.


## 3. Filtern mit if
# Erstelle eine Liste mit allen geraden Zahlen von 1 bis 10.
# Eine Zahl ist gerade, wenn beim Teilen durch 2 kein Rest bleibt (zahl % 2 == 0).
gerade_zahlen = [zahl for zahl in range(1, 11) if zahl % 2 == 0]
print("Gerade Zahlen:", gerade_zahlen)                      # Gerade Zahlen: [2, 4, 6, 8, 10]
print()

# Ergänzung zu 3.
# Das "if" steht ganz hinten und wirkt wie ein Filter: Nur Elemente, bei denen die Bedingung
# True ergibt, kommen in die neue Liste. Die anderen werden einfach übersprungen.
# Der Ausdruck vorne ist hier nur zahl, die Zahlen werden also nicht verändert, nur ausgewählt.
# Dasselbe als normale Schleife:
#   gerade_zahlen = []
#   for zahl in range(1, 11):
#       if zahl % 2 == 0:
#           gerade_zahlen.append(zahl)
# Achtung: Dieses "if" hat kein "else". Ein if/else gehört in einer List Comprehension nach vorne
# in den Ausdruck und sieht anders aus.


## 4. Verschachtelte Schleifen (Kombinationen)
# Erstelle alle Kombinationen aus einer Liste mit Farben und einer Liste mit Dingen.
farben = ["rot", "blau"]
dinge = ["Ball", "Hut", "Tasse"]
kombinationen = [farbe + " " + ding for farbe in farben for ding in dinge]
print("Kombinationen:", kombinationen)                      # Kombinationen: ['rot Ball', 'rot Hut', 'rot Tasse', 'blau Ball', 'blau Hut', 'blau Tasse']
print()

# Ergänzung zu 4.
# Zwei "for" hintereinander heißt: Für jede Farbe (äußere Schleife) werden alle Dinge
# durchgegangen (innere Schleife). Es entstehen 2 * 3 = 6 Kombinationen.
# Die Reihenfolge der "for" ist dieselbe wie bei normalen verschachtelten Schleifen, von links nach rechts:
#   kombinationen = []
#   for farbe in farben:
#       for ding in dinge:
#           kombinationen.append(farbe + " " + ding)
# Die erste Schleife läuft langsam (rot, dann blau), die zweite schnell (Ball, Hut, Tasse).
