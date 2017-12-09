import time
from datetime import datetime as dt

#hostPath = "/etc/hosts"
hostPath = "hosts"
redirectPath = "127.0.0.1"
blockingWebSiteLinks = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours...")
        with open(hostPath,"r+") as file:
            contentFile = file.read()
            for website in blockingWebSiteLinks:
                if website in contentFile:
                    pass
                else:
                    file.write(redirectPath + "\t" + website + "\n")
    else:
        print("Free Hours")
        with open(hostPath,"r+") as file:
            contentLines = file.readlines()
            file.seek(0)
            for line in contentLines:
                if not any(website in line for website in blockingWebSiteLinks):
                    file.write(line)
            file.truncate()
    time.sleep(5)
