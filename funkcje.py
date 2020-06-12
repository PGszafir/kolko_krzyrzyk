def fun1():
  print('spis funkcji')

def iter3(tab,znak,pole,nr):
    a=0
    for j in range(3):
        if(tab[pole+j*nr]==znak):
            a+=1
    return(a,pole,znak)


class ZłePoleEx(Exception):
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
            raise ZłePoleEx(0,self,znak)


    def sprawdz(self):

        # LINIA +1
        # PION +3
        # SKOS LEWO +2
        # SKOS PRAWO +4
        zn = ['O', 'X']
        for z in zn:
            for i in range(0, 7, 3):  # +1
                a = iter3(self.tab, z, i, 1)
                print(a)
                if a[0] == 3:
                    print('Koniec Gry wygrywa:', a[2])
                    return (a)
            for i in range(3):
                b = iter3(self.tab,  z, i, 2)
                print(b)
                if b[0] == 3:
                    print('Koniec Gry wygrywa:',b[2])
                    return b
            for i in range(0, 3, 2):
                c = iter3(self.tab, z, i, 4 - i)
                print(c)
                if c[0] == 3:
                    print('Koniec Gry wygrywa:', c[2])
                    return c
        return max(a, b, c)


# def pytaj(i):
# i=int(input('gracz',i,'proszę podać nr pola'))


def ruchKomp(plansza,znak):
    a=plansza.sprawdz()
    if(a[2]==znak):
        print('gracz',znak,'blisko wygranej')
    else:
        print('randomiks')


def ruchGracza(plansza,znak):
    i = int(input('podaj nr pola'))
    plansza.wczytajPole(znak, i)

def pierwszy_etap(plansza):
    plansza=Plansza()
    print("to pierwszy estp gry w którym kazdy z graczy może napirzemian dołozyć 3 pionki")
    plansza.rys_plansza()
    znak=input('wybierz znak jakim chcesz grać O lub X')
    if znak=='X':
        for j in range(3):
            ruchGracza(plansza,'X')
            ruchKomp(plansza,'Y')
            print('')
            plansza.rys_plansza()
            print('')
    plansza.sprawdz()
    #plansza[komputer] = 'O'
    #rys_plansza(plansza)