import glob
import datetime
import time

fileList = glob.glob("*.txt")
fileTime = datetime.datetime.now()
newFile = fileTime.strftime("%Y-%m-%d-%H-%M-%S-%f")

with open(newFile+".txt","w") as newFileTemp:
    for file in fileList:
        openedFile = open(file,"r")
        newFileTemp.write(openedFile.read()+"\n")
        openedFile.close()
