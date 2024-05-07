

slowo_uzytkownika = input("Wpisz słowo: ")

slowo_uzytkownika = slowo_uzytkownika.upper()

slowo_bez_samoglosek = ""

for litera in slowo_uzytkownika:
    if litera in ['A','E','I','O','U']:
        continue
    slowo_bez_samoglosek += litera

print("Słowo bez samoglosek: ", slowo_bez_samoglosek)

