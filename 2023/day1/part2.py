with open('2023/day1/input.txt', 'r') as input_file:
    input_lines = input_file.read().split('\n')

calibration_nums = 0

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
        numbers_in_line = []
        number_and_index = {}

        for key in translate:
            if key in line:
                line = line.replace(key, translate[key])

      
        for char in line:
            try:
                numbers_in_line.append(int(char))
            except ValueError:
                pass


        this_line_calibration = int(f"{numbers_in_line[0]}{numbers_in_line[-1]}")
        print(this_line_calibration)
        calibration_nums += this_line_calibration
        print(calibration_nums)
