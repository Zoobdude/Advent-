with open('2023/day1/input.txt', 'r') as input_file:
    input_lines = input_file.read().split('\n')

calibration_nums = []


with open('2023/day1/input.txt') as f:
    for line in f:
        numbers_in_line = []
        
        for char in line:
            try:
                numbers_in_line.append(int(char))
            except ValueError:
                pass
        print(numbers_in_line)
        
        this_line_calibration = int(f"{numbers_in_line[0]}{numbers_in_line[-1]}")
        calibration_nums.append(this_line_calibration)


print(sum(calibration_nums))