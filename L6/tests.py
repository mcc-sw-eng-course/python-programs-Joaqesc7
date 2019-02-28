import sort
import unittest

class TestSort(unittest.TestCase):
    """
    Create test cases for the functions created in the sort file
    """

    def test_set_input_data(self):
        """
        Test that the function catches when input file does not exists
        :return:
        """
        list = sort.SortBigList()
        self.assertEqual(list.set_input_data('files/no.csv'), 'File does not exist in path')

    def test_set_input_data_int(self):
        """
        Test that the function catches when input file is not a string
        :return:
        """
        list = sort.SortBigList()
        self.assertEqual(list.set_input_data(666), 'File name must be a string')

    def test_set_input_data_csv(self):
        """
        Test that the function catches if the file is not of csv extension
        :return:
        """
        list = sort.SortBigList()
        self.assertEqual(list.set_input_data('files/no.txt'), 'File name must end with csv')

    def test_set_input_data_success(self):
        """
        Test that the function can successfully set the input file
        :return:
        """
        list = sort.SortBigList()
        self.assertEqual(list.set_input_data('files/yes.csv'), 'OK')

    def test_set_output_data_success(self):
        """
        Test that the function can successfully set the output file
        :return:
        """
        list = sort.SortBigList()
        self.assertEqual(list.set_output_data('files/final.csv'), 'OK')

    def test_set_output_data_int(self):
        """
        Test that the function catches is name is not a string
        :return:
        """
        list = sort.SortBigList()
        self.assertEqual(list.set_output_data(666), 'File name must be a string')

    def test_set_output_data_csv(self):
        """
        Test that the function catches that the output file is not csv format
        :return:
        """
        list = sort.SortBigList()
        self.assertEqual(list.set_output_data('files/no.txt'), 'File name must end with csv')

    def test_merge_sort_success(self):
        """
        Test that the function can perform a sort and write out the file
        :return:
        """
        list = sort.SortBigList()
        list.set_input_data('files/yes.csv')
        list.set_output_data('files/final.csv')
        self.assertEqual(list.execute_merge_sort(list), 'Output file created')

    def test_merge_sort_fail(self):
        """
        Test that the function catches is bad format inside file
        :return:
        """
        list = sort.SortBigList()
        list.set_input_data('files/yes2.csv')
        list.set_output_data('files/final.csv')
        self.assertEqual(list.execute_merge_sort(list), 'File must contain numbers separated by commas only')




if __name__ == '__main__':
    unittest.main()