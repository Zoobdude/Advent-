
overAlocatedCount = 0# Count of over allocated resources

inputFile = open("input.txt", "r")# Open input file
cleanupAllocations = inputFile.readlines()# Read input file
inputFile.close()# Close input file

for i in range(len(cleanupAllocations)):# loops through each line in the input file
    currentLine = cleanupAllocations[i]# stores the current line in a variable
    groups = currentLine.split(",")# splits the two groups of people into a list
    group1 = groups[0]# stores the first group of people in a variable
    group2 = groups[1]# stores the second group of people in a variable
    group1 = group1.split("-")# splits the first group of people into a list reafy for conversion to a range
    group2 = group2.split("-")# splits the second group of people into a list reafy for conversion to a range

    group1Range = list(range(int(group1[0]), int(group1[1])+1))# converts the first group of people into a range
    group2Range = list(range(int(group2[0]), int(group2[1])+1))# converts the second group of people into a range

    test1 = all(x in group2Range for x in group1Range)# checks if all of the rooms the first group will be cleaning are already allocated to the second group
    test2 = all(x in group1Range for x in group2Range)# checks if all of the rooms the second group will be cleaning are already allocated to the first group

    if test1 == True or test2 == True:# if either test is true then the groups are over allocated
        overAlocatedCount += 1# adds one to the count of over allocated groups

print(overAlocatedCount)