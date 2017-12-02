numbers = [1, 2, 3]
writeFile = open("nuumbers.txt","w")
for number in numbers:
    writeFile.write(str(number)+"\n")
writeFile.close()
