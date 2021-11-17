import os, sys, time
from webradio_link import stazioni


class TerminalRadio:

    def __init__(self, radio="Radio1"):
        self.radio = radio

    def list_radio(self):
        """ channel name list """
        print("\n--------------------------")
        print("|    Channel list name   |")
        print("--------------------------")

        # x = "Virgin Radio"
        # print(stazioni[x])
        colonne = 0
        for i in stazioni:
            colonne = colonne + 1
            if colonne%3 == 0:
                print("\t| ", i,end="\n")
            else :
                print("\t| ", i,end="")



    def run(self):
        """ run """
        self.list_radio()
        print("\n----------------------------------------------------")
        print("WRITE THE NAME OF THE RADIO")
        print(" [q] --- change channel    | [l] --- Channel list")
        print(" [0] --- close application | [a] --- Add channel ")
        print("----------------------------------------------------")
        select = input("-> ")
        if select == '0':
            sys.exit()
        elif select == "a":
            self.add_radio()
        elif select == "l":
            self.list_radio()
        else :
            try :
                os.system(stazioni[select])
            except (ValueError, KeyError) :
                print("Valore Inserito non Valido !!!\n\n\n")
                time.sleep(2)


    def add_radio(self):
        """add radio channel in list  """
        name = input("inserisci il nome : ")
        url = input("inserisci l'url valido : ")
        stazioni[name] = "mpv " + url
        # data = open("webradio.txt","a")
        # data.write(f"\n{name}:mpv {url}")
        # data.close()




x = TerminalRadio()

while True:
    x.run()
