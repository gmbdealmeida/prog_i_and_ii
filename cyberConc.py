#2018-2019 Programação 2 (LTI)
#Grupo 40
#52052 Guilherme de Almeida
#51623 Rui Pereira

import sys
from Header import Header
from ExpertCollection import ExpertCollection
from ClientCollection import ClientCollection
from scheduling import scheduling


def update(fileNameExperts, fileNameClients):
    """
    Assign given experts to given clients and Update the experts with
    their new availability.
    Requires: fileNameExperts, fileNameClients are str, with the names
    of the files representing the list of experts and clients, respectively,
    following the format indicated in the project.
    Ensures: Two output files, respectively, with the listing of schedules
    tasks and the updated listing of experts, following the format
    and naming convention indicated in the project.
    """

    #Creates an ExpertCollection object and assigns it to a list.
    expertCollection0 = ExpertCollection(fileNameExperts)
    expertsList = expertCollection0.readExperts()
    #Creates a ClientCollection object and assigns it to a list.
    clientsCollection0 = ClientCollection(fileNameClients)
    clientsList = clientsCollection0.readClients()
    #Creates an Header object using the experts file.
    header = Header(fileNameExperts)
    header.readHeader()
    updatedScheduleHeader = header.updateScheduleHeader()
    updatedExpertsHeader = header.updateExpertsHeader()
    updatedScheduleFileName = header.updateScheduleFileName()
    updatedExpertsFileName = header.updateExpertsFileName()
    #Creates a Schedule object to make the assignment and
    #to create the two output files.
    schedule0 = scheduling(expertsList, clientsList, header)
    schedule0.update()
    schedule0.writeSchedule(updatedScheduleFileName, updatedScheduleHeader)
    schedule0.writeExperts(updatedExpertsFileName, updatedExpertsHeader)

    try:
        dateTimeFileName = fileNameExperts[:4] + fileNameExperts[5:7] + fileNameExperts[8:10] \
         + fileNameExperts[17:19] + fileNameExperts[20:22]
        typeFileName = fileNameExperts[10:17]
        tryExpertsHeader = Header(fileNameExperts)
        tryExpertsHeader.readHeader()
        dateTimeExpertsHeader = tryExpertsHeader.getHeaderDateTime()
        typeExpertsHeader = tryExpertsHeader.getHeaderType().replace("E", "e")

        assert dateTimeFileName == dateTimeExpertsHeader and typeFileName == typeExpertsHeader
    except AssertionError:
        raise IOError("Error in input file: inconsistent name and header in file " + fileNameExperts)

    try:
        dateTimeFileName = fileNameClients[:4] + fileNameClients[5:7] + fileNameClients[8:10] \
         + fileNameClients[17:19] + fileNameClients[20:22]
        typeFileName = fileNameClients[10:17]
        tryClientsHeader = Header(fileNameClients)
        tryClientsHeader.readHeader()
        dateTimeClientsHeader = tryClientsHeader.getHeaderDateTime()
        typeClientsHeader = tryClientsHeader.getHeaderType().replace("C", "c")

        assert dateTimeFileName == dateTimeClientsHeader and typeFileName == typeClientsHeader
    except AssertionError:
        raise IOError("Error in input file: inconsistent name and header in file " + fileNameClients)

    try:
        expertHeader = Header(fileNameExperts)
        expertHeader.readHeader()
        expertFirstSixLines = expertHeader.getFirstSixLines()
        clientHeader = Header(fileNameClients)
        clientHeader.readHeader()
        clientFirstSixLines = clientHeader.getFirstSixLines()

        assert expertFirstSixLines == clientFirstSixLines
    except AssertionError:
        raise IOError("Error in input file: inconsistent files " + fileNameExperts + " and " + fileNameClients)


inputFileName1, inputFileName2 = sys.argv[1:]

update(inputFileName1, inputFileName2)


#Python Console examples for debugging.
#
#update("2019y01m12experts09h00.txt", "201 9y01m12clients09h00.txt")
#update("2019y02m15experts10h30.txt", "2019y02m15clients10h30.txt")
#update("2019y03m20experts12h30.txt", "2019y03m20clients12h30.txt")