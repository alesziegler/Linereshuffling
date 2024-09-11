import os
import random
from file_creation import FileCreation


class Engine:

    def __init__(self):
        self.__path_to_inputs = "Inputs"
        self.__path_to_outputs = "Outputs"

    def create_new_file(self, filename, suffix):

        try:
            new_file = self.__path_to_inputs + "/" + filename
            FileCreation(new_file, suffix)
        except Exception as error_message:
            raise Exception(error_message)

    def find_existing_files(self):
        result = ""
        for file in os.listdir(self.__path_to_inputs):
            result += file + "\n"
        return result

    def write_to_input_file(self, file, line):
        filepath = self.__path_to_inputs + "/" + file
        try:
            with open(filepath, "a") as f:
                f.write(line + "\n")
        except Exception as error_message:
            raise Exception(error_message)

    def scramble(self,file):
        path_to_input = self.__path_to_inputs + "/" + file
        #How to strip end of the string to a first dot:
        root_name_of_output = file.rsplit('.', 1)
        output = self.__path_to_outputs + "/" + root_name_of_output[0] + ".txt"
        #Line list and count:
        with open(path_to_input, 'r') as input:
            lines = input.readlines()
            line_count = sum(1 for line in lines)
        #this is a list and needs to be converted to string:
        result_list = random.sample(lines, line_count)
        result = ""
        for line in result_list:
            result += line
        #input saving:
        with open(output,"w") as o:
            o.write(result)
        """
        ok, we use readlines, for loop and random, somehow.
        Maybe dictionary with random numbers?
        Line count:
        with open('filename.txt', 'r') as file:
            lines = file.readlines()
            line_count = sum(1 for line in lines)
        Randomization:
        result = random.sample(lines, line_count)
        """
        
