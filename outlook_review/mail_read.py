import win32com.client
import win32com
import os
import sys
import traceback

f = open("testfile.txt", 'w+')

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
accounts = win32com.client.Dispatch("Outlook.Application").Session.Accounts

def emailleri_al(folder):
    messages = folder.items
    a = len(messages)
    if a>0:
        for message in messages:
            try:
                sender = message.SenderEmailAddress
                if sender != "":
                    print(sender, file = f)
            except Exception:
                print(inbox)
                traceback.print_exc()
                print("Error")
                print(account.DeliveryStore.Displayname)
                pass
            try:
                message.save
                message.Close(0)
            except:
                pass


for account in accounts:
    global inbox
    inbox = outlook.Folders(account.DeliveryStore.Displayname)
    print("***Account Name*************", file=f)
    print(account.DisplayName, file = f)
    print(account.DisplayName)
    print("****************************", file = f)
    folders = inbox.Folders

    for folder in folders:
        print("***Folder Name*************", file = f)
        print(folder,file = f)
        print("***************************", file = f)
        emailleri_al(folder)
        a = len(folder.folders)

'''        if a>0:
            global z
            z = outlook.Folders(account.DeliveryStore.Displayname).Folders(Folder.name)
            x = z.Folders
'''


