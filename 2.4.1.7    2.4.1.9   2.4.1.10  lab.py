#Oto krótka opowiastka:
#Dawno, dawno temu, w Krainie Pomarańczy, Pomarańczowy Król miał trzy pomarańcze
#Agnieszka miała pięć pomarańczy, a Adam miał ich sześć.
#Wszyscy żyli długo i szczęśliwie. Koniec historii.
#Twoim zadaniem jest:
#stworzenie zmiennych: pomaranczowy_krol, agnieszka, oraz adam,
#przypisanie wartości do zmiennych. Wartości muszą odpowiadać liczbie
#owoców posiadanych przez Pomarańczowego Króla, Agnieszkę oraz Adama,
#po przypisaniu liczb do zmiennych, wyświetl w konsoli zmienne w jednej linii,
#i oddziel każdą z nich przecinkiem,
#teraz utwórz zmienną o nazwie pomaranczy_razem równą sumie wartości trzech
#pozostałych zmiennych,
#wyświetl w konsoli wartość przechowywaną w zmiennej pomaranczy_razem

pomaranczowy_krol=3
agnieszka=5
adam=6
print(pomaranczowy_krol,agnieszka,adam)
pomaranczy_razem=pomaranczowy_krol+agnieszka+adam
print(pomaranczy_razem)
print()

#Mile i kilometry to jednostki długości.
#Zakładając, że 1 mila jest równa w przybliżeniu 1.61 kilometra,
#uzupełnij program w edytorze tak, aby konwertował:
#mile na kilometry;
#kilometery na mile.
#Nie zmieniaj niczego w istniejącym kodzie. Wpisz swój kod w miejscach wskazanych
#przez # Napisz kod tutaj.. Sprawdź swój program za pomocą danych, które dostarczyliśmy
#w kodzie źródłowym.
#Oczekiwany wynik
#7.38 mi to 11.88 km
#12.25 km to 7.61 mi

kilometry = 12.25
mile = 7.38

mile_na_kilometry = mile*1.61 # Napisz kod tutaj.
kilometry_na_mile = kilometry/1.61 # Napisz kod tutaj.

print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")
print()

#Spójrz na kod w edytorze: sczytuje on wartość typu float,
#przypisuje ją do zmiennej xi wypisuje wartość przypisaną do zmiennej y.
#Twoim zadaniem jest uzupełnienie kodu w celu obliczenia następującego wyrażenia:
#3x3 - 2x2 + 3x - 1
#Wynik powinien zostać przypisany do zmiennej y.
#Dane Testowe
#Przykładowe dane wejściowe
#x = 0
#x = 1
#x = -1
#Oczekiwany wynik
#y = -1.0
#y = 3.0
#y = -9.0

x = 0
x = float(x)
y=3*x**3-2*x**2+3*x-1
print("y =", y)

x = 1
x = float(x)
y=3*x**3-2*x**2+3*x-1
print("y =", y)

x = -1
x = float(x)
y=3*x**3-2*x**2+3*x-1
print("y =", y)

