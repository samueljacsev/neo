import matrix

def export(mx, nev):
    file = open(nev + '.txt', 'w', encoding='utf-8')
    for sor in mx.matrix:
        for elem in sor:
            if elem > -0.001 and elem < 0.001:
                elem = 0
            file.write("{:0.2f} ".format(elem))
        file.write('\n')
    file.close()

def beolvas(fajlnev):
    ''' Mátrixot olvas be txt fájlból.'''

    fajl = []
    try:
        f = open(fajlnev + '.txt', 'rt', encoding='utf-8')
        while True:
            sor = f.readline()
            sor = sor.rstrip('\n')
            if sor == '':
                f.close
                break
            sor = sor.split()
            fajl.append(sor)
    except:
        raise FileNotFoundError

    mx_jelolt = []
    for sorok in fajl:
        temp_sor = []
        for elem in sorok:
            try:
                szam = float(elem)
                temp_sor.append(szam)
            except ValueError:
                break
        mx_jelolt.append(temp_sor)
    if sor_vizsgalat(mx_jelolt) is True:
        return matrix.Matrix(mx_jelolt)
    else:
        raise ValueError


def sor_vizsgalat(lista):
    ''' Input ellenőrzésére alkalmas függvény. Megelzőzi hogy hibás mátrix kerülhessen a rendszerbe.'''

    elemszam = len(lista[0])
    for sor in lista:
        if elemszam != len(sor):
            return False
    return True
