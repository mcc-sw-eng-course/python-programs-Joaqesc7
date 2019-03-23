import ast
import os
from errors import InvalidValue, InvalidInput, InvalidExtension


class SortBigList:
    """
    This class should be used to sort large amount of data from csv files.
    The class has two properties: input_file and output_file which are
    strings with the information to be used to read from a file and write
    to a file. It also has a merge sort to sort the values read from a file as
    long as the file is properly formatted
    """

    def __init__(self):
        self.input_file = None
        self.output_file = None

    def set_input_data(self, file_path_name):
        try:
            if not isinstance(file_path_name, str):
                raise InvalidInput

            elif not os.path.isfile(file_path_name):
                raise InvalidValue

            elif '.csv' not in file_path_name:
                raise InvalidExtension

            else:
                self.input_file = file_path_name
                return 'OK'

        except InvalidValue:
            return 'File does not exist in path'

        except InvalidInput:
            return 'File name must be a string'

        except InvalidExtension:
            return 'File name must end with csv'

    def set_output_data(self, file_path_name):
        try:
            if not isinstance(file_path_name, str):
                raise InvalidInput

            elif '.csv' not in file_path_name:
                raise InvalidExtension

            else:
                self.output_file = file_path_name
                return 'OK'

        except InvalidInput:
            return 'File name must be a string'

        except InvalidExtension:
            return 'File name must end with csv'

    def execute_merge_sort(self, clean_list):

        try:

            if not isinstance(clean_list, list):
                big_list = open(self.input_file, "r")

                all_text = big_list.read()
                clean_list = list(ast.literal_eval(all_text))

            if len(clean_list) > 1:
                half = len(clean_list)//2
                left = clean_list[:half]
                right = clean_list[half:]

                self.execute_merge_sort(left)
                self.execute_merge_sort(right)

                i = 0
                j = 0
                k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        clean_list[k] = left[i]
                        i += 1
                    else:
                        clean_list[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    clean_list[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    clean_list[k] = right[j]
                    j += 1
                    k += 1

            final_file = open(self.output_file, 'w')
            final_file.write(str(clean_list))
            final_file.close()
            return 'Output file created'

        except ValueError:
            return 'File must contain numbers separated by commas only'

