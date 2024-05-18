moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unikalne_elementy = []

for i in moja_lista:
    if i not in unikalne_elementy:
        unikalne_elementy.append(i)

print("Lista tylko z unikalnymi elementami:", unikalne_elementy)

