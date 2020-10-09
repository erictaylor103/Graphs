from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "/Users/erictaylor/Documents/Lambda/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = []

#Reverse directions
inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

def traverse(starting_room, visited=set()):
    #Create a list to keep track of each new path we take
    path = []
    #Find all the exits in the current_room by using looping through the get_exits() method
    #the get_exits() method comes from the room.py file
    for direction in player.current_room.get_exits():
        player.travel(direction)

        #If the player is in a room that is in the visited set, then go back by using the inverse direction
        if player.current_room in visited:
            player.travel(inverse_directions[direction])
        #Otherwise if the room has not been visited,
        #add the current_room that the player is in to the visited set
        else:
            visited.add(player.current_room)
            #And append the direction we took to the path
            path.append(direction)
            
            #Using recursion here to update path, current_room that we've visited, and the inverse direction
            path = path + traverse(player.current_room,visited)
            player.travel(inverse_directions[direction])
            path.append(inverse_directions[direction])
    
    return path
#this will add the current_room that the player has traversed to the traversal_path list
traversal_path = traverse(player.current_room)

############################################################################################

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")