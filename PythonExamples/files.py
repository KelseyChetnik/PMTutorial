#!/usr/bin/python

fName = "MontePython.txt"

myFile = open(fName, "r")

fString = myFile.read()

print(fString)

#fLines = []
#for line in myFile:
#    line = line.strip('\n')
#    fLines.append(line)

#print(len(fLines))

#for l in fLines:
#    print(l)

myFile.close()

outFile = "Seuss.txt"

with open(outFile, "w") as out:
    out.write("One fish\n")
    out.write("Two fish\n")

with open(outFile, "w") as out:
    out.write("Red fish\n")
    out.write("Blue fish\n")
