f = open("2023/day2/input.txt", "r")

NUM_OF_DIE = { #number of each colour of die available
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

valid_game_count = 0 #counter of all valid game IDs

for game in f.readlines(): #iterate through each game
    game_id, game_data = game.split(":")
    game_id = game_id.split(" ")[1] #get rid of the "game" part of the game ID
    print("working on game " + game_id)
    subsets = game_data.split(";") #split the subsets of the game
    game_invalid = False #set a flag that will be set to True if any one of the subsets is invalid
    
    for subset in subsets:
        if game_invalid: #if the game is already invalid, don't bother checking the rest of the subsets
            break
        
        cubes_in_subset = subset.split(",") #split up the separate cubes in the subset
        for cube in cubes_in_subset:
            for colour_of_cube in NUM_OF_DIE: #iterate through each colour of die 
                if colour_of_cube in cube:
                    number_of_that_cube = int(cube.replace(colour_of_cube, "")) #get the number of that colour of die
                    if number_of_that_cube > NUM_OF_DIE[colour_of_cube]: #if theres more of that die required than available, the entire game is invalid
                        game_invalid = True
                        
    if game_invalid == False:
        valid_game_count += int(game_id) #if the game is valid, add the game ID to the total
        print("game {} was valid".format(game_id))
                    

print(valid_game_count)
  
f.close()