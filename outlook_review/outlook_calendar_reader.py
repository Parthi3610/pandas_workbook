import win32com.client, datetime
from dateutil.parser import *
from dateutil.relativedelta import relativedelta

import re
import csv
import calendar

def main():
    print("Accessing outlook calendar, please wait....")
    outlook = win32com.client.Dispatch("Outlook.Application")
    ns = outlook.Namespace("MAPI")
    appointments = ns.GetDefultFolder(9).Items
    appointments.Sort["Start"]
    appointments.IncludeRecurrences = "True"

    begin = InputDate("start")
    end = InputDate("end")

    appointments = appointments.Restrict["[Start] >='"+begin+"' AND [END] <= '"+end+"'"]
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


