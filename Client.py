#2018-2019 Programação 2 (LTI)
#Grupo 40
#52052 Guilherme de Almeida
#51623 Rui Pereira


class Client(object):
    """
    A Client.
    """

    def __init__(self, name, city, dateRequested, timeRequested, \
                 maxPayment, minStarsNeeded, skillNeeded, taskDuration):
        """
        Creates a Client object.
        :param name: The name of the Client.
        :param city: The city of the Client.
        :param dateRequested: The date when the Client made its request.
        :param timeRequested: The time when the Client made its request.
        :param maxPayment: The maximum amount that the Client is willing to pay, per hour.
        :param minStarsNeeded: The minimum amount of star rating that the Client is willing to accept.
        :param skillNeeded: The skill that the Client needs.
        :param taskDuration: The duration of the task requested by the Client.
        """
        self.name = name
        self.city = city
        self.dateRequested = dateRequested
        self.timeRequested = timeRequested
        self.maxPayment = maxPayment
        self.minStarsNeeded = minStarsNeeded
        self.skillNeeded = skillNeeded
        self.taskDuration = taskDuration

    def getName(self):
        """
        The Client's name.
        """
        return self.name

    def getCity(self):
        """
        The Client's city.
        """
        return self.city

    def getDateRequested(self):
        """
        The date that the Client made its request.
        """
        return self.dateRequested

    def getTimeRequested(self):
        """
        The time that the Client made its request.
        """
        return self.timeRequested

    def getMaxPayment(self):
        """
        The maximum amount that the Client is willing to pay, per hour.
        """
        return self.maxPayment

    def getMinStarsNeeded(self):
        """
        The minimum amount of star rating that the Client is willing to accept.
        """
        return self.minStarsNeeded

    def getSkillNeeded(self):
        """
        The Skill that the Client needs.
        """
        return self.skillNeeded

    def getTaskDuration(self):
        """
        The duration of the task requested by the Client.
        """
        return self.taskDuration

    def getYear(self):
        """
        The year when the Client made its request.
        """
        return self.getDateRequested().split("-")[0]

    def getMonth(self):
        """
        The month when the Client made its request.
        """
        return self.getDateRequested().split("-")[1]

    def getDay(self):
        """
        The day when the Client made its request.
        """
        return self.getDateRequested().split("-")[2]

    def getHour(self):
        """
        The hour when the Client made its request.
        """
        return self.getTimeRequested().split(":")[0]

    def getMinutes(self):
        """
        The minute when the Client made its request.
        """
        return self.getTimeRequested().split(":")[1]

    def getDateTime(self):
        """
        The result of aggregating year, month, day, hour, minutes in a str representation.
        """
        return self.getYear() + self.getMonth() + self.getDay() + self.getHour() + self.getMinutes()

    def getIncTimeHour(self, incTime):
        """
        The single value of the hour without the "h" char.
        :param incTime: The hour to be split of the "h" char.
        """
        return incTime.split("h")[0]

    def getIncTimeMinutes(self, incTime):
        """
        The single value of the minutes without the "h" char.
        :param incTime: The minutes to be split of the "h" char.
        """
        return incTime.split("h")[1]

    def assembleDate(self, year, month, day):
        """
        Assembles the date according to the format given
        in the contract.
        Requires: year, month and day should be of str type.
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
        Requires: hour and minutes should be of str type.
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

    def taskAssembleTime(self, hour, minutes):
        """
        Assembles the time according to the format given
        in the contract referring to a task duration.
        Requires: hour and minutes should be of str type.
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

        time = hour + "h" + minutes

        return time

    def composeTime(self, firstTime, secondTime):
        """
        Update time when to firstTime you increment secondTime.
        Ensures: The time updated of str type.
        :param firstTime: The first time to be utilized for the update.
        :param secondTime: The second time to be utilized for the update.
        :return: The time updated of str type.
        """
        firstTimeHour = int(self.getIncTimeHour(firstTime))
        firstTimeMinutes = int(self.getIncTimeMinutes(firstTime))
        secondTimeHour = int(self.getIncTimeHour(secondTime))
        secondTimeMinutes = int(self.getIncTimeMinutes(secondTime))

        hoursComposed = firstTimeHour + secondTimeHour
        minutesComposed = firstTimeMinutes + secondTimeMinutes

        if minutesComposed >= 60:
            hoursComposed = hoursComposed + (minutesComposed // 60)
            minutesComposed = minutesComposed % 60

        newTime = self.taskAssembleTime(hoursComposed, minutesComposed)

        return newTime

    def getNewTime(self, incTime):
        """
        Update date and time when to it you increment incTime.
        Ensures: The date and time updated of str type.

        >>> newTime("2019-12-30", "19:30", "0h40")
        ('2020-01-01', '08:10')
        >>> newTime("2018-08-03", "16:00", "6h30")
        ( '2018-08-04', '10:30')

        :param incTime: The time to be incremented to the current time.
        :return: Two elements of str type; the first one with the updated date
        and the second one with the updated time.
        """
        year = int(self.getYear())
        month = int(self.getMonth())
        day = int(self.getDay())
        hour = int(self.getHour())
        minutes = int(self.getMinutes())
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

    def __str__(self):
        """
        Prints the Client object.
        """
        return "(" + self.getName() + ", " + self.getCity() + ", " \
               + self.getDateRequested() + ", " + self.getTimeRequested() + ", " \
               + self.getMaxPayment() + ", " + self.getMinStarsNeeded() + ", " \
               + self.getSkillNeeded() + ", " + self.getTaskDuration() + ")"


#Python Console examples for debugging.
#
#client1 = Client("Guillaume Dutroux", "london", "2019-03-12", "13:30", "55", "4*", "plumbing", "4h00")