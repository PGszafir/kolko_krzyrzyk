def fun1():
  print('spis funkcji')


class Plansza:
    def __init__(self):
        self.tab=[' ' for i in range(9)]

    def rys_plansza(self):
        for i in range(0, 9):
            if (i % 3 == 0):
                print('\n')
            print(tab[i], '|', end='')













plwzorc = []
for i in range(0, 9):
    plwzorc.append(i + 1)



# def pytaj(i):
# i=int(input('gracz',i,'proszę podać nr pola'))

def iter3(tab,znak,pole,nr):
    a=0
    for j in range(3):
        if(tab[pole+j*nr]==znak):
            a+=1
    return(a,pole,znak)

def sprawdz(tablica):
    zn=['O','X']
    for z in zn:
        for i in range(0,7,3):#+1
            a=iter3(tablica,z,i,1)
            print(a)
            if a[0]==3:
                return(a)
        for i in range(3):
            b=iter3(tablica, z, i, 2)
            print(b)
            if b[0]==3:
                return b
        for i in range(0,3,2):
            c=iter3(tablica, z, i,4-i)
            print(c)
            if c[0]==3:
                return c
    return max(a,b,c)
# LINIA +1
# PION +3
# SKOS LEWO +2
# SKOS PRAWO +4
def wczytajPole(plansza,znak):
    text=['\ngracz ', znak, 'proszę podać nr pola']
    gracz1 = int(input(text))
    if 9 >= gracz1 and gracz1 >= 1 and plansza[gracz1] == ' ':
        plansza[gracz1] = znak
    else:
        print('error')
        wczytajPole(plansza,znak)
def ruchKomp(plansza,znak):
    a=sprawdz(plansza)
    if(a[2]==znak):
        print('gracz',znak,'blisko wygranej')
    else:
        print('randomiks')


def pierwszy_etap(plansza):
    print("to pierwszy estp gry w którym kazdy z graczy może napirzemian dołozyć 3 pionki")
    rys_plansza(plwzorc)
    znak=input('wybierz znak jakim chcesz grać O lób X')
    if znak=='X':
        wczytajPole(plansza,'X')
        ruchKomp()

    plansza[komputer] = 'O'
    rys_plansza(plansza)