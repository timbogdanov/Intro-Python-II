from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


def main():

    player = Player(input("Enter your name: "), room['outside'])

    while True:
        current_room = player.current_room

        print(
            f"Welcome {player.name} \n{current_room.name} \n{current_room.description}")

        user_input = input("[n]: North [e]: East [s]: South [w]: West ")
        directions = ('n', 's', 'e', 'w')

        if len(user_input) == 1:
            if user_input in directions:
                attempted_room = getattr(
                    current_room, f"{user_input}_to")
                if attempted_room != None:
                    player.change_room(attempted_room)
                else:
                    print("You cannot move in that direction")
            elif user_input == 'q':
                break
            else:
                print("Input not valid, please try again")


main()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
