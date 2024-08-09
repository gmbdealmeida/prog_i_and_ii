#2018-2019 Programação 2 (LTI)
#Grupo 40
#52052 Guilherme de Almeida
#51623 Rui Pereira

from collections import UserList
from Client import Client
import constants


class ClientCollection(UserList):
    """
    A clientCollection.
    """

    def __init__(self, fileName):
        """
        Creates a clientCollection object.
        :param fileName: The name of the file where the collection of clients is contained.
        """
        super().__init__()
        self.fileName = fileName

    def readClients(self):
        """
        Reads the collection of clients and adds it to a list.
        Requires: The format of the file read should be of the same type
        as the one given in the contract.
        Ensures: A list with the experts available as shown on
        the input file.
        :return: A list with the clients available and its corresponding characteristics.
        """
        file = open(self.fileName, "r")
        line = file.readline()

        #Passes over the file's header.
        for i in range(constants.headerLines):
            line = file.readline()

        #Reads each client and adds him to a list.
        while line != "":
            strippedLine = line.rstrip("\n")
            name, city, dateRequested, timeRequested, maxPayment, minStarsNeeded, \
            skillNeeded, taskDuration = strippedLine.split(", ")
            self.append(Client(name, city, dateRequested, timeRequested, maxPayment, minStarsNeeded, \
                               skillNeeded, taskDuration))
            line = file.readline()

        file.close()

        return self

    def __str__(self):
        """
        Prints the clientCollection object.
        """
        lst = ""

        for elem in self:
            lst = lst + str(elem)

        return lst


#Python Console examples for debugging.
#
#clientCollection1 = clientCollection("2019y01m12clients09h00.txt")