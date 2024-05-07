rok = int(input("Wprowadź rok: "))

if rok<=1580:
    print("Nie w kalendarzu gregorianskim")
elif rok%4 !=0:
    print("Rok zwykły")
elif rok%100 !=0:
    print("Rok przestępny")
elif rok%400 !=0:
    print("Rok zwykły")
else:
    print("Rok przestępny")
 
