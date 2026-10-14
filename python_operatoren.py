# Aufgabe 6 | Python Operatoren

## 1. Arithmetische Operatoren
# Erstelle zwei Variablen: a und b mit den Werten 17 und 5.
# Berechne und gib jeweils das Ergebnis aus: Addition, Subtraktion, Multiplikation,
# Division, Ganzzahldivision, Modulo (Rest) und Potenzierung.
a = 17
b = 5
print("Addition:", a + b)                  # Addition: 22
print("Subtraktion:", a - b)               # Subtraktion: 12
print("Multiplikation:", a * b)            # Multiplikation: 85
print("Division:", a / b)                  # Division: 3.4
print()
# // und % gehören zusammen: Aus 17 = 5 mal 3 plus 2 kommen die 3 und die 2. Die 3 liefert //, der Rest 2 kommt von %.
print("Ganzzahldivision:", a // b)         # Ganzzahldivision: 3
print("Modulo:", a % b)                    # Modulo: 2
print()
print("Potenzierung:", a ** b)             # Potenzierung: 1419857
print()

## 2. Zuweisungsoperatoren
# Starte mit einer Variablen x = 10.
# Verändere x mit +=, -=, *= und /=. Gib nach jeder Operation das Ergebnis aus.
x = 10
x += 3
print("Nach += 3:", x)         # Nach += 3: 13
x -= 3
print("Nach -= 3:", x)         # Nach -= 3: 10
x *= 3
print("Nach *= 3:", x)         # Nach *= 3: 30
x /= 3
print("Nach /= 3:", x)         # Nach /= 3: 10.0
print()



## 3. Vergleichsoperatoren
# Vergleiche a und b mit ==, !=, >, <, >= und <=.
# Gib das Ergebnis jedes Vergleichs aus.
print("a == b:", a == b)       # a == b: False
print("a != b:", a != b)       # a != b: True
print("a > b:", a > b)         # a > b: True
print("a < b:", a < b)         # a < b: False
print("a >= b:", a >= b)       # a >= b: True
print("a <= b:", a <= b)       # a <= b: False
print()



## 4. Logische Operatoren
# Erstelle zwei Boolean-Variablen: is_python_fun = True und is_java_fun = False.
# Verknüpfe oder verneine sie mit and, or und not. Gib die Ergebnisse aus.
is_python_fun = True
is_java_fun = False
print("and:", is_python_fun and is_java_fun)       # and: False
print("or:", is_python_fun or is_java_fun)         # or: True
print("not Python:", not is_python_fun)            # not Python: False
print("not Java:", not is_java_fun)                # not Java: True
print()



## 5. Identitätsoperatoren
# Erstelle zwei Listen: list1 = [1, 2, 3] und list2 = list1.
# Prüfe, ob list1 is list2 gilt und ob list1 is not list2 gilt.
# Erstelle eine dritte Liste list3 = [1, 2, 3] und prüfe, ob list1 is list3 gilt.
list1 = [1, 2, 3]
list2 = list1
print("list1 is list2:", list1 is list2)              # list1 is list2: True
print("list1 is not list2:", list1 is not list2)      # list1 is not list2: False
list3 = [1, 2, 3]
print("list1 is list3:", list1 is list3)              # list1 is list3: False
print()



## 6. Zugehörigkeitsoperatoren
# Erstelle einen String text = "Python programming is fun!".
# Prüfe, ob das Wort "Python" im String enthalten ist.
# Prüfe, ob das Wort "Java" nicht im String enthalten ist.
text = "Python programming is fun!"
print('"Python" in text:', "Python" in text)               # "Python" in text: True
print('"Java" not in text:', "Java" not in text)           # "Java" not in text: True
print()



## 7. Bitweise Operatoren (BONUS)
# Mit a = 5 und b = 3: bitweises UND (&), ODER (|), XOR (^),
# a um 1 nach links schieben (<<) und b um 1 nach rechts schieben (>>).
a = 5
b = 3
print("a & b:", a & b)         # a & b: 1
print("a | b:", a | b)         # a | b: 7
print("a ^ b:", a ^ b)         # a ^ b: 6
print("a << 1:", a << 1)      # a << 1: 10
print("b >> 1:", b >> 1)      # b >> 1: 1
print()



## 8. Operatorrangfolge
# Schreib einen Ausdruck, der +, * und ** kombiniert.
# Berechne ihn einmal ohne und einmal mit Klammern, die die Reihenfolge ändern.
# Schau dir an, wie sich das Ergebnis unterscheidet.
print("Ohne Klammern:", 2 + 3 * 2 ** 2)                  # Ohne Klammern: 14 (2 ** 2 = 4, 3 * 4 = 12, 2 + 12 = 14)
print("Mit Klammern:", (2 + 3) * 2 ** 2)                 # Mit Klammern: 20 (2 + 3 = 5, 2 ** 2 = 4, 5 * 4 = 20)
print("Mehr Klammern:", ((2 + 3) * 2) ** 2)              # Mehr Klammern: 100 (2 + 3 = 5, 5 * 2 = 10, 10 ** 2 = 100)

