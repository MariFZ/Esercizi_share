# 6.2 NUMERI PREFERITI

name_number: dict = {"Natalia": 10, "Andrew": 6, "Chiara": 14, "Jean Paul": 2, "Manuel": 24}

print(name_number.items()[0])

print(list(name_number.items())[0])

print(f"Questo è il numero preferito di: {list(name_number.items())[0]}")
print(f"Questo è il numero preferito di: {name_number['Jean Paul']}")
print(f"Questo è il numero preferito di: {name_number['Manuel']}")


for name, number in name_number.items(): # FUNZIONE .items ()
    print(f"{name}: {number}")