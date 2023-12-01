
#open file
file = open("food.txt", "r")
outputFile = open("output.txt", "a")#append mode
#read file
calories = file.read().splitlines()
caloriesWorking = 0

for i in range(len(calories)):
    if calories[i] == "":
        outputFile.write(str(caloriesWorking) + "\n")
        caloriesWorking = 0
    else:
        print(calories[i])
        caloriesWorking += int(calories[i])

#then coppied the contents of output.txt and sorted using https://onlinenumbertools.com/sort-numbers 