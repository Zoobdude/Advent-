f = open("2023/day6/input.txt", "r")
list_of_lines = f.read().split('\n')
f.close()

times, distances = list_of_lines
times = times.split(":")[1]
times = times.split(" ")
times = list(filter(None, times))

distances = distances.split(":")[1]
distances = distances.split(" ")
distances = list(filter(None, distances))

total_methods_multiplyer = 1

current_race_duration = int("".join(distances))
current_race_record = int("".join(times))

print(current_race_duration, current_race_record)

race_won = False 
i = 1

count_of_different_ways_to_win = 0
for j in range(1, current_race_duration):
    distance_traveled = j * (current_race_duration - j)
    
    if distance_traveled > current_race_record:
       print(j)

print(count_of_different_ways_to_win)

final_win = current_race_duration - i
count_of_wins = (final_win -i)

print(count_of_wins)