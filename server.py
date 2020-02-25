import key_press
import socket
import websocket

#parsing
def Parse(Stringa, Carattere):
    s=""
    for i in range(len(Stringa)):
        if Stringa[i]==Carattere:
            i=i+3
            while((Stringa[i]=="'")or(Stringa[i]=="b")or(Stringa[i]==":")or(Stringa[i]=='"'))and i<=len(Stringa):
                i=(i+1)%len(Stringa)
            while (Stringa[i]!=",")and(Stringa[i]!='"')and(Stringa[i]!="'")and(Stringa[i]!="b")and i<=len(Stringa)and(Stringa[i]!="{"):
                s=s+Stringa[i]
                i=(i+1)%len(Stringa)
            return s
    return -1
def Check_modello(modello):
    for i in range(len(lista_connessi)):
        if lista_connessi[i].model==modello:
            return i
    return -1
def Check_comando(parametro, valore, mod): #legenda cooking
    if(parametro=="X"):
        if(valore>mod.valore1):
            return "direzione1" #padella destra
        if(valore<mod.valore2):
            return "direzione2" #padella sinistra
    if(parametro=="Y"):
        if (valore < mod.valore3):
            return "direzione3" #padella avanti
        if (valore > mod.valore4):
            return "direzione4" #padella indietro

class mode:
    def __init__(self, v1, v2, v3, v4, d1, d2, d3, d4):
        self.valore1 = v1
        self.valore2 = v2
        self.valore3 = v3
        self.valore4 = v4
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4

#modalità
drive=mode("410","280","510","690", "a", "i", "s", "d")
rdrive=mode("340","270","510","610", "i", "a", "d", "s")
cook=mode("670","440","500","610", "d", "s", "a", "i")

class connessioni:
    def __init__(self, addr, conn, mod):
        self.address=addr
        self.connection=conn
        self.model=mod

host = '192.168.43.209'
port = 255
port_interface = 256

lista_connessi = [] #lista connessi
connected = 2  #numero di connessioni accettate

#creazione socket
s=socket.socket()
s.bind((host, port))
s.listen()

stringa=""
waiter=0 #iteratore
piattaforma=""

print("Server Partito")

while waiter < connected:
    conn, addr = s.accept()
    s.setblocking(1)

    if '192.168.43.162' in addr:
        modello="macchina"
    if '192.168.43.188' in addr:
        modello="controller"
    if ((len(lista_connessi) == 0)or(Check_modello(modello))==-1):
        a=connessioni(addr,conn,modello)
        lista_connessi.append(a)
        print('Connected by', a.address[0], 'Tipo', a.model )
        waiter = waiter + 1
    indice = Check_modello("controller")
    controller = lista_connessi[indice].connection
    indice = Check_modello("macchina")
    macchina = lista_connessi[indice].connection

while True:  #while generale
    #configurazione
    stringa=""
    print("Modalita' configurazione interfaccia")
    websocket.importConfig(host, port_interface)

    if(Parse(websocket.config, "M")=="1"):
        modalita=drive
        piattaforma="macchina"
        print("Modalità Drive- Car")
    if(Parse(websocket.config, "M")=="2"):
        modalita=drive
        piattaforma="steam"
        print("Modalità Drive- Steam")
    if (Parse(websocket.config, "M") == "3"):
        modalita = cook
        piattaforma = "macchina"
        print("Modalità Cooking- Car")
    if (Parse(websocket.config, "M") == "4"):
        modalita = cook
        piattaforma = "steam"
        print("Modalità Cooking- Steam")
    if (Parse(websocket.config, "M") == "5"):
        modalita = rdrive
        piattaforma = "macchina"
        print("Modalità Reverse Drive- Car")
    if (Parse(websocket.config, "M") == "6"):
        modalita = rdrive
        piattaforma = "steam"
        print("Modalità Reverse Drive- Steam")

    port_interface+=1

    while True: #while utilizzo
        data = str(controller.recv(20480))
        stringa = stringa + data
        if ("}" in stringa):
            split = stringa.split("}", 1)
            buona=split[0]
            stringa=split[1]
            comandoX=Check_comando("X", Parse(buona, "X"), modalita)
            comandoY=Check_comando("Y", Parse(buona, "Y"), modalita)
            if("true" in buona):
                print("Exiting modalita' di utilizzo")
                break
            if(comandoX=="direzione1"):
                 print(modalita.d1)
                 if(piattaforma=="steam"):
                    key_press.Press(modalita.d1)
                 if(piattaforma=="macchina"):
                    macchina.send(str.encode(modalita.d1))
            if (comandoX == "direzione2"):
                print(modalita.d2)
                if (piattaforma == "steam"):
                    key_press.Press(modalita.d2)
                if (piattaforma == "macchina"):
                    macchina.send(str.encode(modalita.d2))
            if (comandoY == "direzione3"):
                print(modalita.d3)
                if (piattaforma == "steam"):
                    key_press.Press(modalita.d3)
                if (piattaforma == "macchina"):
                    macchina.send(str.encode(modalita.d3))
            if (comandoY == "direzione4"):
                print(modalita.d4)
                if (piattaforma == "steam"):
                    key_press.Press(modalita.d4)
                if (piattaforma == "macchina"):
                    macchina.send(str.encode(modalita.d4))
