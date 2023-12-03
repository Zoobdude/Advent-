f = open("2023/day2/input.txt", "r")

power = 0

for game in f.readlines(): #iterate through each game
    game_id, game_data = game.split(":")
    game_id = game_id.split(" ")[1] #get rid of the "game" part of the game ID
    print("working on game " + game_id)
    subsets = game_data.split(";") #split the subsets of the game
    
    power_for_this_game = 1
    
    num_of_die_required = { #setup a dictionary to store the number of each colour of die required
    "red" : 0,
    "green" : 0,
    "blue" : 0
    }
    for subset in subsets:
        cubes_in_subset = subset.split(",") #split up the separate cubes in the subset
        for cube in cubes_in_subset:
            for colour_of_cube in num_of_die_required: #iterate through each colour of die 
                if colour_of_cube in cube:
                    number_of_that_cube = int(cube.replace(colour_of_cube, "")) #get the number of that colour of die
                    if number_of_that_cube > num_of_die_required[colour_of_cube]: #check if we need to number of required die for that game
                        num_of_die_required[colour_of_cube] = number_of_that_cube
    
    for key in num_of_die_required: #multiply the number of each colour of die required together to get the total number of die required
        power_for_this_game *= num_of_die_required[key]
    
    power += power_for_this_game #add the power for this game to the running total of power
        


print(power)
  
f.close()