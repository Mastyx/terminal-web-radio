import os, sys, time, json
from elements import SCRITTA

class TerminalRadio:

    def __init__(self, radio="Radio1"):
        self.radio = radio
        # popoliamo il dizionari con la lista delle stazioni
        load_stazioni = open("mydict.dic", "r")
        self.stazioni = json.load(load_stazioni)

    def list_radio(self):
        """ channel name list """
        print(SCRITTA)
        print("\n---------------------------------------------------------")
        print("|            Enter the name of the web radio            |")
        print("---------------------------------------------------------")
        colonne = 0
        for i in self.stazioni:
            colonne = colonne + 1
            if colonne%3 == 0:
                print("", i,end="\t\n")
            else :
                print("\t".expandtabs(1), i,"\t",end="")

    def run(self):
        """ run """
        self.list_radio()
        print("\n---------------------------------------------------------")
        print(" [q] --- change channel     |   [l] --- Channel list")
        print(" [0] --- close application  |   [a] --- Add channel ")
        print(" [s] --- save list radio    |   [r] --- Remove Radio")
        print("---------------------------------------------------------")
        select = input("-> ")
        if select == '0':
            sys.exit()
        elif select == "a":
            self.add_radio()
        elif select == "l":
            self.list_radio()
        elif select == "s":
            self.save_radio()
        elif select == "r":
            self.remove_radio()
        else :
            try :
                os.system(self.stazioni[select])
            except (ValueError, KeyError) :
                print("Valore Inserito non Valido !!!\n\n\n")
                time.sleep(2)

    def save_radio(self):
        try :
            file = open("mydict.dic","w")
            json.dump(self.stazioni, file)
            print("List save successfully !!! ")
            time.sleep(2)
            file.close()
        except :
            print("Errore di scrittura, file non savato !!! ")
            time.sleep(2)

    def add_radio(self):
        """add radio channel in list  """
        name = input("Inserisci il nome : ")
        url = input("Inserisci l'url valido : ")
        self.stazioni[name] = "mpv " + url
        self.save_radio()

    def remove_radio(self):
        print(" --- Remove radio from list -- ")
        try:
            name = input(" Inserisci il nome : ")
            del self.stazioni[name]
            print(f"{name} has been removed !!! ")
            time.sleep(2)
            self.save_radio()

        except KeyError:
            print("Value not present !")
            time.sleep(2)


def main():
    myTerminalRadio= TerminalRadio()
    while True:
        myTerminalRadio.run()

if __name__ == "__main__":
    main()
