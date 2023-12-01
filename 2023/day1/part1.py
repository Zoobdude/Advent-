#day 1 advent of code 2023

calibration_nums = 0 #initialise the running total

with open('2023/day1/input.txt') as f:
    for line in f: #iterate over every line in the file
        numbers_in_line = []
        
        for char in line: #iterate over every character in the line
            try:
                numbers_in_line.append(int(char)) #if the number can be converted to an int, add it to the list
            except ValueError:
                pass
        
        this_line_calibration = int(f"{numbers_in_line[0]}{numbers_in_line[-1]}")#combine the first and last numbers from the line into a single number and convert to int 

        calibration_nums += this_line_calibration #add the number to the running total

#output the result
print(calibration_nums)