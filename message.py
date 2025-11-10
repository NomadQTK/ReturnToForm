import sys
import random

class Spiels:

    def __init__(self):
        self.NOCSpiels = [["Requesting for parallel checking", "Asking for your assistance on parallel checking", "May we request parallel checking for..."],
              ["Copy on this, checking", "This is already on going", "This is noted, we will proceed with checking"],
              ["Sir M is Daddy", "Sir J is Uncle", "Sir R is Grandpa"]]
    
 
    def Parallel(self, choice):
        choice = int(choice)
        if choice == 1:
            self.randomize()
            print(self.NOCSpiels[0][self.randNO])
        if choice == 2:
            self.randomize()
            print(self.NOCSpiels[1][self.randNO])
        if choice == 3:
            self.randomize()
            print(self.NOCSpiels[2][self.randNO])
        

    def randomize(self):
        self.randNO = random.randint(0, 2)

class MainApp:
    def __init__(self):
        self.Spiels = Spiels()
        self.choices = ["1", "2", "3"]

    def Menu(self):
        FirstMessage=r"""   
        =========================================================
                 __  ___  ___     _           _     _               
              /\ \ \/___\/ __\   /_\  ___ ___(_)___| |_ 
             /  \/ //  // /     //_\\/ __/ __| / __| __|
            / /\  / \_// /___  /  _  \__ \__ \ \__ \ |_ 
            \_\ \/\___/\____/  \_/ \_/___/___/_|___/\__|
        =========================================================
        """

        print(FirstMessage)
        print("This is CLI application produces sample Spiels for NOC Engineers when coordinating with third-party companies \nor other Departments\n")

        print("1. Request for parrallel checking ")
        print("2. Response to L2 Support  ")
        print("3. Random Kagaguhan \n")
        print("\n 'q' to exit")

    def CMDrun(self):
        self.Menu()
        while True:
            opt = input("Please select an option: ")
            
            if opt == "q": 
                sys.exit()
            if opt in self.choices:
                self.Spiels.Parallel(opt)
            else:
                print("---Please select one of the choices---")
            

            
             
if __name__ == '__main__':
    App = MainApp()
    App.CMDrun()