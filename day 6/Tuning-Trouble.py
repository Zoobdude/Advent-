inputFile = open("input1.txt", "r")
datastream = inputFile.read()# Read the file

dataProcessing = ["s","b","p","b"]# Initialize the dataProcessing list with the first 4 elements of the datastream
j = 4# Initialize the counter including the first 4 elements of the datastream

for i in range(len(datastream)):# Loop through the datastream
    dataProcessing.append(datastream[i])# Add the next element to the end of the dataProcessing list from the datastream
    dataProcessing.pop(0)# Remove the first element from the dataProcessing list
    multipleOccurences = False #reset the multipleOccurences flag
    print(dataProcessing)#chuck the current 4 characters being worked on
    if len(dataProcessing) == len(set(dataProcessing)):
        print("No duplicates")
        print(" ")
        print(j + 1) #output the ammount of characters processed
        break# Break out of the loop so the rest of the datastream is not processed
    else:
        print("Duplicates found")
        j += 1# Increment the counter
    