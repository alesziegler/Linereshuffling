import os
from file_creation import FileCreation

class Engine:
    
    def __init__(self):
        self.__path_to_inputs = "Inputs"
        self.__path_to_outputs = "Outputs"

    def create_new_file(self,filename,suffix):
    
        try:
            new_file = self.__path_to_inputs + "/" + filename
            FileCreation(new_file,suffix)
        except Exception as error_message:
            raise Exception(error_message)

    def find_existing_files(self):
        result =""
        for file in os.listdir(self.__path_to_inputs):
            result += file + "\n"
        return result
    
    def write_to_input_file(self,file,line):
        filepath = self.__path_to_inputs + "/" + file
        try:
            with open (filepath,"a") as f:
                f.write(line + "\n")
        except Exception as error_message:
            raise Exception(error_message)
        