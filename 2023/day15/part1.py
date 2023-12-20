f = open("2023/day15/input.txt", "r")
input_data = f.read()
f.close()

list_of_data = input_data.split(",")

running_total = 0

for i, item in enumerate(list_of_data):
    currrent_value = 0
    for char in item:
        currrent_value += ord(char)
        currrent_value *= 17
        currrent_value %= 256
        
    running_total += currrent_value
    
print(running_total)