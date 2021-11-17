import os, sys, time
from webradio_link import stazioni


class TerminalRadio:

    def __init__(self, radio="Radio1"):
        self.radio = radio

    def list_radio(self):
        """ channel name list """
        print("--------------------------")
        print("|    Channel list name   |")
        print("--------------------------")
        # x = "Virgin Radio"
        # print(stazioni[x])
        for i in stazioni:
            print(i)

    def run(self):
        """ run """
        self.list_radio()
        print("--------------------------")
        print("Scrivi il nome della radio")
        print(" [q] --- per cambio canale")
        print(" [0] --- per chiudere app ")
        print("--------------------------")
        select = input()
        print("--------------------------")
        if select == '0':
            sys.exit()
        else :
            try :
                print(" [q] --- per cambio canale")
                print(" [0] --- per chiudere app ")
                os.system(stazioni[select])
            except (ValueError, KeyError) :
                print("Valore Inserito non Valido !!!\n\n\n")
                time.sleep(2)


    def add_radio(self):
        """add radio channel in list  """
        name = input("inserisci il nome : ")
        url = input("inserisci l'url valido ")
        stazioni[name] = "mpv " + url
        data = open("webradio.txt","a")
        data.write(f"\n{name}:mpv {url}")
        data.close()




x = TerminalRadio()

while True:
    x.run()
