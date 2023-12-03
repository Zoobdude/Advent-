f = open("2023/day3/input.txt", "r")
list_of_lines = f.read().split('\n')
f.close()


part_number_counter = 0
NON_SPECIAL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
num_of_lines_in_input = len(list_of_lines)
print(num_of_lines_in_input)

LINE_LENGTH = 140

for i, line in enumerate(list_of_lines):
    part_of_part_number = False
    part_number_joiner = ""
    
    print("working on line", line)
    
    for j, char in enumerate(line):
        print("---------------")
        print("checking char", char)
        try:
            int(char)
        
        except ValueError:
            if part_of_part_number:
                part_number_counter += int(part_number_joiner)
                print(part_number_joiner + " was valid")

                part_of_part_number = False
            
            part_number_joiner = ""
    
        else:
            if j-1 > -1:
                if line[j-1] not in NON_SPECIAL: #checks if the previous char in the current line was special
                    part_of_part_number = True
            
            if LINE_LENGTH > j+1:
                if line[j+1] not in NON_SPECIAL: #checks if next char in current line is spcial
                    part_of_part_number = True
            
            if i > 0: #checks it's not the first line of the file
                print("cheking line above")
                line_above = list_of_lines[i-1]
                
                if line_above[j] not in NON_SPECIAL: #checks if the char above is special
                    part_of_part_number = True
                
                if j-1 > -1:    
                    if line_above[j-1] not in NON_SPECIAL: #checks if the char diagonaly left above is special
                        part_of_part_number = True
                if LINE_LENGTH > j+1:
                    if line_above[j+1] not in NON_SPECIAL: #checks if the char diagonly right above is special
                        part_of_part_number = True
                    
            if num_of_lines_in_input > i+1:
                print("checking line below")
                line_below = list_of_lines[i+1]
                 
                if line_below[j] not in NON_SPECIAL: #checks if the char below is special
                    part_of_part_number = True
                
                if j-1 > -1:      
                    if line_below[j-1] not in NON_SPECIAL: #checks if the char diagonaly left below is special
                        part_of_part_number = True
                if LINE_LENGTH > j+1:   
                    if line_below[j+1] not in NON_SPECIAL: #checks if the char diagonly right below is special
                        part_of_part_number = True
                
            part_number_joiner += char

        if j == LINE_LENGTH-1: #subtract one because it indexes from zero
            if part_of_part_number:
                part_number_counter += int(part_number_joiner)
                print(part_number_joiner + " was valid")

                part_of_part_number = False
            
            
print(part_number_counter)