f = open("2023/day5/input.txt", "r")
list_of_lines = f.read().split('\n')
f.close()

for line in list_of_lines
    seed_number = 2149186375

    test_case = input()

    test_case = test_case.split(" ")


    test_range = int(test_case[2])
    source_start_val = int(test_case[1])

    source_end_val = source_start_val + (test_range-1)

    if seed_number >= source_start_val and seed_number <= source_end_val:
        destination_val = int(test_case[0])

        actual_destination = destination_val + (seed_number - source_start_val)
        
    if not actual_destination
        
