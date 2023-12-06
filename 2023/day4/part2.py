f = open("2023/day4/input.txt", "r")
list_of_lines = f.read().split('\n')
f.close()

total_score_counter = 0 #

for i, line in enumerate(list_of_lines):
    print((i/len(list_of_lines))*100)
    card_score_counter = 0
    
    winning_numbers, my_numbers = line.split("|")
    winning_numbers = winning_numbers.split(":")[1] #remove the card number
    
    winning_numbers = list(filter(None, winning_numbers.split(" "))) #remove blank indexes using filter
    my_numbers = list(filter(None, my_numbers.split(" ")))
    
    wins = 0
    for num in my_numbers:
        if num in winning_numbers:
            wins += 1
    
    card_to_duplicate_index = i
    last_line_dupe = line
    for win in range(wins):
        while list_of_lines[card_to_duplicate_index] == last_line_dupe:
            card_to_duplicate_index += 1
        
        card_duplicated =list_of_lines[card_to_duplicate_index]
        card_to_duplicate_index += 1
        list_of_lines.insert(card_to_duplicate_index, card_duplicated)
        last_line_dupe = card_duplicated
        card_to_duplicate_index += 1
        
print("--------------")
print(len(list_of_lines))
