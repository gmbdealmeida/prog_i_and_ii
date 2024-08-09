#2018-2019 Programação 2 (LTI)
#Grupo 40
#52052 Guilherme de Almeida
#51623 Rui Pereira

from collections import UserList
from Expert import Expert
from Client import Client
from Header import Header
from ExpertCollection import ExpertCollection
from ClientCollection import ClientCollection
import constants


class scheduling(UserList):
    """
    A Schedule.
    """

    def __init__(self, expertsList, clientsList, header):
        """
        Creates a Schedule object.
        :param expertsList: The experts list.
        :param clientsList: The clients list.
        :param header: The header to be utilized in the writing of the new files.
        """
        super().__init__()
        self.expertsList = expertsList
        self.clientsList = clientsList
        self.header = header
        self.expertChosen = []
        self.matchList = []
        self.expertUpdated = []

    def update(self):
        """
        Makes the assignment between experts and clients and updates
        the experts with their new availability.
        Requires:w
        - A Collection of Experts, that should be a list with the same format
        as the one given in the contract.
        - A Collection of Clients, that should be a list with the same format
         as the one given in the contract.
        - An Header, that should be a list with the same format as the one given
        in the contract.
        Ensures: Two new lists; one with the matches between experts and clients
        and another with the updated experts availability.
        :return: A list with the matches between experts and clients.
        """
        #Iterates over every client contained in clientsList
        for client in self.clientsList:
            self.expertChosen = []
            self.matchList = []
            matchFound = False

            #Iterates over every expert contained in expertsList
            for expert in self.expertsList:
                if not matchFound:
                    #Checks the conditions needed for the expert to be a match for the given client.
                    if client.getCity() == expert.getCity() and client.getSkillNeeded() in expert.getSkills() \
                       and client.getMinStarsNeeded() <= expert.getStars() \
                       and int(client.getMaxPayment()) >= int(expert.getPayment()):
                        matchFound = True
                        #Appends an expert that is a match for the given client to a new list.
                        self.expertChosen.append(Expert(expert.getName(), expert.getCity(), expert.getSkills(), \
                                                        expert.getStars(), expert.getPayment(), \
                                                        expert.getDateAvailable(), expert.getTimeAvailable(), \
                                                        expert.getMoneySum()))
                #Checks if there is a more suitable expert for the given client.
                else:
                    if client.getCity() == expert.getCity() and client.getSkillNeeded() in expert.getSkills() \
                       and client.getMinStarsNeeded() <= expert.getStars() \
                       and int(client.getMaxPayment()) >= int(expert.getPayment()):
                        if expert < self.expertChosen[0]:
                            self.expertChosen = []
                            self.expertChosen.append(Expert(expert.getName(), expert.getCity(), expert.getSkills(), \
                                                            expert.getStars(), expert.getPayment(), \
                                                            expert.getDateAvailable(), expert.getTimeAvailable(), \
                                                            expert.getMoneySum()))

            #Makes the matching between expert and client and appends it to a list.
            if matchFound:
                if client.getDateTime() > self.expertChosen[0].getDateTime():
                    self.matchList.append(client.getDateRequested())
                    self.matchList.append(client.getTimeRequested())
                else:
                    #Checks if the time needed for the expert to get to the client (1h00)
                    #surpasses the working hours of a day (20:00)
                    if (int(self.expertChosen[0].getTime()) + 100) > 2000:
                        newDate = self.expertChosen[0].getNewTime(constants.minutesAddedExpert)
                        self.expertChosen[0].setDateAvailable(newDate[0])
                        self.expertChosen[0].setTimeAvailable("08:00")
                    if self.expertChosen[0].getTimeAvailable() != "08:00":
                        newDate = self.expertChosen[0].getNewTime(constants.minutesAddedExpert)
                    else:
                        newDate = self.expertChosen[0].getNewTime(constants.noMinutesAdded)
                    self.matchList.append(newDate[0])
                    self.matchList.append(newDate[1])
                self.matchList.append(client.getName())
                self.matchList.append(self.expertChosen[0].getName())
                self.append(self.matchList)

                #Updates the experts with their new availability and sum of money.
                for expert in self.expertsList:
                    if self.expertChosen[0].getName() == expert.getName():
                        if client.getDateTime() > self.expertChosen[0].getDateTime():
                            newDateTime = client.getNewTime(client.getTaskDuration())
                            self.expertChosen[0].setDateAvailable(newDateTime[0])
                            self.expertChosen[0].setTimeAvailable(newDateTime[1])
                            expert.setDateAvailable(self.expertChosen[0].getDateAvailable())
                            expert.setTimeAvailable(self.expertChosen[0].getTimeAvailable())
                        else:
                            if self.expertChosen[0].getTimeAvailable() != "08:00":
                                newDateTime = self.expertChosen[0].getNewTime(
                                    expert.composeTime(constants.minutesAddedExpert, client.getTaskDuration()))
                            else:
                                newDateTime = self.expertChosen[0].getNewTime(client.getTaskDuration())
                            expert.setDateAvailable(newDateTime[0])
                            expert.setTimeAvailable(newDateTime[1])
                        expert.setMoneySum(client.getTaskDuration())

            #Assigns "declined" if no match for the given client is found.
            else:
                refreshedHeader = []
                newDate = self.header.getNewTime(constants.minutesRefresh)
                refreshedHeader.append(newDate[0])
                refreshedHeader.append(newDate[1])

                self.matchList.append(refreshedHeader[0])
                self.matchList.append(refreshedHeader[1])
                self.matchList.append(client.getName())
                self.matchList.append("declined")
                self.append(self.matchList)

        #Sorts the assignment and updated experts according to given conditions.
        self.expertsList.sort()
        self.sort()

        return self

    def writeSchedule(self, newFileName, updatedScheduleHeader):
        """
        Writes an .txt file with given assignment.
        Requires: The new file name should be of str type.
        Furthermore the updated header should have the same format
        as the one given in the contract.
        Ensures: A new file with the schedule written on the same format
        as the one given in the contract.
        :param newFileName: The name to be given to the new file.
        :param updatedScheduleHeader: An header with updated date, time and type of file.
        """
        newFile = open(newFileName, "w")

        #Writes the header to the new file.
        for line in range(constants.headerLines):
            newFile.write(updatedScheduleHeader[line] + "\n")

        i = 0

        #Writes the matches to the new file.
        for match in self:
            line = ""

            for elem in match:
                line = line + elem + ", "

            auxLine = line.rstrip(", ")

            #Checks whether there are more elements to add to a new line.
            #If there aren't, doesn't write the newline character ("\n")
            if i != (len(self) - 1):
                newFile.write(auxLine + "\n")
            else:
                newFile.write(auxLine)

            i = i + 1

        newFile.close()

    def writeExperts(self, newFileName, updatedExpertsHeader):
        """
        Writes an .txt file with given updated experts.
        Requires: The new file name should be of str type.
        Furthermore the updated header should have the same format
        as the one given in the contract.
        Ensures: A new file with the experts updated written on the
        same format as the one given in the contract.
        :param newFileName: The name to be given to the new file.
        :param updatedExpertsHeader: An header with updated date, time and type of file.
        """
        newFile = open(newFileName, "w")

        #Writes the header to the new file.
        for line in range(constants.headerLines):
            newFile.write(updatedExpertsHeader[line] + "\n")

        i = 0

        #Writes the updated experts to the new file.
        for expert in self.expertsList:
            expertWrite = [expert.getName(), expert.getCity(), expert.getSkills(), expert.getStars(),
                           expert.getPayment(), expert.getDateAvailable(), expert.getTimeAvailable(),
                           expert.getMoneySum()]

            expertStr = str(expertWrite)
            expertStr = expertStr.strip("[").strip("]").replace("'", "")

            #Checks whether there are more elements to add to a new line.
            #If there aren't, doesn't write the newline character ("\n")
            if i != (len(self.expertsList) - 1):
                newFile.write(expertStr + "\n")
            else:
                newFile.write(expertStr)

            i = i + 1

        newFile.close()

    def __str__(self):
        """
        Prints the Schedule object.
        """
        lst = ""

        for elem in self:
            lst = lst + str(elem)

        return lst