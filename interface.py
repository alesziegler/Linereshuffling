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
        self.__new_engine = Engine()
        while not done:
            print("""      
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
                continue  #this somehow prevents repeating invalid message
            """
            if choice == (1 or 2 or 3):
                self.__new_engine = Engine()
            """
            match choice:
                case 1:
                    created_file = self.create_file()
                    additional_choice = input(
                        "Do you wish to write a line into this file? ").lower(
                        )
                    if additional_choice.lower() == "y":
                        self.add_a_line(created_file)
                case 2:
                    self.find_files()
                    file = input(
                        "Write the name of a file to which you wish to add: ")
                    print(file)
                    self.add_a_line(file)
                case 3:
                    self.randomize()
                case 4:
                    print("bye")
                    done = True
                case _:
                    print("Invalid choice. Try again.")

    def create_file(self):
        filename = input("Write the name of your file without suffix: ")
        file_suffix = input("Write suffix of your file: ")

        try:
            self.__new_engine.create_new_file(filename, file_suffix)
            created_file = filename + "." + file_suffix
            return created_file
        except Exception as e:
            print(e)

    def find_files(self):
        print("There are following files: ")
        print(self.__new_engine.find_existing_files())

    def add_a_line(self, file):
        line = input("Write your line: ")
        try:
            self.__new_engine.write_to_input_file(file, line)
        except Exception as e:
            print(e)

    def randomize(self):
        input("choose an input file: ")
