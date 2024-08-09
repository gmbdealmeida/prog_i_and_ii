#2018-2019 Programação 2 (LTI)
#Grupo 40
#52052 Guilherme de Almeida
#51623 Rui Pereira

from collections import UserList
from Expert import Expert
import constants


class ExpertCollection(UserList):
    """
    An expertCollection.
    """

    def __init__(self, fileName):
        """
        Creates an expertCollection object.
        :param fileName: The name of the file where the collection of experts is contained.
        """
        super().__init__()
        self.fileName = fileName

    def readExperts(self):
        """
        Reads the collection of experts and adds it to a list.
        Requires: The format of the file read should be of the same type
        as the one given in the contract.
        Ensures: A list with the experts available as shown on
        the input file.
        :return: A list with the experts available and its corresponding characteristics.
        """
        file = open(self.fileName, "r")
        line = file.readline()

        #Passes over the file's header.
        for i in range(constants.headerLines):
            line = file.readline()

        #Reads each expert and adds him to a list.
        while line != "":
            strippedLine = line.rstrip("\n")
            name, city, skills, stars, payment, dateAvailable, timeAvailable, moneySum = strippedLine.split(", ")
            self.append(Expert(name, city, skills, stars, payment, dateAvailable, timeAvailable, moneySum))
            line = file.readline()

        file.close()

        return self

    def __str__(self):
        """
        Prints the expertCollection object.
        """
        lst = ""

        for elem in self:
            lst = lst + str(elem)

        return lst


#Python Console examples for debugging.
#
#expertCollection1 = expertCollection("2019y01m12experts09h00.txt")