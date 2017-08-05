from multiprocessing import Value, Lock
from SendKeys import SendKeys
from os import system, _exit
from time import sleep
from win32api import SetCursorPos, mouse_event
from win32api import keybd_event
from win32con import MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from keywords import *
from sub import *


class semaforo(object):
    def __init__(self, initval=0):
        self.m = [Value('i', initval) for i in range(9)]
        self.lock = Lock()
        self.carregaOpc()

    def setState(self, ID, value):
        with self.lock:
            print '\nMacro:', ID, 'state: ', value
            self.m[ID].value = value

    def getState(self, ID):
        with self.lock:
            return self.m[ID].value

    def getLAG(self):
        return self.LAG

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def getSenha(self):
        return self.senha

    def getSub(self):
        return self.subSeha

    def getNick(self):
        return self.nick

    def getTIME(self):
        return self.time

    def carregaOpc(self):
        with self.lock:
            try:
                f = open("config/config.cfg", "r")
                linha = f.read()
                self.posx, self.posy, self.senha, self.subSeha, self.nick, self.LAG, self.time = linha.split(",")
                f.close()
                self.time = int(self.time) * 10
                self.posx = int(self.posx)
                self.posy = int(self.posy)
                print 'Lag: ', self.LAG
                self.LAG = (float(self.LAG) / 1000) + 0.5
                print 'Lag: ', self.LAG
            except:
                print 'Please fix your configuration files'
                print linha.split(',')
                system('timeout 10')
                _exit(0)

    def carregaMacros(self):
        with self.lock:
            try:
                f = open("config/macros.cfg", "r")
                self.macro = f.read().split('\n')
                f.close()
            # print self.macro
            except:
                print 'Please fix your Macro files'
                system('timeout 10')
                _exit(0)

    def getComandos(self, macroNum):
        self.carregaMacros()
        with self.lock:
            return self.macro[macroNum]


def press(KEY, TIME=0.01):
    keybd_event(1, KEY, 0, 0)
    sleep(TIME)
    keybd_event(1, KEY, 0x0002, 0)


def arrasta_Rigth(x1, y1, x2, y2):
    x1, y1 = int(x1), int(y1)
    sleep(0.5)
    SetCursorPos((x1, y1))
    mouse_event(MOUSEEVENTF_RIGHTDOWN, x1, y1, 0, 0)
    sleep(0.5)
    SetCursorPos((x2, y2))
    sleep(0.5)
    mouse_event(MOUSEEVENTF_RIGHTUP, x2, y2, 0, 0)
    sleep(0.5)


def click_right(x, y):
    x, y = int(x), int(y)
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    # sleep(0.1)
    mouse_event(MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def click_left(x, y):
    x, y = int(x), int(y)
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    # sleep(0.1)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def worker(ID, macros):
    from time import sleep
    while 1:
        if macros.getState(ID) == 1:
            comandos = macros.getComandos(ID)
            # print comandos
            x = 0
            while x < len(comandos):
                c = comandos[x]
                # print c
                if c == ' ':
                    press(KEY_SPC)
                if c == 'z':
                    press(KEY_Z)
                if c == '1':
                    press(KEY_1)
                if c == '2':
                    press(KEY_2)
                if c == '3':
                    press(KEY_3)
                if c == '4':
                    press(KEY_4)
                if c == '5':
                    press(KEY_5)
                if c == '6':
                    press(KEY_6)
                if c == '7':
                    press(KEY_7)
                if c == '8':
                    press(KEY_8)
                if c == '9':
                    press(KEY_9)
                if c == '0':
                    press(KEY_0)
                if c == '-':
                    press(KEY_MI)
                if c == '+':
                    press(KEY_AD)
                if c == '{':
                    if comandos[x + 1:x + 5] == 'wait':
                        tempo = int(comandos[x + 5:x + 9])
                        # print tempo
                        sleep(tempo / 1000)
                        x = x + 9
                    elif comandos[x + 1:x + 6] == 'sleep':
                        tempo = int(comandos[x + 6:x + 10])
                        # print tempo
                        sleep(tempo)
                        x = x + 10
                x += 1
    return


def iniciaDG(semaforo):
    from time import sleep
    LAG = semaforo.getLAG()
    click_left(525, 525)  # Inicia DG
    sleep(1 + LAG)


def andaGluto(semaforo):
    from time import sleep
    LAG = semaforo.getLAG()
    x, y = 837, 115
    sleep(0.5)
    SetCursorPos((x, y))
    sleep(0.5)
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    sleep(2)
    press(KEY_D, 0.2)
    sleep(2)
    press(KEY_D, 0.2)
    sleep(2)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    press(KEY_W, 1)


def saiDG(semaforo):
    from time import sleep
    LAG = semaforo.getLAG()
    click_left(1075, 700)  # cabal menu
    sleep(0.5)
    click_left(1036, 407)  # DG
    sleep(0.5)
    click_left(1208, 437)  # exit DG
    sleep(0.5)
    click_left(642, 418)  # acept
    sleep(0.5 + LAG)


def vaiEntradaSiena(semaforo):
    from time import sleep
    LAG = semaforo.getLAG()
    sleep(1)
    arrasta_Rigth(840, 300, 1050, 170)
    x, y = 640, 100
    sleep(0.5)
    SetCursorPos((x, y))
    sleep(1)
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    sleep(0.02)
    arrasta_Rigth(800, 200, 30, 400)
    sleep(1)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    sleep(3 + LAG)


def entraDgGema(semaforo):
    from time import sleep
    LAG = semaforo.getLAG()
    click_left(780, 560)  # entra DG com gemas
    sleep(1 + LAG)


def entraDgItem(semaforo):
    from time import sleep
    LAG = semaforo.getLAG()
    click_left(680, 560)  # entra DG com Item
    sleep(1 + LAG)


def farmaSiena(ID, semaforo):
    LAG = semaforo.getLAG()
    TIME = semaforo.getTIME()
    while True:
        vaiEntradaSiena(semaforo)
        entraDgItem(semaforo)
        sleep(5 + LAG)
        iniciaDG(semaforo)
        sleep(1 + LAG)
        andaGluto(semaforo)
        semaforo.setState(0, 1)
        for decMin in range(TIME):
            if semaforo.getState(ID) == 1:
                sleep(6)
            else:
                print 'aborting bot'
                semaforo.setState(0, 0)
                return
        semaforo.setState(0, 0)
        sleep(3)
        saiDG(semaforo)
        sleep(3 + LAG)


def quebraItens(semaforo):
    larguraItem = 2
    alturaItem = 1
    inventorySize = 64 / (larguraItem * alturaItem)
    LAG = semaforo.getLAG()
    TIME = semaforo.getTIME()
    x0, y0 = (1220, 415)
    click_left(1231, 641)  # abrequebra
    for linha in range(8 / alturaItem):
        print linha
        for coluna in range(8 / larguraItem):
            print coluna
            # click_left(1170,380) #Select tab
            sleep(LAG)
            click_left(x0 + (larguraItem * coluna * 26), y0 + (alturaItem * linha * 26))
            sleep(LAG)
            print x0 + (coluna * 26), y0 + (coluna * 26)
            click_left(721, 535)  # Item Extract
            sleep(LAG)
            click_left(722, 509)  # Agree
            sleep(LAG)
            click_left(730, 600)  # Acept itens
            sleep(LAG)
    print "Terminei"


def criaItens(ID, semaforo):
    LAG = semaforo.getLAG()
    TIME = semaforo.getTIME()
    while True:
        if semaforo.getState(ID) == 0:
            break
        click_left(320, 510)  # Cria
        sleep(0.3)
        click_left(633, 80)  # recebe
        sleep(0.2)


def abreItens(ID, semaforo):
    LAG = semaforo.getLAG()
    TIME = semaforo.getTIME()
    while True:
        if semaforo.getState(ID) == 0:
            break
        click_right(1072, 428)  # Cria
        sleep(0.2)
        click_right(1128, 428)  # Cria
        sleep(0.2)
        click_right(1180, 428)  # Cria
        sleep(0.2)
        click_right(1238, 428)  # Cria
        sleep(0.2)


def criaChar(ID, semaforo):
    from time import sleep
    global posx, posy
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(1750, 347)  # abre cria
    if esperaOciosa(ID, semaforo, 5): return
    SendKeys(semaforo.nick)
    if esperaOciosa(ID, semaforo, 0.1): return
    click_left(1650, 640)  # escolhe AA
    if esperaOciosa(ID, semaforo, 0.1): return
    click_left(1700, 800)  # cria
    if esperaOciosa(ID, semaforo, 5): return
    loga()


def loga():
    from time import sleep
    global posx, posy
    click_left(1700, 780)  # entra
    sleep(0.5)


def recompensa():
    from time import sleep
    press(KEY_I)
    click_left(100, 464)
    click_left(90, 485)
    click_left(153, 100)
    click_left(153, 300)  # 1
    click_left(153, 335)
    click_left(153, 322)  # 2
    click_left(153, 355)
    click_left(153, 348)  # 3
    click_left(153, 383)
    click_left(153, 372)  # 4
    click_left(153, 408)
    click_left(153, 390)  # 5
    click_left(153, 428)
    click_left(153, 418)  # 6
    click_left(153, 454)
    click_left(153, 443)  # 7
    click_left(153, 473)
    click_left(153, 464)  # 8
    click_left(153, 494)
    click_left(80, 520)  # recebe
    sleep(0.5)
    click_left(970, 600)  # ok
    sleep(1)
    click_right(1771, 480)  # abre gema
    sleep(1)
    click_left(970, 600)  # ok
    sleep(0.5)
    # press(KEY_M)
    # sleep(0.5)
    # SetCursorPos((posx,posy))
    print 'Apagando char'


def digitaSub(semaforo):
    p = [(975, 510), (1000, 510), (1028, 510), (1055, 510),
         (975, 538), (1000, 538), (1028, 538), (1055, 538),
         (975, 565), (1000, 565), (1028, 565), (1055, 565)]
    Hash = demuxSub(pegaSub())
    for i in range(len(semaforo.subSeha)):
        d = int(semaforo.subSeha[i])
        print Hash[d]
        if Hash[d] == '00':
            click_left(p[0][0], p[0][1])
        if Hash[d] == '01':
            click_left(p[1][0], p[1][1])
        if Hash[d] == '02':
            click_left(p[2][0], p[2][1])
        if Hash[d] == '03':
            click_left(p[3][0], p[3][1])
        if Hash[d] == '10':
            click_left(p[4][0], p[4][1])
        if Hash[d] == '11':
            click_left(p[5][0], p[5][1])
        if Hash[d] == '12':
            click_left(p[6][0], p[6][1])
        if Hash[d] == '13':
            click_left(p[7][0], p[7][1])
        if Hash[d] == '20':
            click_left(p[8][0], p[8][1])
        if Hash[d] == '21':
            click_left(p[9][0], p[9][1])
        sleep(0.8)
    sleep(0.5)
    click_left(979, 612)


def esperaOciosa(ID, semaforo, tempo):
    if semaforo.getState(ID) == 0:
        print "Parando macro  ", ID
        return True
    else:
        sleep(tempo)


def apagaChar(ID, semaforo):
    press(KEY_O)
    if esperaOciosa(ID, semaforo, 0.3): return
    click_left(950, 505)  # select server
    if esperaOciosa(ID, semaforo, 0.3): return
    click_left(970, 600)  # ok
    if esperaOciosa(ID, semaforo, 4): return
    SendKeys("{ENTER}")
    if esperaOciosa(ID, semaforo, 5): return
    click_left(1885, 363)  # apagar
    if esperaOciosa(ID, semaforo, 1): return
    SendKeys(semaforo.senha)
    if esperaOciosa(ID, semaforo, 0.2): return
    SendKeys("{ENTER}")
    if esperaOciosa(ID, semaforo, 0.2): return
    click_left(960, 600)  # apagar
    if esperaOciosa(ID, semaforo, 1): return
    digitaSub(semaforo)
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(979, 599)
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(979, 599)
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(979, 599)
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(979, 599)
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(979, 599)
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(979, 599)
    if esperaOciosa(ID, semaforo, 0.5): return
    click_left(979, 599)
    if esperaOciosa(ID, semaforo, 0.5): return
    criaChar(ID, semaforo)
    state = (semaforo.getState(5) + 1) % 2
    semaforo.setState(5, state);
