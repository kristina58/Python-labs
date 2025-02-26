#Twoim zadaniem jest uzupełnienie kodu w celu otrzymania wyników czterech
#podstawowych działań arytmetycznych.
#Wyniki należy wyświetlić na konsoli.
#Możesz nie być w stanie ochronić kodu przed użytkownikiem,
#który chce podzielić przez zero. W porządku, nie przejmuj się tym teraz.
#Przetestuj swój kod - czy wypisuje oczekiwane rezultaty?
#Nie pokażemy ci żadnych danych testowych - byłoby to zbyt proste.

a=4 # tu wprowadź wartość zmiennoprzecinkową dla zmiennej a
b=12# tu wprowadź wartość zmiennoprzecinkową dla zmiennej b

print(a+b)# tutaj wypisz wynik dodania 
print(a-b)# tutaj wypisz wynik odejmowania
print(a*b)# tutaj wypisz wynik mnożenia
print(a/b)# tutaj wypisz wynik dzielenia

print("\nI to by było na tyle!\n")

#Twoim zadaniem jest uzupełnienie kodu w celu obliczenia następującego
#wyrażenia:
#Przykładowe dane wejściowe: 1
#Oczekiwany wynik:
#y = 0.6000000000000001

#Przykładowe dane wejściowe: 10
#Oczekiwany wynik:
#y = 0.09901951266867294

#Przykładowe dane wejściowe: 100
#Oczekiwany wynik:
#y = 0.009999000199950014

#Przykładowe dane wejściowe: -5
#Oczekiwany wynik:
#y = -0.19258202567760344

x = float(input("Wprowadź wartość dla x: "))

y= 1/(x+1/(x+1/(x+1/x)))# tutaj wpisz swój kod

print("y =", y)
print()

#Twoim zadaniem jest przygotowanie prostego kodu, który będzie w stanie
#wskazać czas zakończenia dla jakiegoś przedziału czasu, podanego jako
#liczba minut (może być dowolnie duża). Czas rozpoczęcia podawany jest
#jako para godzin (0..23) i minut (0..59). Wynik musi zostać wyświetlony
#na konsoli.
#Na przykład, jeśli wydarzenie zaczyna się o 12:17 i trwa 59 minut,
#to skończy się o 13:16.
#Nie przejmuj się żadnymi niedoskonałościami w kodzie - jest w porządku,
#jeśli akceptuje on niepoprawny czas - najważniejsze jest to, że kod generuje
#prawidłowe wyniki dla prawidłowych danych wejściowych.
#Przetestuj swój kod dokładnie. Podpowiedź: użycie operatora % może być
#kluczem do sukcesu.
#Przykładowe dane wejściowe:
#12
#17
#59
#Oczekiwany wynik: 13:16

#Przykładowe dane wejściowe:
#23
#58
#642
#Oczekiwany wynik: 10:40

#Przykładowe dane wejściowe:
#0
#1
#2939
#Oczekiwany wynik: 1:0


h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

m2=h*60+m+d
h2=m2//60%24
m3=m2%60
print("Czas zakoczenia",h2,":",m3)
