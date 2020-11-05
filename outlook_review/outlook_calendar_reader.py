import win32com.client, datetime
from dateutil.parser import *
from dateutil.relativedelta import relativedelta

import re
import csv
import calendar

def main():
    print("Accessing outlook calendar, please wait....")
    outlook = win32com.client.Dispatch("Outlook.Application")
    ns = outlook.GetNamespace("MAPI")
    appointments = ns.GetDefaultFolder(9).Items
    appointments.Sort("[Start]")
    appointments.IncludeRecurrences = "True"

    begin = InputDate("start")
    end = InputDate("end")

    appointments = appointments.Restrict("[Start] >= '"+begin+"' AND [END] <= '"+end+"'")
    appointmentDictionary = {}

    timeregex = re.compile('\d\d/\d\d/\d\d')
    nameregex = re.compile(u'[Nn]ame: ?(?P<name>[\( \)\&;\w]*)', re.UNICODE)
    locationregex = re.compile(u'[Ll]ocation: ?(?P<location>[\( \)\&;\d]*)', re.UNICODE)

    for a in appointments:
        meetingDate = str(a.Start)
        subject = str(a.Subject)
        body = str(a.Body.encode("utf8"))
        duration = str(a.duration)
        date = parse(meetingDate).date()
        time = parse(meetingDate).time()
        participants = []

        for r in a.Recipients:
            participants += [str(r)]

        if subject in appointmentDictionary.keys():
            appointmentDictionary[subject]["Meetings"] += [date.strftime("%m%d%y")]
            appointmentDictionary[subject]["Times"] += [date.strftime("%I:%M %p")]
            appointmentDictionary[subject]["Durations"] += [duration]
            temp = appointmentDictionary[subject]["Participants"]+participants
            appointmentDictionary[subject]["Participants"] = list(set(temp))
        else:
            appointmentDictionary[subject]={"Subject":subject,"Body": body, "Meetings":[date.strftime("%m%d%y")],
                                            "Times": [time.strftime("%I:%M %p")], "Durations": [duration], "Participants": participants
                                            }


    resultsfile = open("resultsTally.csv",'wb')
    fields = ["Subject", "Body", "Number of Occurences", "Date (First)", "Time (First)", "Duration (First)", "Date (Second)", "Time (Second)", "Duration (Second)", "Date (Third)", "Time (Third)", "Duration (Third)", "Further Dates", "Further Times", "Further Durations", "Participants"]
    resultsWriter = csv.DictWriter(resultsfile,fields)
    resultsWriter.writeheader()

    for subject in appointmentDictionary.keys():
        rowDict = {}
        rowDict["subject"] = appointmentDictionary[subject]["Subject"] if appointmentDictionary[subject]["Subject"] else ""
        rowDict["body"] = appointmentDictionary[subject]["Body"] if appointmentDictionary[subject]["Body"] else ""
        rowDict["participants"] = ", ".join(appointmentDictionary[subject]["Participants"]) if appointmentDictionary[subject]["Participants"] else ""
        MeetingWriter(rowDict,appointmentDictionary[subject]["Meetings"], appointmentDictionary[subject]["Times"], appointmentDictionary[subject]["Durations"])
        rowDict["Number of Occurences"] = len(appointmentDictionary[subject]["Meetings"])

        resultsWriter.writerow(rowDict)

def MeetingWriter(rowDict, meetings, times, durations):
    datecount = 0
    for i in range(0,len(meetings)):
        if datecount == 0:
            rowDict["Date(First)"] = meetings[i]
            rowDict["Time(First)"] = times[i]
            rowDict["Duration(First)"] = durations[i]

        elif datecount == 1:
            rowDict["Date(Second)"] = meetings[i]
            rowDict["Time(Second)"] = times[i]
            rowDict["Duration(Second)"] = durations[i]

        elif datecount == 2:
            rowDict["Date(Third)"] = meetings[i]
            rowDict["Time(Third)"] = times[i]
            rowDict["Duration(Third)"] = durations[i]

        else:
            if "Further Dates" in rowDict.keys():
                rowDict["Further Dates"] += "," + meetings[i]
                rowDict["Further Dates"] += "," + times[i]
                rowDict["Further Dates"] += "," + durations[i]
            else:
                rowDict["Further Dates"] = meetings[i]
                rowDict["Further Dates"] = times[i]
                rowDict["Further Dates"] = durations[i]

            datecount +=1
        return rowDict

def InputDate(startOrEnd):
    ifValid = False
    while not ifValid:
        inp = input("Please enter the date " + startOrEnd + " the tally (mm/dd/yyyy):")
        try:
            parsedInput = parse(inp).date()
            ifValid = True
        except:
            print("The date you entered could not be processed")
        return parsedInput.strftime("%m/%d/%Y")

if __name__ == "__main__":
    main()


