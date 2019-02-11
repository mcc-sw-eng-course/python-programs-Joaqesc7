import HW2
import unittest

class TestHW2(unittest.TestCase):
    """
    Create test cases for the functions created in homework two
    """

    def test_read_from_file(self):
        """
        Test that the function can succesfully read from file and return a list
        :return:
        """
        self.assertEqual(HW2.myPowerList().readFromTextFile('file.txt'), ['test'])

    def test_read_no_file(self):
        """
        Test that the function will return proper exception when file doesn't exist
        :return:
        """
        self.assertEqual(HW2.myPowerList().readFromTextFile('no_file.txt'), 'File Not Found')

    def test_add_contact(self):
        """
        Test that a conctac can be added successfully
        :return:
        """
        self.assertEqual(HW2.Contacts().addContact('Name', 'Address', 'Phone', 'Email'), 'Contact Added')

    def test_read_contacts_from_file(self):
        """
        Test that the function can succesfully read from file and return a list
        :return:
        """
        self.assertEqual(HW2.Contacts().getRecords('test_records.txt'), ['test'])

    def test_read_contacts_no_file(self):
        """
        Test that the function will return proper exception when file doesn't exist
       :return:
        """
        self.assertEqual(HW2.Contacts().getRecords('no_file.txt'), 'File Not Found')

    def test_search_records(self):
        """
        Test that text can be successfully read from file
        :return:
        """
        self.assertEqual(HW2.Contacts().searchRecord('test','test_records.txt'), ['test'])

if __name__ == '__main__':
    unittest.main()