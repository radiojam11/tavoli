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




# serataFull = 65  ( se gia' prenotato il 65% dei tavoli ) 
from time import time , ctime
from math import modf

serataFull = 70
# tempo_s = 1  #espresso in ore.minuti cioe' (ore 1 e minuti 45 = 1.45)
def servizio(tempo_s):
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



print(servizio(0.30))







cliente = Cliente(nome="mario")
print(cliente.nome, cliente.social["twitter"])



t = time()
print(t)
print(ctime(int(t)))