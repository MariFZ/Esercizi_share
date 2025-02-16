# ESERCIZIO 10

# Distribuzione di una borsa di studio. 
# Progettare un algoritmo che, richiesto allo studente il reddito familiare e la media dei voti, 
# se il reddito è inferiore a 20.000 € e la media è superiore a 27 approva la borsa di studio, 
# altrimenti rifiuta la richiesta visualizzando il messaggio "Borsa di studio rifiutata. (Motivo: reddito o media insufficiente)"

reddito = float(input("Inserisci il tuo reddito familiare in questo formato,  per esempio: 40.000 (€): "))
media_voti = int(input("Inserisci la media dei tuoi voti: "))

if reddito < 20.000 and media_voti > 27:
    print("Borsa di studio approvata")
else:
    print("Borsa di studio rifiutata: Media o reddito insufficiente")