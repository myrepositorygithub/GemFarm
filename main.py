import multiprocessing
import pyHook
import pythoncom
from actions import *
from time import time
import sys,os
from sub import *
from datetime import date


def OnKeyboardEvent(event):
    global ant,macros

    millis = int(round(time() * 1000))
    #print 'KeyID:', event.KeyID,millis-ant
    #print '.',

    if event.KeyID == 97:# 1
        state = (macros.getState(0) + 1 )%2
        macros.setState(0,state);
        #print  'Macro N 1 Activated'
        pass
    if event.KeyID == 98:# 2
        state = (macros.getState(1) + 1 )%2
        macros.setState(1,state);
        #print  'Macro N 1 Activated'
        pass
    if event.KeyID == 99:# 3
        state = (macros.getState(2) + 1 )%2
        macros.setState(2,state);
        #print  'Macro N 1 Activated'
        pass
    if event.KeyID == 100:# 4
        state = (macros.getState(3) + 1 )%2
        macros.setState(3,state);
        if state == 1:
            farmThread = multiprocessing.Process(target=farmaSiena, args=(3,macros,))
            farmThread.start()
        pass
    if event.KeyID == 101:# 5
        state = (macros.getState(4) + 1 )%2
        macros.setState(4,state);
        if state == 1:
            farmThread = multiprocessing.Process(target=quebraItens, args=(macros,))
            farmThread.start()
        pass
    if event.KeyID == 102:# 6
        quebraItens(macros)
        #carregaOpc()
        #state = (macros.getState(3) + 1 )%2
        #macros.setState(3,state);
        pass
    if event.KeyID == 103:# 7
        state = (macros.getState(5) + 1 )%2
        macros.setState(5,state);
        if state == 1:
            farmThread = multiprocessing.Process(target=criaItens, args=(5,macros,))
            farmThread.start()
        #carregaOpc()
        #state = (macros.getState(4) + 1 )%2
        #macros.setState(4,state);
        pass
    if event.KeyID == 104:# 8
        state = (macros.getState(6) + 1 )%2
        macros.setState(6,state);
        if state == 1:
            farmThread = multiprocessing.Process(target=abreItens, args=(6,macros,))
            farmThread.start()
        #loga()
        pass
    if event.KeyID == 105:# 9
        #apagaChar()
        pass
    if event.KeyID == 27:# esc
        #verificaSub()
        #demuxSub(pegaSub())
        macros.carregaOpc()
        print '*************   Loaded Configs   *************'
        #os._exit(0)
    ant = millis
    return True


if __name__ == '__main__':

    d0 = date.today()
    d1 = date(2016, 6, 19)
    delta = d1 - d0
    print delta.days, 'Days of free use'
    if delta.days < 0:
        print '************ Expirado **********'
        os.system('timeout 10')
        os._exit(0)



    hm = pyHook.HookManager()
    multiprocessing.freeze_support()
    m_flag = [0]
    ant = int(round(time() * 1000))


    try:
        f = open('../config/macros.cfg','r')
    except:
        f = open('../config/macros.cfg','r')
        f.write('z{wait9999}\n'*3)
        f.close()
        f = open('../config/macros.cfg','r')

    comandos = f.read().split('\n')
    f.close()
    macros = semaforo(0)
    #macros.carregaOpc()
    #print comandos

    m1 = multiprocessing.Process(target=worker, args=(0,macros,))
    m2 = multiprocessing.Process(target=worker, args=(1,macros,))
    m3 = multiprocessing.Process(target=worker, args=(2,macros,))
    m1.start()
    m2.start()
    m3.start()

    print '*************   Ready   *************'
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
