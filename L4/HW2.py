
class myPowerList:

    def readFromTextFile(self, filename):
        '''
        Load every line of a text file as a list. If file not found will return such error
        :param filename:
        :return: List
        '''

        try:
            with open(filename, 'r') as textfile:
                values = [line.strip() for line in textfile]
                return values
        except:
            return ('File Not Found')


class Contacts:

    def addContact(self, name, address, phone, email):
        """
        Add a record to end of file, the file will be created if non existent. This functions assumes that
        all values are given in the specific order and will not validate the information entered

        :param name: String
        :param address: String
        :param phone: Int
        :param email: String
        :return: Nothing
        """

        user = {
            'Name': name,
            'Address': address,
            'Phone': phone,
            'Email': email
        }

        data = open('records.txt', 'a+')
        data.write(str(user))
        data.close()

        return ('Contact Added')

    def getRecords(self, filename):
        """
        Load every line of a text file as a list. If file not found will return such error

        :param filename: Name of file where text should be searched
        :return: List of loaded elements
        """
        try:
            with open(filename, 'r') as textfile:
                values = [line.strip() for line in textfile]
                return values
        except:
            return ('File Not Found')


    def searchRecord(self, text, file):
        """
        Search for text in a given record file and return all information information found.
        An empty list is return if nothing is found
        :param text: Element to be searched in file
        :param file: Name of file where text should be searched
        :return: List of found elements
        """
        records = self.getRecords(file)

        return [index for index in records if text in index]


