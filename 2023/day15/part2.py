f = open("2023/day15/input.txt", "r")
input_data = f.read()
f.close()

list_of_data = input_data.split(",")

boxes = [[] for i in range(256)]

def hash(string):
    running_total = 0
    for char in string:
        running_total += ord(char)
        running_total *= 17
        running_total %= 256
    return running_total

for i, item in enumerate(list_of_data):
    if "-" in item:
        box_lable_str = item.split("-")[0]
        box_lable_int = hash(box_lable_str)
        current_box  = boxes[box_lable_int]
        
        for lens in current_box:
            if box_lable_str in lens:
                current_box.remove(lens)
                boxes[box_lable_int] = current_box
    
    elif "=" in item:
        box_lable_str, focal_length = item.split("=")
        box_lable_int = hash(box_lable_str)
        
        current_box = boxes[box_lable_int]
        
        updated_box = False
        for lens in current_box:
            if box_lable_str in lens:
                location = current_box.index(lens)
                current_box.remove(lens)
                current_box.insert(location, box_lable_str+" "+focal_length)
                boxes[box_lable_int] = current_box
                updated_box = True
        
        if not updated_box:
            current_box.append(box_lable_str+" "+focal_length)
            boxes[box_lable_int] = current_box
    
focusing_power_total = 0
for i, box in enumerate(boxes):
    if len(box) == 0:
        continue
    
    focusing_power = 0
    for j, lens in enumerate(box):
        focal_length = int(lens.split(" ")[1])
        focusing_power += ((i +1) * (j+1) * focal_length)
    
    focusing_power_total += focusing_power
    

print(focusing_power_total)