c0 = int(input("Wprowadź liczbę naturalną: "))

kroki = 0

while c0 != 1:
    if c0%2 == 0:
        c0 //=2
    else:
        c0 = 3*c0+1
    print (c0)
    kroki +=1
print("Liczba kroków: ", kroki)
    
