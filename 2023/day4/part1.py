f = open("2023/day4/input.txt", "r")
list_of_lines = f.read().split('\n')
f.close()

total_score_counter = 0 #

for line in list_of_lines:
    card_score_counter = 0
    
    winning_numbers, my_numbers = line.split("|")
    winning_numbers = winning_numbers.split(":")[1] #remove the card number
    
    winning_numbers = list(filter(None, winning_numbers.split(" "))) #remove blank indexes using filter
    my_numbers = list(filter(None, my_numbers.split(" ")))
    
    for num in my_numbers:
        if num in winning_numbers:
            if not card_score_counter: #if its the first winning card the score must be set to 1
                card_score_counter = 1
            
            else:
                card_score_counter *= 2
    total_score_counter += card_score_counter

print(total_score_counter)
