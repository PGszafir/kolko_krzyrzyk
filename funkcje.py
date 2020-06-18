def fun1():
  print('spis funkcji')

def iter3(tab,znak,pole,nr):
    a=0
    for j in range(3):#sprawdzanie dla danego pola znaków na polach odległych o nr
        if(tab[pole+j*nr]==znak):
            a+=1
    return(a,pole,znak)#zwraca ile pól ma pożądany znak,liczac od pole


class ZłePoleEx:#(Exception):
    def __init__(self,value,plansza,znak):
        self.value=value
        if value==0:
            ruchGracza(plansza,znak)

    def __str__(self):
        return repr(self.value)



class Plansza:
    def __init__(self):
        self.tab=[' ' for i in range(9)]

    def rys_plansza(self):
        for i in range(0, 9):
            if (i % 3 == 0):
                print('\n')
            print(self.tab[i], '|', end='')

    def wczytajPole(self, znak,pole):

        if 9 >= pole and pole >= 1 and self.tab[pole-1] == ' ':
            self.tab[pole-1] = znak
        else:
            ZłePoleEx(0,self,znak)#raise ZłePoleEx(0,self,znak)


    def sprawdz(self):

        # LINIA +1
        # PION +3
        # SKOS LEWO +2
        # SKOS PRAWO +4
        zn = ['O', 'X']
        a1=b1=c1=(0,0,0)
        for z in zn:#poziom
            for i in range(0, 7, 3):  # +1
                a = iter3(self.tab, z, i, 1)
                if a[0]>0:
                    a1=a
                #print(a)
                if a[0] == 3:
                    print('Koniec Gry wygrywa a:', a[2])
                    return (a)
            for i in range(3):#pion
                b = iter3(self.tab,  z, i, 2)
                if b[0]>0:
                    b1=b
                #print(b)
                if b[0] == 3:
                    print('Koniec Gry wygrywa b:',b[2])
                    return b
            for i in range(0, 3, 2):#skos
                c = iter3(self.tab, z, i, 4 - i)
                if c[0]>0:
                    c1=c
                #print(c)
                if c[0] == 3:
                    print('Koniec Gry wygrywa c:', c[2])
                    return c


        if a1[0]>=b1[0]and a1[0]>=c1[0]:
            return a1
        elif b1[0]>c1[0]:
            return b
        else:
            return c



# def pytaj(i):
# i=int(input('gracz',i,'proszę podać nr pola'))

def blokuj(plansza,znak):
    pass

def wygraj(plansza,znak):
    pass

import random as rand

def ruchKomp(plansza,znak):
    a=plansza.sprawdz()
    print(a)
    if(a[0]==2):
        print('gracz',a[2],'blisko wygranej')
        if a[2]==znak:
            a[0]
            wygraj(plansza,znak)
        else:
            blokuj(plansza,znak)
    elif(a[0]==3):
        print('KONIEC')
    else:
        plansza.wczytajPole(znak,rand.randint(1,9))


def ruchGracza(plansza,znak):
    i = int(input('podaj nr pola'))
    plansza.wczytajPole(znak, i)

def pierwszy_etap(plansza):
    plansza=Plansza()
    print("to pierwszy estp gry w którym kazdy z graczy może napirzemian dołozyć 3 pionki")
    plansza.rys_plansza()
    znak=input('wybierz znak jakim chcesz grać O lub X')
    if znak in 'Xx':
        for j in range(3):
            ruchGracza(plansza,'X')
            ruchKomp(plansza,'O')
            print('')
            plansza.rys_plansza()
            print('')
    elif znak in 'o0O':
        for j in range(3):
            ruchKomp(plansza,'X')
            ruchGracza(plansza,'O')
            print('grasz O')
            plansza.rys_plansza()
            print('')
    a=plansza.sprawdz()
    if a[0]==3:
        return 0
    return plansza,znak


def drugi_etap(plansza,znak):
    print('Drugi Etap')
    print('Grasz:',znak)
    plansza.rys_plansza()


