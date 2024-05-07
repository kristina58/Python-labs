blokow = int(input("Wprowadź liczbę bloków: "))

wysokosc = 0

while blokow >= wysokosc + 1:
    wysokosc += 1
    blokow -= wysokosc

print("Wysokość piramidy wynosi:", wysokosc)
