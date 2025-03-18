#includere de biblioteci, definirea operatorilor genetici
#generare initiala, functie fitness
import numpy as np

def algoritm_genetic(finiser,frecv,dim,NMAX,pm,dim_copii):
    frecv=np.getfromtxt(fisier_frecv)
    #generarea populatiei initiale
    populatie_curenta,calitati_curente=generare_initiala(frecv,dim)
    iteratii=1
    gata=False
    nrgen_max=1
    calitate_max=np.max(calitati_curente)
    while iteratii<=NMAX and not gata:
        #selectia parintilor
        parinti,calitati=selectie(populatie_curenta,calitati_curente,dim)
        #aplicare recombinare
        copii,calitati_copii=crossover(parinti,calitati,dim_copii)
        #aplicare mutatie
        copii_m,calitati_copii_m=mutatie(copii,calitati_copii,pm)
        populatie_noua,calitati_noi=selectie_generare_urmatoare(populatie_curenta,calitati_curente,copii_m,calitati_copii_m,dim)
        val_max=np.max(calitati_noi)
        val_min=np.min(calitati_noi)
        if val_min==val_max:
            gata=True
        if calitate_maxima<cal_max:
            calitate_maxima=cal_max
            nrgen_max=1
        else:
            nrgen_max+=1
        iteratii+=1
        populatie_curenta=populatie_noua.copy()
        calitati_curente=calitati_noi.copy()
    indice_sol=np.argmax(calitati_curente)
    solutia_GA=populatie_curenta[indice_sol]
    valoarea_GA=calitati_curente[indice_sol]