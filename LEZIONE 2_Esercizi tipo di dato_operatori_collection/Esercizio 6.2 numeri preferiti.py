# 6.2 NUMERI PREFERITI

name_number: dict = {"Natalia": 10, "Andrew": 6, "Chiara": 14, "Jean Paul": 2, "Manuel": 24}

# stampa il valore del numero preferito, inserendo la chiave

print(f"Questo è il numero preferito di Manuel: {name_number['Manuel']}. Ho messo tra parentesi graffe il nombre del dizionario e tra parentesi quadre il nome della chiave")

# mettendo .items alla fine, stampa il dizionario con chiave e valore, dandome il valore in una lista

print(name_number.items())

# Se invece voglio stampare la chiave e il valore, posso convertire il dizionario in una lista e dopo scrivere il numero dell'indice dell'elemento

print(f"Questo è il numero preferito della prima chiave/valore della persona nel dizionario.  Per farlo, ho convertito il dizionario in una lista, ho scritto .items alla fine e ho scritto l'indice in parentesi quadre: \n list(name_number.items())[0], e il risultato viene cosi: {list(name_number.items())[0]}")

print(f"Questo è il numero preferito di tutte le chiavi/valori del dizionario.  Per farlo, ho convertito  il dizionario in una lista e alla fine al nome del dizionario ho scritto .items: {list(name_number.items())}")





#for name, number in name_number.items(): # FUNZIONE .items ()
    #print(f"{name}: {number}")