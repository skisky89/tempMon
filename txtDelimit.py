# Fix old temperature data

import sys

#open/create files
filetoopen = raw_input("Filename: ")
source = open(filetoopen)

#New file name
newFile = "B" + filetoopen 

#OS dependant file structure
fileOut = open(newFile, 'a')

while True:
            #Read source
            partA = source.readline()
            partB = source.readline()
            partC = source.readline()
            partD = source.readline()
            #Time/Date
            fileOut.write(partA.rstrip('\n'))
            fileOut.write(",")          
            #Temp A,B,C
            fileOut.write(partB.rstrip('\n'))
            fileOut.write(",")
            fileOut.write(partC.rstrip('\n'))
            fileOut.write(",")
            fileOut.write(partD)
            #End of delimited row
            fileOut.flush()

            if "" == partA:
                print "Done"
                break

