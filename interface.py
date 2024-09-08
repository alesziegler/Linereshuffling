
import os
from engine import Engine

class Interface:

    """
    Ok, we'll have a menu with following options:
    1) create a new input file,
    2) write into existing input file,
    3) make an output file from a given input file 
    """
    
    def __init__(self):
        done = False

        while not done:
            print(
            """      
            What do you want to do? \n
            1) Create new file.\n
            2) Add to existing file.\n
            3) Randomize existing file.\n
            4) Quit.
            """)

            choice = input("Choose here: ")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice. Try again.")
                #continue

            if choice is (1 or 2 or 3):
                self.__new_engine = Engine()
            
            match choice:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    self.randomize()
                case 4:
                    done = True
                case _:
                    print("Invalid choice. Try again.")
        

    def randomize(self):
        input("choose an input file: ")
