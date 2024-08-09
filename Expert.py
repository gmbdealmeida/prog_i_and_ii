#2018-2019 Programação 2 (LTI)
#Grupo 40
#52052 Guilherme de Almeida
#51623 Rui Pereira


class Expert(object):
    """
    An Expert.
    """

    def __init__(self, name, city, skills, stars, payment, \
                 dateAvailable, timeAvailable, moneySum):
        """
        Creates an Expert object.
        :param name: The name of the Expert.
        :param city: The city of the Expert.
        :param skills: The skills that the Expert possesses.
        :param stars: The star rating ot the Expert.
        :param payment: The payment demanded by the Expert, per hour.
        :param dateAvailable: The nearest date when the Expert is available to take requests.
        :param timeAvailable: The nearest time when the Expert is available to take requests.
        :param moneySum: The sum of money accumulated by the Expert to this moment.
        """
        self.name = name
        self.city = city
        self.skills = skills
        self.stars = stars
        self.payment = payment
        self.dateAvailable = dateAvailable
        self.timeAvailable = timeAvailable
        self.moneySum = moneySum

    def getName(self):
        """
        The Expert's name.
        """
        return self.name

    def getCity(self):
        """
        The Expert's city.
        """
        return self.city

    def getSkills(self):
        """
        The Expert's skills.
        """
        return self.skills

    def getStars(self):
        """
        The Expert's star rating.
        """
        return self.stars

    def getPayment(self):
        """
        The Expert's demanded payment, per hour.
        """
        return self.payment

    def getDateAvailable(self):
        """
        The nearest date when the Expert is available.
        """
        return self.dateAvailable

    def getTimeAvailable(self):
        """
        The nearest time when the Expert is available.
        """
        return self.timeAvailable

    def getMoneySum(self):
        """
        The sum of money accumulated by the Expert.
        """
        return self.moneySum

    def getYear(self):
        """
        The year when the Expert is available.
        """
        return self.getDateAvailable().split("-")[0]

    def getMonth(self):
        """
        The month when the Expert is available.
        """
        return self.getDateAvailable().split("-")[1]

    def getDay(self):
        """
        The day when the Expert is available.
        """
        return self.getDateAvailable().split("-")[2]

    def getHour(self):
        """
        The hour when the Expert is available.
        """
        return self.getTimeAvailable().split(":")[0]

    def getMinutes(self):
        """
        The minute when the Expert is available.
        """
        return self.getTimeAvailable().split(":")[1]

    def getDateTime(self):
        """
        The result of aggregating year, month, day, hour, minutes in a str representation.
        """
        return self.getYear() + self.getMonth() + self.getDay() + self.getHour() + self.getMinutes()

    def getTime(self):
        """
        The result of aggregating hour and minutes a str representation.
        """
        return self.getHour() + self.getMinutes()

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

    def setDateAvailable(self, newDateAvailable):
        """
        Set the nearest date when the Expert is available.
        """
        self.dateAvailable = newDateAvailable

    def setTimeAvailable(self, newTimeAvailable):
        """
        Set the nearest time when the Expert is available.
        """
        self.timeAvailable = newTimeAvailable

    def setMoneySum(self, taskDuration):
        """
        Set the sum of money accumulated by the Expert.
        """
        taskHours = float(self.getIncTimeHour(taskDuration))
        taskMinutes = float(self.getIncTimeMinutes(taskDuration))

        if taskMinutes != 0:
            self.moneySum = float(self.moneySum) + (float(self.getPayment()) * taskHours \
                            + float(self.getPayment()) * (1 / (60 / taskMinutes)))
        else:
            self.moneySum = float(self.moneySum) + float(self.getPayment()) * taskHours

        self.moneySum = str(self.moneySum)

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

    def __lt__(self, other):
        """
        Defines the criteria through which an Expert element
        should be considered less than other.
        """
        if self.getDateTime() == other.getDateTime():
            if self.getPayment() == other.getPayment():
                if self.getMoneySum() == other.getMoneySum():
                    return self.getName() < other.getName()
                else:
                    return self.getMoneySum() < other.getMoneySum()
            else:
                return self.getPayment() < other.getPayment()
        else:
            return self.getDateTime() < other.getDateTime()

    def __str__(self):
        """
        Prints the Expert object.
        """
        return "(" + self.getName() + ", " + self.getCity() + ", " + self.getSkills() \
               + ", " + self.getStars() + ", " + self.getPayment() + ", " \
               + self.getDateAvailable() + ", " + self.getTimeAvailable() + ", " \
               + self.getMoneySum() + ")"


#Python Console examples for debugging.
#
#expert1 = Expert("Dan Tufis", "lisbon", "(heating; doors; windows)", "2*", "20", "2019-03-12", "09:15", "2879.0")