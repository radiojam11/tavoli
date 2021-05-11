# TecnoGeppetto Maggio 2021
# Si tratta di un sistema di prenotazione tavoli di un ristorante 
# Il sistema consente di prenotare  attraverso un operatore, tavoli di un ristorante,, 
# verra' sviluppata anche una interfaccia grafica che consente di posizionare i tavoli nello spazio 
# E selezionare i tavoli in modo grafico, clickando sull icona del tavolo nella sala virtuale
# 
# Il Sistema consente di gestire piu' locali 
# 
# Il Tavolo ha le seguenti caratteristiche:
# N max di persone possibile
# N. minimo di persone possibile 
# N. minimo serataFull (valido se il parametro serataFull = True)
# apparecchiato = True/False
# fiori/luci = True/False
# locale_coordinate =  {"locale":codice_locale,"sala":1, "latoX":3, "latoY":5}
# prenotazione = [(id_Cliente,time), (id_Cliente,time),....] in fase di prenotazione da evitare accavallamenti di time+tempo_servizio 
#  #




from time import time , ctime
from math import modf
from testo import banner 

# gestione del tempo
# now = time.ctime()
# parsed = time.strptime(now)
# print(time.strftime("%a %b %d %H:%M:%S %Y", parsed))


# serataFull = 65  ( se gia' prenotato il 65% dei tavoli ) 
serataFull = 70

# tempo_s = 1  #espresso in ore.minuti cioe' (ore 1 e minuti 45 = 1.45)
# variabile da locale a locale ( es. pizzeria 50 minuti - ristorante alla carta 2ore)
def servizio(tempo_s):
    """Ritorna il conteggio del tempo del servizio (passato come ore.minuti) in numero di secondi """
    minuti, ore = modf(tempo_s)
    return ore*3600+(int(minuti*100)*60)

class Tavolo():
    def __init__(self, n_max=4, n_min=1, n_min_s=3, app=False, acc=False, loc_coor={"locale":1, "sala":1, "latoX":1, "latoY":1}, prenot=[(1,1620548163)] ):
        self.n_max = n_max
        self.n_min = n_min
        self.n_min_s = n_min_s
        self.app = app
        self.acc = acc
        self.loc_coor = loc_coor
        self.prenot = prenot

class Cliente():
    def __init__(self, nome="", cognome="", n_tel="", social={"twitter":None, "instagram":None, "facebook":None, "telegram":None, }, id=None):
        self.nome = nome
        self.cognome = cognome
        self.n_tel = n_tel
        self.social = social
        self.id = id


class Cameriere():
    def __init__(self, nome="", cognome="", id=None, tavoli=[]):
        self.nome = nome
        self.cognome = cognome
        self.id = id
        self.tavoli = tavoli


class Prenotazioni():
    def __init__(self, id=None, tavolo=None, ora=None):
    pass



def main():
    print(banner)
    t = time()
    print(t)
    print(ctime(int(t)))



if __name__ == '__main__':
	main()
