import numpy as np

#FUNCTII PENTRU SELECTIA PARINTILOR
#POPULATIA DE INTRARE/SELECTATA - SPECIFICATE PRIN CATE O MATRICE SI CATE UN VECTOR AL CALITATILOR - pentru situatii generale de reprezentare


#SELECTIA TURNEU pentru k indivizi
#selectia turneu - selecteaza dim indivizi
#I: pop,qual,dim,n,k - matricea populatiei, vectorul calitatilor, pop-dim x n, qual - dim, numarul indivizilor care intra in competitie
#E: spop,squal - populatia selectata, impreuna cu calitatile membrilor sai
def turneu(pop,qual,dim,n,k):
    spop=pop.copy()
    squal=np.zeros(dim)
    for it in range(dim):
        #selectia unui individ la iteratia it
        #generarea a k indici aleatori in poz
        poz=np.random.randint(0,dim,k)
        #calitatile care intra in competitie
        v=[qual[poz[i]] for i in range(k)]
        M=max(v)
        p=np.where(v==M)
        #imax = prima pozitie in v in care este atinsa valoarea maxima
        imax=p[0][0]
        # isel=corespondentul lui imax in populatie
        isel=poz[imax]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal

#SELECTIA TURNEU pentru k indivizi
#selectia turneu - selecteaza dimc<dim indivizi
#I: pop,qual,dim,n,k - matricea populatiei, vectorul calitatilor, pop-dim x n, qual - dim, numarul indivizilor care intra in competitie
#E: spop,squal - populatia selectata, impreuna cu calitatile membrilor sai
def turneu_2(pop,qual,dim,dimc,n,k):
    spop=np.zeros([dimc,n])
    squal=np.zeros(dimc)
    for it in range(dimc):
        #selectia unui individ la iteratia it
        #generarea a k indici aleatori in poz
        poz=np.random.randint(0,dim,k)
        #calitatile care intra in competitie
        v=[qual[poz[i]] for i in range(k)]
        M=max(v)
        p=np.where(v==M)
        #imax = prima pozitie in v in care este atinsa valoarea maxima
        imax=p[0][0]
        # isel=corespondentul lui imax in populatie
        isel=poz[imax]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal


#SELECTIILE RULETA SI SUS

#calculul distributiei de probabilitate FPS pentru un vector de calitati
# I: qual,dim - vectorul calitatilor, de dimensiune dim
# E: distributia cumulata qfps
def fps(qual,dim):
    fps=np.zeros(dim)
    #suma valorilor vectorului qual
    suma=np.sum(qual)
    for i in range (dim):
        fps[i] = qual[i]/suma
    qfps=fps.copy()
    for i in range(1, dim):
        qfps[i]=qfps[i-1]+fps[i]
    return qfps

#fps cu sigma scalare
# I: qual,dim - vectorul calitatilor, de dimensiune dim
# E: distributia cumulata qfps
#daca toate elementele din qual sunt egale, returneaza fps standard
def sigmafps(qual, dim):
    #media vectorului qual
    med=np.mean(qual)
    #deviatia standard - qual
    var=np.std(qual)
    #calculul variantei sigma-scalate: newq[i]=max(qual[i]-(med-2var)), i=1...dim
    newq=[max(0,qual[i]-(med-2*var)) for i in range(dim)]
    #calculul distributieipe noul vector
    if np.sum(newq)==0:
        qfps=fps(qual,dim)
    else:
        qfps=fps(newq,dim)
    return qfps


#calculul dispributiei de probabilitate rang liniar pentru un vector de calitati
# I: dim - dimensiunea populatiei
#    s - presiunea de selectie
# E: distributia cumulata qlr
def lrang(dim,s):
    #calculul probabilitatii rang liniar
    lr=[(2-s)/dim+2*(i+1)*(s-1)/(dim*(dim+1)) for i in range(dim)]
    #calculul probabilitatii cumulate
    qlr=lr.copy()
    for i in range(1, dim):
        qlr[i]=qlr[i-1]+qlr[i]
    return np.array(qlr)

#selectia ruleta cu distributia fps cu sigma-scalare
#I: pop,qual,dim,n - matricea populatiei, vectorul calitatilor, pop-dim x n, qual - dim
#E: spop,squal - populatia selectata, impreuna cu calitatile membrilor sai
def ruleta(pop,qual,dim,n):
    spop=pop.copy()
    squal=np.zeros(dim)
    #utilizeaza fps cu sigma-scalare
    qfps=sigmafps(qual,dim)
    for it in range(dim):
        #selectia unui individ la iteratia it
        r=np.random.uniform(0,1)
        poz=np.where(qfps>=r)
        #isel = prima pozitie in qfps cu suma primelor isel elemente mai mare decat r
        isel=poz[0][0]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal

# sorteaza populatia pop, cu calitatile qual crescator dupa calitati
#I: pop,qual, dim - ca mai sus
# E: pops, quals - variantele sortate dupa calitati
def sort_pop(pop,qual):
    indici=np.argsort(qual)
    pops=pop[indici]
    quals=qual[indici]
    return pops,quals

#selectia ruleta cu distributia rang
#populatia de intrare este presupusa sortata
#I: pop,qual,dim,n,s - matricea populatiei, vectorul calitatilor, pop-dim x n, qual - dim, presiunea de selectie
#E: spop,squal - populatia selectata, impreuna cu calitatile membrilor sai
def ruleta_rang(pop,qual,dim,n,s):
    spop=pop.copy()
    squal=np.zeros(dim)
    #utilizeaza selectia rang
    qr=lrang(dim,s)
    for it in range(dim):
        #selectia unui individ la iteratia it
        r=np.random.uniform(0,1)
        poz=np.where(qr>=r)
        #isel = prima pozitie in qfps cu suma primelor isel elemente mai mare decat r
        isel=poz[0][0]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal


#selectia SUS cu distributia rang liniar
#I: pop,qual,dim,n - matricea populatiei, vectorul calitatilor, pop-dim x n, qual - dim
#E: pop_s,qual_s - populatia selectata, impreuna cu calitatile membrilor sai
def SUS_rangl(pop,qual,dim,n,s):
    pop,qual=sort_pop(pop, qual)
    spop=pop.copy()
    squal=np.zeros(dim)
    #utilizeaza fps cu sigma-scalare
    qfps=lrang(dim,s)
    r=np.random.uniform(0,1/dim)
    k,i=0,0
    while (k<dim):
        while (r<=qfps[i]):
            spop[k][:]=pop[i][:]
            squal[k]=qual[i]
            r=r+1/dim
            k=k+1
        i=i+1
    newp = np.random.permutation(dim)
    pop_r = spop[newp]
    qual_r = squal[newp]
    return pop_r, qual_r

#selectia SUS cu distributia fps cu sigma scalare
#I: pop,qual,dim,n - matricea populatiei, vectorul calitatilor, pop-dim x n, qual - dim
#E: spop,squal - populatia selectata, impreuna cu calitatile membrilor sai
def SUS(pop,qual,dim,n):
    spop=pop.copy()
    squal=np.zeros(dim)
    #utilizeaza fps cu sigma-scalare
    qfps=sigmafps(qual,dim)
    r=np.random.uniform(0,1/dim)
    k,i=0,0
    while (k<dim):
        while (r<=qfps[i]):
            spop[k][:]=pop[i][:]
            squal[k]=qual[i]
            r=r+1/dim
            k=k+1
        i=i+1
    return spop, squal

#SELECTIA ELITISTA

#selectia elitista
#I: pop_c,qual_c,pop_mo,qual_mo - populatiile curenta si a copiilor mutati pe baza carora se face selectia, fiecare insotita de vectorii calitatilor
#E: pop,qual - populatia rezultata si vectorul calitatilor
def elitism(pop_c,qual_c,pop_mo,qual_mo,dim):
    pop=np.copy(pop_mo)
    qual=np.copy(qual_mo)
    max_c=np.max(qual_c)
    max_mo=np.max(qual_mo)
    if max_c>max_mo:
        p1=np.where(qual_c==max_c)
        #imax = prima pozitie in qual_c in care este atinsa valoarea maxima
        imax=p1[0][0]
        ir=np.random.randint(dim)
        # inlocuirea
        pop[ir]=pop_c[imax].copy()
        qual[ir]=max_c
    return pop,qual



#selectia GENITOR
#I:
# pop_c,qual_c,pop_mo,qual_mo - populatiile curenta si a copiilor mutati pe baza carora se face selectia, fiecare insotita de vectorii calitatilor
# dim, dimc - dimensiunile
#E: pop_r,qual_r - populatia rezultata si vectorul calitatilor
def genitor(pop_c,qual_c,pop_mo,qual_mo,dim,dimc):
    pops,quals=sort_pop(pop_c,qual_c)
    pop=pops.copy()
    qual=quals.copy()
    for i in range(dimc):
        pop[i]=pop_mo[i].copy()
        qual[i]=qual_mo[i]
    # pentru a obtine populatii in ordinea oarecare a indivizilor, amestec
    newp=np.random.permutation(dim)
    pop_r=pop[newp]
    qual_r=qual[newp]
    return pop_r,qual_r

#selectia determinista
#I: pop_c,qual_c,pop_mo,qual_mo - populatiile curenta si a copiilor mutati pe baza carora se face selectia, fiecare insotita de vectorii calitatilor
# dim, L - dimensiunile
#E: pop_r,qual_r - populatia rezultata si vectorul calitatilor
def sel_det(pop_c,qual_c,pop_mo,qual_mo,dim,L):
    pop=np.append(pop_c,pop_mo)
    pop.resize(2*dim,L)
    qual=np.append(qual_c,qual_mo)
    p,q=sort_pop(pop, qual)
    pop_1=p[dim:2*dim].copy()
    qual_1=q[dim:2*dim].copy()
    newp = np.random.permutation(dim)
    pop_r = pop_1[newp]
    qual_r = qual_1[newp]
    return pop_r,qual_r