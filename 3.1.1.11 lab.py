dochod = float(input("Wprowadź swój roczny dochód: "))

if dochod<85528.0:
    podatek=dochod*0.18-556.2
elif dochod>85528:
    podatek=(dochod-85528)*0.32+14839.2
if podatek<0:
    podatek=0.0
podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)
