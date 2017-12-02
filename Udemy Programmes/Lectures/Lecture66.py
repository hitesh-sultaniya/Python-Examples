temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        print("That temperature doesn't make sense!")
    else:
        f=c*9/5+32
        writeFile.write(str(f)+"\n")


with open("temperature.txt","w") as writeFile:
    for t in temperatures:
        c_to_f(t)
