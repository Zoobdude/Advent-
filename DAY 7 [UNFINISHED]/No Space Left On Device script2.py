import re

inputFile = open("output2.txt", "r")
directories = inputFile.read().split()
inputFile.close()

for i in range(0, len(directories)):
    currentdirectories[i]