class Matrix:
    def __init__(self, matrix, sor=None, oszlop=None):
        if sor != None or oszlop !=None:
            assert(sor > 0 and oszlop > 0)
        self.matrix = matrix
        if sor == None or oszlop == None:
            self.sor = len(matrix)
            self.oszlop = len(matrix[0])
        else:    
            self.sor = sor
            self.oszlop = oszlop
            
    def __str__(self):
        fl = self.float_e()
        m = len(str(round(self.abs_max(), 2))) + 1
        if fl is True:
            m += 3
        mxstr = ''
        for s in range(self.sor):
            for elem in self.matrix[s]:
                if elem > -0.001 and elem < 0.001:
                    elem = 0
                if fl is True:
                    mxstr += "{:>{width}.2f}".format(elem, width=m)
                else:
                    mxstr += "{:>{width}d}".format(elem, width=m)                    
            mxstr += "\n"
        return mxstr
    
    def abs_max(self):
        ''' Visszaadja egy mátrix abszolút maximumát. '''
        
        maxim = self.matrix[0][0]
        for sor in self.matrix:
            if maxim < max(sor):
                maxim = max(sor)
                
        minim = self.matrix[0][0]
        for sor in self.matrix:
            if minim > min(sor):
                minim = min(sor)

        m = max(maxim, abs(minim))
        if m == abs(minim):
            return m * 10
        return m

    def float_e(self):
        for sor in self.matrix:
            for elem in range(len(sor)):
                if type(sor[elem]) == float:
                    return True
        return False
        
    def __mul__(self, szam):
        ''' Mátrix és valós szám szorzata. '''
        mx = self.matrix
        mul_mx = []
        for i in range(self.sor):
            temp_sor = []
            for c in range(self.oszlop):
                temp_sor.append(round(mx[i][c] * szam, 4))
            mul_mx.append(temp_sor)
        return Matrix(mul_mx, self.sor, self.oszlop)            
            
    def __add__(self, mx):
        ''' Két mátrix összegét adja vissza Mátrix formátumban.
            Kikötés: mindkét mátrix n×k méretű. '''
        assert(self.sor == mx.sor and self.oszlop == mx.oszlop)
        mx1 = self.matrix
        mx2 = mx.matrix
        osszeg = []
        for s in range(self.sor):
            temp_sor = []
            for o in range(self.oszlop):
                temp_sor.append(mx1[s][o] + mx2[s][o])
            osszeg.append(temp_sor)
        return Matrix(osszeg, self.sor, self.oszlop)

    def __sub__(self, mx):
        ''' Két mátrix különbségét adja vissza Mátrix formátumban.
            Kikötés: mindkét mátrix n×k méretű. '''
        assert(self.sor == mx.sor and self.oszlop == mx.oszlop)
        mx1 = self.matrix
        mx2 = mx.matrix
        osszeg = []
        for s in range(self.sor):
            temp_sor = []
            for o in range(self.oszlop):
                temp_sor.append(mx1[s][o] - mx2[s][o])
            osszeg.append(temp_sor)
        return Matrix(osszeg, self.sor, self.oszlop)

    def determinans(self):
        ''' Rekurzívan determinánst számol kifejtési tétellel.
            Determináns számolás csak n×n-es mátrixon hajtható végre. '''

        mx = self.matrix
        sor = self.sor
        oszlop = self.oszlop
        assert(sor == oszlop)
        det = 0
        if sor == 2 and oszlop == 2:
            return mx[0][0]*mx[1][1] - mx[0][1] * mx[1][0]
        for idx in range(sor):
            det_almx = self.almatrix(idx).determinans()
            det += Matrix.sakktabla(idx) * mx[idx][0] * det_almx
        return det

    def almatrix(self, sor_idx=0, oszlop_idx=0):
        ''' Egy mátrix almátrixát adja vissza sor -és oszlopindex alapján.
            Ciklussal kell meghívni ha az összes almátrixot meg akarjuk kapni,
            de meg lehet hívni anélkül is csak egy adott sorra vagy oszlopra. '''

        mx = self.matrix
        sor = self.sor
        oszlop = self.oszlop
        almatrix = []
        for i in range(sor):
            temp_sor = []
            for c in range(oszlop):
                if i != sor_idx and c != oszlop_idx:
                    temp_sor.append(mx[i][c])
            if temp_sor != []:
                almatrix.append(temp_sor)
        return Matrix(almatrix, sor-1, oszlop-1)

    @staticmethod
    def sakktabla(sor_idx, oszlop_idx=0):
        ''' Sakttábla szabály alapján visszaadja az adott indexekhez tartozó előjelet. '''
            
        return 1 if sor_idx % 2 == oszlop_idx % 2 else -1

    def transzponal(self):
        ''' Egy mátrix transzponáltját adja vissza Mátrix formátumban. '''
        
        mx = self.matrix
        sor = self.sor
        oszlop = self.oszlop
        trszp_mx = []
        for oszl_idx in range(oszlop):
            temp_sor = []
            for sor_idx in range(sor):
                temp_sor.append(mx[sor_idx][oszl_idx])
            trszp_mx.append(temp_sor)
        sor, oszlop = oszlop, sor
        return Matrix(trszp_mx, sor, oszlop)

    def mx_mul_mx(self, mx):
        ''' Két mátrix szorzatát adja eredményül Mátrix formátumban. '''

        assert(self.oszlop == mx.sor)
        mx = mx.transzponal()
        szorzat = []
        for sor_a in range(self.sor):
            temp_sor = []
            for sor_b in range(mx.sor):
                temp_sor.append(Matrix.skalarszorzat(self.matrix[sor_a], mx.matrix[sor_b]))
            szorzat.append(temp_sor)
        return Matrix(szorzat, self.sor, mx.sor)
    
    @staticmethod
    def skalarszorzat(v1, v2):
        ''' Két vektor skalrászorzatát számolja ki. Visszatérési értéke egy skalár. '''
        osszeg = 0
        for i in range(len(v1)):
            osszeg += v1[i] * v2[i]
        return osszeg

    def inverz(self):
        ''' Mátrix inverzét adja vissza Mátrix formátumban. '''

        det = self.determinans()
        assert(det != 0)
        almx_det = [] #almátrixok determinánsai
        for s in range(self.sor):
            temp_sor = []
            for o in range(self.oszlop):
                temp_sor.append(
                    round(self.almatrix(s,o).determinans() * Matrix.sakktabla(s, o), 4))
            almx_det.append(temp_sor)
        almx_det_mx = Matrix(almx_det, self.sor, self.oszlop)
        inverz = almx_det_mx.transzponal() * (1/det) #almátrixok determinánsaiból képzett*
        return inverz # *mátrix transzponáltja, szorozva az eredeti mátrix determinánsának reciprokával.

    def gauss_lmnc(self):
        ''' Gauss eliminálást végez a kapott mátrixon.
            kikötés, hogy n×n+1 -es input legyen. '''
        
        assert(self.sor == self.oszlop - 1)
        gauss = self.masol()
        g_mx = gauss.matrix
        g_s = gauss.sor
        g_o = gauss.oszlop
        for oszlop in range(g_o-2):
            if g_mx[oszlop][oszlop] !=0:
                for sor in range(oszlop+1, g_s):
                    sor1 = Matrix([self.sor_1_1(g_mx[oszlop], g_mx[oszlop][oszlop])])
                    sor2 = Matrix([g_mx[sor]],1,g_o)
                    sor_mx = sor2 - (sor1 * g_mx[sor][oszlop])
                    g_mx[sor] = sor_mx.matrix[0]
            else:
                for s in range(oszlop, g_s):
                    if g_mx[s][oszlop] != 0:
                        g_mx[oszlop], g_mx[s]= g_mx[s], g_mx[oszlop]
                        self.sor_1_1(g_mx[oszlop], g_mx[oszlop][oszlop])
            if g_mx[g_s-1][g_o-2] != 0:
                g_mx[g_s-1] = self.sor_1_1(g_mx[g_s-1], g_mx[g_s-1][g_o-2])

        for osz in range(g_o-2, -1, -1):
            for sr in range(osz, 0, -1):
                temp_sor1 = Matrix([g_mx[sr-1]], 1, g_o)
                temp_sor2 = Matrix([g_mx[osz]],1, g_o) * g_mx[sr-1][osz]
                temp_sor = temp_sor1 - temp_sor2
                g_mx[sr-1] = temp_sor.matrix[0]
        if g_mx[g_s-1][g_o-2] != 1:
                g_mx[g_s-1][g_o-1] = 0
        return gauss

    def sor_1_1(self, sor, oszto):
        ''' Elosztja egy sor (lista/ vektor) minden elemét a kapott osztóval. '''
        
        for i in range(len(sor)):
            sor[i] /= oszto
        return sor

    def masol(self):
        ''' Másolatot készít egy mátrixról, arra az esetre, ha nem referenciával akarnánk dolgozni. '''
        
        masolt = []
        for sor in self.matrix:
            masolt.append(sor)
        return Matrix(masolt, self.sor, self.oszlop)

    def rang(self):
        mx = self.gauss_lmnc()
        rang = self.sor
        for i in range(self.sor):
            if mx.matrix[i][i] != 1:
                rang -= 1
        return rang
