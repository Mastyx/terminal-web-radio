import os


def scelta_Stazione(x):
    if int(x) == 0 :
        os.system("mpv http://icestreaming.rai.it/1.mp3")
    elif int(x) == 1 :
        os.system("mpv http://icestreaming.rai.it/2.mp3")
    elif int(x) == 2 :
        os.system("mpv http://icestreaming.rai.it/3.mp3")
    elif int(x) == 3 :
        os.system("mpv http://icecast.unitedradio.it/Virgin.mp3")
    elif int(x) == 4 :
        os.system("mpv http://radiodeejay-lh.akamaihd.net/i/RadioDeejay_Live_1@189857/master.m3u8")
    else :
        print('Scelta errata canale non trovato ... ')



while True:

    try :
        print ("Per acoltare la radio selezione il canale e premi invio")
        print (" 0 - radio 1 ")
        print (" 1 - radio 2 ")
        print (" 2 - radio 3 ")
        print (" 3 - virgin radio")
        print (" 4 - radio deejay")
        x = input()
        scelta_Stazione(x)
    except ValueError:
        print("Errore inserimento data ...")
