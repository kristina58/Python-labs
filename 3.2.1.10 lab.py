slowo_uzytkownika = input("Wprowadź słowo: ")

slowo_uzytkownika = slowo_uzytkownika.upper()

for litera in slowo_uzytkownika:
    if litera in ['A','I','O','U']:
        continue
    print(litera)
    

