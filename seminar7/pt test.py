import numpy as np
def fitness(p,castig):
    return np.dot(p,castig)
def generare_populatie(dim, castig):
    n = len(castig)
    populatie = np.zeros([dim, n], dtype="int")
    calitati = np.zeros(dim)
    for i in range(dim):
        populatie[i] = np.random.permutation(n)
        calitati[i] = fitness(populatie[i], castig)
    return populatie, calitati
def generare_populatie(dim, n):
    populatie = np.zeros((dim, n), dtype=int)
    calitati = np.zeros(dim, dtype=int)
    for i in range(dim):
        populatie[i] = np.random.permutation(n)
        calitati[i] = fitness(populatie[i])
    return populatie, calitati
def fitness(x):
    suma = np.sum(x)
    return suma, suma % 2 == 0
def generare_populatie(dim):
    populatie = np.zeros([dim, 18], dtype="int")
    i = 0
    while i < dim:
        populatie[i, :17] = np.random.randint(0, 2, 17)
        populatie[i, 17], fezabil = fitness(populatie[i, :17])
        if fezabil:
            i += 1
    return populatie

def turneu(populatie,k):  #direct
    dim=populatie.shape[0]
    parinti=populatie.copy()
    for i in range(dim):
        poz=np.random.randint(0,dim,k)
        ales=np.argmax(np.array([populatie[poz[j],17] for j in range(k)]))
        parinti[i,:17]=populatie[poz[ales],:17].copy()
        parinti[i,17]=populatie[poz[ales],17]
    return parinti

def crossover_OCX(x,y,n):  #foloseste ocx ca functie auxiliara
    poz=np.random.randint(0,n,2)
    while poz[0]==poz[1]:
        poz=np.random.randint(0,n,2)
    p1=np.min(poz)
    p2=np.max(poz)
    c1=OCX(x,y,n,p1,p2)
    c2=OCX(y,x,n,p1,p2)
    return c1,c2
def OCX(x,y,n,p1,p2):
    c2=[x[i] for i in range(p1,p2+1)]
    z1=[y[i] for i in range(p2,n) if y[i] not in c2]
    z2=[y[i] for i in range(p2) if y[i] not in c2]
    z=np.append(z1,z2)
    c3=[z[i] for i in range(n-p2-1)]
    c1=[z[i] for i in range(n-p2-1,len(z))]
    c=np.append(c1,c2)
    c=np.append(c,c3)
    return c

def crossover_CX(x,y,n):  #directa
    ciclu=cicluri(x,y,n)
    c1=x.copy()
    c2=y.copy()
    for i in range(n):
        cat, rest = np.divmod(ciclu[i], 2)
        if not rest:
            c1[i]=y[i]
            c2[i]=x[i]
    return c1,c2

def crossover_PMX(x,y,n): #foloseste pmx ca functie auxiliara
    poz=np.random.randint(0,n,2)
    while poz[0]==poz[1]:
        poz=np.random.randint(0,n,2)
    p1=np.min(poz)
    p2=np.max(poz)
    c1=PMX(x,y,n,p1,p2)
    c2=PMX(y,x,n,p1,p2)
    return c1,c2
def PMX(x,y,n,p1,p2):
    c=-np.ones(n,dtype=int)
    c[p1:p2+1]=x[p1:p2+1]
    for i in range(p1,p2+1):
        a=y[i]
        if a not in c:
            curent=i
            plasat=False
            while not plasat :
                b=x[curent]
                # poz=pozitia in care se afla b in y
                [poz]=[j for j in range(n) if y[j]==b]
                if c[poz]==-1 :
                    c[poz]=a
                    plasat=True
                else:
                    curent=poz
    z=[y[i] for i in range(n) if y[i] not in c]
    poz=[i for i in range(n) if c[i]==-1]
    m=len(poz)
    for i in range(m):
        c[poz[i]]=z[i]
    return c

def crossover_unipunct(x,y,n):
    i = np.random.randint(1,n-1)
    c1=x.copy()
    c2=y.copy()
    c1[0:i] = x[0:i]
    c1[i:n] = y[i:n]
    c2[0:i] = y[0:i]
    c2[i:n] = x[i:n]
    return c1,c2

def crossover_uniform(x,y,n):
    c1=x.copy()
    c2=y.copy()
    for i in range(n):
        r = np.random.randint(0,2)
        if r == 1:
            c1[i] = y[i]
            c2[i] = x[i]
    return c1,c2

def mutatie_populatie(populatie,calitati,pm,castig): #foloseste mutatie_inv ca functie auxiliara
    pop_mutat=populatie.copy()
    cal_mutat=calitati.copy()
    for i in range(dim):
        raspuns=np.random.uniform(0,1)
        if raspuns<pm:
            pop_mutat[i]=mutatie_inv(populatie[i])
            cal_mutat[i]=fitness(pop_mutat[i],castig)
    return pop_mutat,cal_mutat
def mutatie_inv(p):
    r=p.copy()
    n=len(p)
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    return r
def crossover_unipunct(x,y,n):
    i = np.random.randint(1,n-1)
    c1=x.copy()
    c2=y.copy()
    c1[0:i] = x[0:i]
    c1[i:n] = y[i:n]
    c2[0:i] = y[0:i]
    c2[i:n] = x[i:n]
    return c1,c2

def crossover_multipunct(x, y, n):
    c1, c2 = x.copy(), y.copy()
    r = np.random.randint(1, n)
    pct = np.random.choice(np.arange(1, n), r, replace=False)
    pct = np.sort(pct)
    parinte_crt = x
    for i in pct:
        parinte_crt = y if parinte_crt is x else x
        c1[i - 1:i + 1], c2[i - 1:i + 1] = parinte_crt[i - 1:i + 1], parinte_crt[i - 1:i + 1]
    return c1, c2

