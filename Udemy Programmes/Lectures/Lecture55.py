fileContent = open('fruits.txt','r')
fileLines = fileContent.readlines()
fileContent.close()
fileLines = [item.rstrip("\n") for item in fileLines]
for item in fileLines:
    print(len(item))
