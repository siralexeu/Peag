import numpy as np

def fitness(p):
    n = p.size
    calitate = n * (n - 1) / 2
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(i - j) == abs(p[i] - p[j]):
                calitate -= 1
    return calitate

def vecini(p):
    vecini_p = np.zeros(0,dtype="int")
    calitati_v = np.zeros(0)
    n = p.size
    for i in range(n - 1):
        for j in range(i + 1, n):
            v=p.copy()
            v[i],v[j]=p[j],p[i]
            vecini_p = np.append(vecini_p, v)
            calitati_v = np.append(calitati_v, fitness(v))
    nlinii=int(vecini_p.size/n)
    vecini_p=vecini_p.reshape([nlinii,n])
    return vecini_p,calitati_v

def HC(n):
    p = np.random.permutation(n)
    c_p = fitness(p)
    local = False
    while not local:
        V_p, C_p = vecini(p)
        val_max = C_p.max()
        i_max = np.argmax(C_p)
        if c_p < val_max:
            p = V_p[i_max].copy()
            c_p = val_max
        else:
            local = True
    return p, c_p

def rezolvare(n, nr_apeluri):
    p, c_p = HC(n)
    for i in range(nr_apeluri - 1):
        pnou, cnou = HC(n)
        if cnou > c_p:
            p = pnou.copy()
            c_p = cnou
    return p, c_p


if __name__ == "__main__":
    #p = np.array([1, 3, 4, 0, 2, 5])
    #cal_p = fitness(p)
    #print(cal_p)
    #vp,cp=vecini(p)
    #print(vp)
    #print(cp)
    n = 20
    p, cp = HC(n)
    print("solutia calculata: ", p)
    dif = n * (n - 1) / 2 - cp
    if dif == 0:
        print("aranjare corecta")
    else:
        print("nr perechilor aflate in pozitie de atac: ", dif)

