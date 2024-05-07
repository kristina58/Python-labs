tajnytajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
numer = int(input("Wprowadz numer:"))
while numer !=777:
    if numer != tajnytajny_numer:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
        numer = int (input("Wprowadz numer:"))
    if numer == tajnytajny_numer:
        print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
