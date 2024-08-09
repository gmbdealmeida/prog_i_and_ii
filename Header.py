#2018-2019 Programação 2 (LTI)
#Grupo 40
#52052 Guilherme de Almeida
#51623 Rui Pereira

import constants


class Header(object):
    """
    A Header.
    """

    def __init__(self, fileName):
        """
        Creates an Header object.
        :param fileName: The name of the file where the header is contained.
        """
        self.fileName = fileName
        self.headerList = []

    def readHeader(self):
        """
        Reads the header elements and adds them to a list.
        Requires: The format of the file read should be of the same type
        as the one given in the contract.
        Ensures: A list with the header elements as shown on
        the input file.
        :return: A list with the header elements.
        """
        file = open(self.fileName, "r")
        line = file.readline()

        #Reads each header element and adds it to a list.
        for i in range(constants.headerLines):
            self.headerList.append(line.rstrip("\n"))
            line = file.readline()

        file.close()

        return self.headerList

    def getHeader(self):
        """
        The list of Header's elements.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[:]

    def getFileName(self):
        """
        The name of the file where the Header was read from.
        Requires: self.readHeader() should already have been executed.
        """
        return self.fileName

    def getHeaderDate(self):
        """
        The date element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[1]

    def getHeaderTime(self):
        """
        The time element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[3]

    def getHeaderType(self):
        """
        The type element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[6].strip(":")

    def getHeaderYear(self):
        """
        The year of the date element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[1].split("-")[0]

    def getHeaderMonth(self):
        """
        The month of the date element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[1].split("-")[1]

    def getHeaderDay(self):
        """
        The day of the date element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[1].split("-")[2]

    def getHeaderHour(self):
        """
        The hour of the time element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[3].split(":")[0]

    def getHeaderMinutes(self):
        """
        The minutes of the time element of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[3].split(":")[1]

    def getHeaderDateTime(self):
        """
        The result of aggregating year, month, day, hour, minutes of
        the date and time elements in a str representation.
        Requires: self.readHeader() should already have been executed.
        """
        return self.getHeaderYear() + self.getHeaderMonth() + self.getHeaderDay() \
         + self.getHeaderHour() + self.getHeaderMinutes()

    def getFirstSixLines(self):
        """
        The first six lines/elements of the Header.
        Requires: self.readHeader() should already have been executed.
        """
        return self.headerList[0] + self.headerList[1] + self.headerList[2] + self.headerList[3] \
         + self.headerList[4] + self.headerList[5]

    def getIncTimeHour(self, incTime):
        """
        The single value of the hour without the "h" char.
        Requires: self.readHeader() should already have been executed.
        :param incTime: The hour to be split of the "h" char.
        """
        return incTime.split("h")[0]

    def getIncTimeMinutes(self, incTime):
        """
        The single value of the minutes without the "h" char.
        Requires: self.readHeader() should already have been executed.
        :param incTime: The minutes to be split of the "h" char.
        """
        return incTime.split("h")[1]

    def assembleDate(self, year, month, day):
        """
        Assembles the date according to the format given
        in the contract.
        Requires: self.readHeader() should already have been executed.
                  year, month and day should be of str type.
        Ensures: Returns year, month and day according to the format
        given in the contract.
        :param year: The year to be assembled.
        :param month: The month to be assembled.
        :param day: The day to be assembled.
        :return: A string with the assembled date.
        """
        year = str(year)
        month = str(month)
        day = str(day)

        if int(month) < 10:
            month = "0" + month

        if int(day) < 10:
            day = "0" + day

        date = year + "-" + month + "-" + day

        return date

    def assembleTime(self, hour, minutes):
        """
        Assembles the time according to the format given
        in the contract.
        Requires: self.readHeader() should already have been executed.
                  hour and minutes should be of str type.
        Ensures: Returns hour and minutes according to the format
        given in the contract.
        :param hour: The hour to be assembled.
        :param minutes: The minutes to be assembled.
        :return: A string with the assembled time.
        """
        hour = str(hour)
        minutes = str(minutes)

        if int(hour) < 10:
            hour = "0" + hour

        if int(minutes) < 10:
            minutes = "0" + minutes

        time = hour + ":" + minutes

        return time

    def getNewTime(self, incTime):
        """
        Assembles the time according to the format given
        in the contract referring to a task duration.
        Requires: self.readHeader() should already have been executed.
                  hour and minutes should be of str type.
        Ensures: Returns hour and minutes according to the format
        given in the contract.
        :param hour: The hour to be assembled.
        :param minutes: The minutes to be assembled.
        :return: A string with the assembled time.
        """
        year = int(self.getHeaderYear())
        month = int(self.getHeaderMonth())
        day = int(self.getHeaderDay())
        hour = int(self.getHeaderHour())
        minutes = int(self.getHeaderMinutes())
        incHour = int(self.getIncTimeHour(incTime))
        incMinutes = int(self.getIncTimeMinutes(incTime))

        hour = hour + incHour
        minutes = minutes + incMinutes

        if minutes >= 60:
            hour = hour + (minutes // 60)
            minutes = minutes % 60

            if hour >= 20:
                hour = (hour % 20) + 8
                day = day + 1

                if day > 30:
                    day = day % 30
                    month = month + 1

                    if month > 12:
                        month = month % 12
                        year = year + 1

        elif hour >= 20:
            hour = (hour % 20) + 8
            day = day + 1

            if day > 30:
                day = day % 30
                month = month + 1

                if month > 12:
                    month = month % 12
                    year = year + 1

        newDate = self.assembleDate(year, month, day)
        newTime = self.assembleTime(hour, minutes)

        return newDate, newTime

    def updateExpertsHeader(self):
        """
        Update the header to be utilized on writing the updated Experts file
        according to the format given on the contract.
        Requires: self.readHeader() should already have been executed.
        :return: The updated header to be utilized on the updated Experts file.
        """
        header = self.getHeader()
        newDate = self.getNewTime(constants.minutesRefresh)
        header[1] = newDate[0]
        header[3] = newDate[1]

        return header

    def updateScheduleHeader(self):
        """
        Update the header to be utilized on writing the assignment file
        according to the format given on the contract.
        Requires: self.readHeader() should already have been executed.
        :return: The updated header to be utilized on the assignment file.
        """
        header = self.getHeader()
        newDate = self.getNewTime(constants.minutesRefresh)
        header[1] = newDate[0]
        header[3] = newDate[1]
        header[6] = "Schedule:"

        return header

    def updateExpertsFileName(self):
        """
        Update the name of the file to be utilized on writing the update Experts file
        according to the format given on the contract.
        :return: The updated name of the file to be utilized on the updated Experts file.
        """
        newDate = self.getNewTime(constants.minutesRefresh)
        updatedFileName = newDate[0].split("-")[0] + "y" + newDate[0].split("-")[1] + "m" + newDate[0].split("-")[2] \
                          + "experts" + newDate[1].split(":")[0] + "h" + newDate[1].split(":")[1] + ".txt"

        return updatedFileName

    def updateScheduleFileName(self):
        """
        Update the name of the file to be utilized on writing the assignment file
        according to the format given on the contract.
        :return: The updated name of the file to be utilized on the assignment file.
        """
        newDate = self.getNewTime(constants.minutesRefresh)
        updatedFileName = newDate[0].split("-")[0] + "y" + newDate[0].split("-")[1] + "m" + newDate[0].split("-")[2] \
                          + "schedule" + newDate[1].split(":")[0] + "h" + newDate[1].split(":")[1] + ".txt"

        return updatedFileName
