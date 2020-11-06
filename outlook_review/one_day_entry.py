import win32com.client, datetime


def getCalendarEntries(days=1):

    Outlook = win32com.client.Dispatch("Outlook.Application")
    ns = Outlook.GetNamespace("MAPI")
    appointments = ns.GetDefaultFolder(9).Items
    appointments.Sort("[Start]")
    appointments.IncludeRecurrences = "True"
    today = datetime.datetime.today()
    begin = today.date().strftime("%m/%d/%Y")
    tomorrow = datetime.timedelta(days=days) + today
    end = tomorrow.date().strftime("%m/%d/%Y")
    appointments = appointments.Restrict("[Start] >= '" + begin + "' AND [END] <= '" + end + "'")
    events = {'Start': [], 'Subject': [], 'Duration': []}
    for a in appointments:
        adate = datetime.datetime.fromtimestamp(int(a.Start))
        print(a.Start, a.Subject,a.Duration)
        events['Start'].append(adate)
        events['Subject'].append(a.Subject)
        events['Duration'].append(a.Duration)
    return events

