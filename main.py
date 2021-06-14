import matrix
import fajlmuveletek
import os

class Tarhely():
    A = matrix.Matrix([[7.11,9,2.5,9],[-14,9.5,-3,-13],[28.3,8,-10,39]],3,4)
    B = matrix.Matrix([[2,2,3],[5,9,11],[9,7,4]],3,3)
    C = matrix.Matrix([[5,9,11,5],[9,7,4,0],[0,11,3,42]])

def import_menu():
    while True:
        print('*******__MÁTRIX BEVITEL__*******')
        print('\nNeo 3 mátrixot tud kezelni, ezek neve A, B és C.')
        print('Válassz az alábbi lehetőségek közül: ')
        print('1. Mátrix importálása fájlból.')
        print('2. Mátrix beírása.')
        print('9. Vissza a főmenübe.\n')
        valasz = input('Válaszz bevitelt: ')
        try:
            valasz = int(valasz)
        except:
            print('Nem számot adtál meg. ')
            continue
        if valasz == 1:
            mx_fajlbol()
        elif valasz == 2:
            try:
                user_input()
            except ValueError:
                print('Nem számot adtál meg.')
        elif valasz == 9:
            break
        else:
            print('Ilyen opció sajnos nincs.\n')

def mx_fajlbol():
    cls()
    print('**Mátrix import**\n')
    try:
        print("A kiterjesztés legyen .txt, de azt ne add meg, csak a fájl nevét. Pl 'matrix'.")
        fajlnev = input('Fájlnev: ')
        M = fajlmuveletek.beolvas(fajlnev)
        print(fajlnev + '=')
        print(M)
        mentes(M)
    except ValueError:
        print('Hibás bemenet. Lehet hogy eltérő elemszámú sorok vannk.')
    except FileNotFoundError:
        print('\nNem létező, vagy nem txt formátumú fájl.\n')
        
    
def user_input():
    cls()
    print('**Mátrix beírása**\n')
    mx = []
    while True:
        sor_szam = input("Add meg a sorok számát: ")
        oszlop_szam = input("Add meg az oszlopok számát: ")
        try:
            sor_szam = int(sor_szam)
            oszlop_szam = int(oszlop_szam)
            if sor_szam > 0 and oszlop_szam > 0:
                break
            else:
                print('Figyelj, hogy sor > 0, oszlop > 0 legyen.')
                continue
        except ValueError:
            print('Nem számot adtál meg.')
        
    for s in range(sor_szam):
        print('{}.sor:'.format(s + 1))
        sor = []
        for o in range(oszlop_szam):
            szam = int(input())
            sor.append(szam)
        mx.append(sor)
    kesz = matrix.Matrix(mx, sor_szam, oszlop_szam)
    mentes(kesz) 

def muveletek():
    cls()
    while True:   
        print('\n*******__MÁTRIXMŰVELETEK__*******')
        print('\nVálassz az alábbi műveletek közül!')
        print('0. Gauss elimináció.')
        print('1. Rang számolás.')
        print('2. Két mátrix összeadása')
        print('3. Két mátrix különbsége')
        print('4. Két mátrix szorzata.')
        print('5. Mátrix szorzása valós számmal.')
        print('6. Transzponálás.')
        print('7. Determináns számolás.')
        print('8. Inverz számolás.')
        print('9. Vissza a főmenübe\n')

        valasz = input('Válaszz műveletet: ')
        try:
            valasz = int(valasz)
        except:
            print('Nem számot adtál meg. ')
            continue
        if valasz == 0:
            gauss_elim()
        elif valasz == 1:
            rang()
        elif valasz == 2:
            mx_add_mx()
        elif valasz == 3:
            mx_sub_mx()
        elif valasz == 4:
            mx_mul_mx()
        elif valasz == 5:
            mx_mul_num()
        elif valasz == 6:
            transzponal()
        elif valasz == 7:
            determinans()
        elif valasz == 8:
            inverz()
        elif valasz == 9:
                break
        else:
            print('Ilyen opció sajnos nincs.')

def gauss_elim():
    cls()
    print('**Gauss elimináció**\n')
    print('Melyiken szeretnél Gauss eliminálni?')
    try:
        M, nev = tarhely_valaszt()
        eredmeny = M.gauss_lmnc()
        print('Gauss lmnc ({})='.format(nev))
        print(eredmeny)
        mented_e(eredmeny)
    except AssertionError:
        print('Gauss eliminálni csak n×n+1-es bővített mátrixon lehet.')
    except TypeError:
        pass        

def rang():
    cls()
    print('**Rang**\n')
    print('Melyik rangját szeretnéd tudni?')
    try:
        M, nev = tarhely_valaszt()
        eredmeny = M.rang()
        print('Rang({})= {}'.format(nev, eredmeny))
    except AssertionError:
        print('Rangja csak n×n+1-es bővített mátrixnak lehet.')
    except TypeError:
        pass        
    

def mx_add_mx():
    cls()
    print('**Két mátrix összege**\n')
    print('Válaszd ki az elsőt?')
    M1, nev1 = tarhely_valaszt()
    print('\nMielyiket szeretnéd hozzáadni {}-hoz/hez?'.format(nev1))
    M2, nev2 = tarhely_valaszt()
    try:
        eredmeny = M1 + M2
        print('\n{} + {}='.format(nev1, nev2))
        print(eredmeny)
        mented_e(eredmeny)
    except AssertionError:
        if M1.sor == M2.oszlop and M1.oszlop == M2.sor:
            print('Nem kompatibilis mátrixok, de ne csüggedj el, transzponálással menni fog!')
        else:
            print('Nem kompatibilis mátrixok.')
    except TypeError:
        pass

def mx_sub_mx():
    cls()
    print('**Két mátrix különbsége**\n')
    print('Mielyikből szeretnél kivonni?')
    M1, nev1 = tarhely_valaszt()
    print('\nMielyiket szeretnéd kivonni {}-ból?'.format(nev1))
    M2, nev2 = tarhely_valaszt()
    try:
        eredmeny = M1 - M2
        print('\n{} - {}='.format(nev1, nev2))
        print(eredmeny)
        mented_e(eredmeny)
    except AssertionError:
        if M1.sor == M2.oszlop and M1.oszlop == M2.sor:
            print('Nem kompatibilis mátrixok, de ne csüggedj el, transzponálással menni fog!')
        else:
            print('Nem kompatibilis mátrixok.')
    except TypeError:
        pass
    
def mx_mul_mx():
    cls()
    print('**Két mátrix szorzata**\n')
    print('Mielyiket szeretnéd szorozni?')
    M1, nev1 = tarhely_valaszt()
    print('\nMielyikkel szeretnéd szorozni {}-t?'.format(nev1))
    M2, nev2 = tarhely_valaszt()
    try:
        eredmeny = M1.mx_mul_mx(M2)
        print('\n{} * {}='.format(nev1, nev2))
        print(eredmeny)
        mented_e(eredmeny)
    except AssertionError:
        if M1.sor == M2.oszlop or M1.oszlop == M2.sor:
            print('\n{} * {} nem lehetséges, de ne csüggedj el.'.format(nev1, nev2))
            print('{} * {} sikerülni fog!'.format(nev2, nev1))
        else:
            print('\nNem kompatibilis mátrixok.')
    except TypeError:
        pass
    
def mx_mul_num():
    cls()
    print('**Mátrix szorzása számmal**\n')
    M, nev = tarhely_valaszt()
    print('Mennyivel szeretnéd szorozni?')
    while True:
        szam = input('szám: ')
        try:
            szam = int(szam)
            print('{} * {}='.format(nev, szam))
            eredmeny = M * szam
            print(eredmeny)
            mented_e(eredmeny)
            break
        except ValueError:
            print('Nem számot adtál meg.')
        except TypeError:
            pass

def transzponal():
    cls()
    print('**Transzponálás**\n')
    M, nev = tarhely_valaszt()
    print("Transzponált {}=".format(nev))
    eredmeny = M.transzponal()
    print(eredmeny)
    mented_e(eredmeny)

def determinans():
    cls()
    print('**Determináns**\n')
    M, nev = tarhely_valaszt()
    try:
        eredmeny = M.determinans()
        print("\ndet({})= {}.".format(nev, eredmeny))
    except AssertionError:
        print('\nNem n×n- es mátrixnak sajnos nincs determinánsa.')
    except TypeError:
        pass

def inverz():
    cls()
    print('**Inverz**\n')
    M, nev = tarhely_valaszt()
    try:
        eredmeny = M.inverz()
        print("Inverz {}=".format(nev))
        print(eredmeny)
        mented_e(eredmeny)
    except AssertionError:
        if M.sor == M.oszlop:
            print('det({})= 0, ezért nincs inverze.'.format(nev))
        else:
            print('\nNem n×n- es mátrixnak sajnos nincs inverze.')
    except TypeError:
        pass

def mented_e(mx):
    print('Szeretnéd menteni?')
    valasz = input("i/n: ")
    if valasz == 'i' or valasz == 'I':
        return mentes(mx)

def tarhely_valaszt():
    print("Válassz mátrixot.")
    print('V = Vissza\n')
    while True:
        valasz = input("'A' 'B' 'C' vagy 'V': ")
        v = valasz.upper()
        if v == 'A' or v == 'B' or v == 'C':
            if v == 'A':
                return Tarhely.A, v
            elif v == 'B':
                return Tarhely.B, v
            elif v == 'C':
                return Tarhely.C, v
        elif v == 'V':
            break
        else:
            print('Ilyen sajnos nincsen.')
            continue
        
def mentes(mx):
    print("Melyik helyre szeretnéd menteni?")
    print("'V' = vissza")
    while True:
        valasz = input("'A' 'B' 'C' vagy 'V': ")
        v = valasz.upper()
        if v == 'A' or v == 'B' or v == 'C':
            print("\nMátrix '{}' néven menve!\n".format(v))
            if v == 'A':
                Tarhely.A = mx
                break
            elif v == 'B':
                Tarhely.B = mx
                break
            elif v == 'C':
                Tarhely.C = mx
                break
        elif v == 'V':
            break
        else:
            print('Ilyen sajnos nincsen. ')
            continue

def kiir_menu():
    cls()
    print('*******__MÁTRIXOK_KIÍRÁSA__*******\n')
    while True:
        print('Válassz opciót!')
        print('1. Képernyőre')
        print('2. Fájlba (.txt)')
        print('9. Vissza a főmenübe\n')
        valasz = input('Válasz: ')
        try:
            v = int(valasz)
            if v == 1:
                kepernyo_kiir()
            elif v == 2:
                fajl_kiir()
            elif v == 9:
                break
            else:
                print('Ilyen opció sajnos nincs.')
        except ValueError:
            print('Kérlek számot adj meg')
            continue

def kepernyo_kiir():
    cls()
    print('**Képernyőre kiír**\n')
    while True:
        print('Melyiket szeretnéd kiírni?')
        try:
            M, nev = tarhely_valaszt()
            print('{}='.format(nev))
            print(M)
        except TypeError:
            break

def fajl_kiir():
    cls()
    print('**Fájlba írás**\n')
    while True:
        print('Melyiket szeretnéd kiírni?')
        try:
            M, nev = tarhely_valaszt()
            try:
                nev_ment = input('\nMilyen néven?: ')
                fajlmuveletek.export(M, nev_ment)
                print("\nMátrix '{}' '{}' néven mentve.\n".format(nev, nev_ment))
                break
            except:
                print('Speciális karakterekkel ne is próbálkozz.\n')
        except TypeError:
            break

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    while True:
        cls() 
        print('*******__FŐMENÜ__*******\n')
        print('Válassz az alábbi lehetőségek közül:')
        print("0. Mátrix bevitel")
        print('1. Mátrixműveletek')
        print('2. Mátrix kiírása')
        print('42. KILÉP\n')
        valasz = input('Almenü: ')
        try:
            valasz = int(valasz)
        except:
            print('Kérlek számot adj meg')
            continue
        if valasz == 0:
            import_menu()
        elif valasz == 1:
            muveletek()
        elif valasz == 2:
            kiir_menu()
        elif valasz == 42:
            break
        else:
            print('Ilyen opció sajnos nincs.')

main()
