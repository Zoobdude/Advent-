calibration_nums = 0 #initialise the running total

#some of the numbers are writtern as words, so we need to translate them. 
#Some of the words share first or last letters so we add them to each end of the translations just incase
translate = { 
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

with open('2023/day1/input.txt') as f:
    for line in f:
        numbers_in_line = [] #initilise the var that will store all numbers in the line

        for key in translate: #itterate over each number that needs to be translated
            if key in line:
                line = line.replace(key, translate[key]) #replace the word with the translation

        for char in line: #iterate over every character in the line
            try:
                numbers_in_line.append(int(char)) #if the number can be converted to an int, add it to the list
            except ValueError:
                pass


        this_line_calibration = int(f"{numbers_in_line[0]}{numbers_in_line[-1]}")

        calibration_nums += this_line_calibration #add the number to the running total
 
#output the result       
print(calibration_nums)
