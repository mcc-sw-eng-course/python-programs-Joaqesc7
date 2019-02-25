import os
from errors import InvalidValue, InvalidInput, InvalidExtension


class SortBigList:

    def __init__(self, input_file=None, output_file=None):
        self.input_file = input_file
        self.output_file = output_file

    def set_input_data(self, file_path_name):
        try:
            if not os.path.isfile(file_path_name):
                raise InvalidValue

            elif not isinstance(file_path_name, str):
                raise InvalidInput

            elif '.csv' not in file_path_name:
                raise InvalidExtension

            else:
                self.input_file = file_path_name

        except InvalidValue:
            print ('File does not exist in path')

        except InvalidInput:
            print ('File name must be a string')

        except InvalidExtension:
            print ('File name must end with csv')

    def set_output_data(self, file_path_name):
        try:
            if not isinstance(file_path_name, str):
                raise InvalidInput

            elif '.csv' not in file_path_name:
                raise InvalidExtension

            else:
                self.output_file = file_path_name

        except InvalidInput:
            print ('File name must be a string')

        except InvalidExtension:
            print ('File name must end with csv')

    def execute_merge_sort(self):
        big_list = file.read(self.input_file)
        
        if len(big_list) > 1:
            half = len(big_list)//2
            left = big_list[:half]
            right = big_list[half:]
            
            self.execute_merge_sort(left)
            self.execute_merge_sort(right)
            
            i = 0
            j = 0
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    big_list[k] = left[i]
                    i += 1
                else:
                    big_list[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                big_list[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                big_list[k] = right[j]
                j += 1
                k += 1
            
            return big_list

