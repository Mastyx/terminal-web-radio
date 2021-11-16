import os, sys
from webradio_link import stazioni


class TerminalRadio:

    def __init__(self, radio="Radio1"):
        self.radio = radio

    def list_radio(self):
        print("--------------------------")
        print("|    List radio names    |")
        print("--------------------------")
        # x = "Virgin Radio"
        # print(stazioni[x])
        for i in stazioni:
            print(i)

    def run(self):
        self.list_radio()
        print("--------------------------")
        select = input("- insert id radio : ")
        print("--------------------------")
        if select == '0':
            sys.exit()
        else :
            os.system(stazioni[select])

    def add_radio(self):
        name = input("inserisci il nome : ")
        url = input("inserisci l'url valido ")
        stazioni[name] = "mpv " + url
        data = open("webradio.txt","a")
        data.write(f"\n{name}:mpv {url}")
        data.close()

    def read_file(self):
        data = open("webradio.txt","r").read()
        print(data)



x = TerminalRadio()

while True:
    x.run()

#
#
#
#
#
#
# def scelta_Stazione(x):
#     if int(x) == 1 :
#         os.system("mpv http://icestreaming.rai.it/1.mp3")
#     elif int(x) == 2 :
#         os.system("mpv http://icestreaming.rai.it/2.mp3")
#     elif int(x) == 3 :
#         os.system("mpv http://icestreaming.rai.it/3.mp3")
#     elif int(x) == 4 :
#         os.system("mpv http://icecast.unitedradio.it/Virgin.mp3")
#     elif int(x) == 5 :
#         os.system("mpv http://radiodeejay-lh.akamaihd.net/i/RadioDeejay_Live_1@189857/master.m3u8")
#     elif int(x) == 0 :
#         print("Alla prossima !!!")
#         sys.exit()
#     else :
#         print('Scelta errata canale non presente nella lista dei possibili  ... ')
#
# while True:
#
#     try :
#         print ("-------------------------------------------------------")
#         print ("Per acoltare la radio selezione il canale e premi invio")
#         print ("-------------------------------------------------------")
#         print ("|   1 - radio 1             |                         |")
#         print ("|   2 - radio 2             |                         |")
#         print ("|   3 - radio 3             |                         |")
#         print ("|   4 - virgin radio        |                         |")
#         print ("|   5 - radio deejay        |                         |")
#         print ("-------------------------------------------------------")
#         print ("|   q - chiudi stazione                               |")
#         print ("|   0 - exit                                          |")
#         print ("-------------------------------------------------------")
#
#         x = input()
#         scelta_Stazione(x)
#     except ValueError:
#         print("Errore inserimento data ...")
