a=4 # tu wprowadź wartość zmiennoprzecinkową dla zmiennej a
b=12# tu wprowadź wartość zmiennoprzecinkową dla zmiennej b

print(a+b)# tutaj wypisz wynik dodania 
print(a-b)# tutaj wypisz wynik odejmowania
print(a*b)# tutaj wypisz wynik mnożenia
print(a/b)# tutaj wypisz wynik dzielenia

print("\nI to by było na tyle!")


x = float(input("Wprowadź wartość dla x: "))

y= 1/(x+(1/(x+(1/(x+(1/x))))))# tutaj wpisz swój kod

print("y =", y)



h = int(input("Czas startu (godziy): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

s=h*60+m+d
g = (s//60)%24
q = (s%60)
print(g,":",q)
