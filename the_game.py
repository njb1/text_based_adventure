##
## Added coded in main(),and create a function to ask for your name and return it.
##
import os

##### ACTIONS #####
def you_died(why):
    '''
    In: Passing in the string showing player how they dies 

    Result: 
    Prints reason why they player died. 
    Programme exits without error.
    '''
    print("{}. Good job!".format(why))

    # This exits the program entirely.
    exit(0)

### END ACTIONS ###

### CHARACTERS ###
def soldier():
    '''
    Encountering the soldier, the player chooses to attack, check or sneak.
    - attack: player dies and it is game over
    - check: sees what the soldier is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the soldier and wins the game
    '''
    # Actions on the soldier
    actions_dict = {"check":"You see the soldier is still sleeping, you need to get to that door on the right of him. What are you waiting for?",
                    "sneak":"You approach the soldier, he's still sleeping. Reaching for the door, you open it slowly and slip out.",
                    "attack":"You swiftly run towards the sleeping soldier and knock him out with the hilt of your dagger. Unfortunately it wasn't hard enough."}
    
    # While loop
    while True:
        action = input("What do you do? [attack | check | sneak] >").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("You just slipped through the door before the soldier realised it.")
                print("You are now outside, home free! Huzzah!\n")
                return 
            elif action == "attack":
                you_died("soldier woke with a grunt, and reached for his dagger and before you know it, the world goes dark and you just died. \n<GAME OVER>")

### END CHARACTERS ###

##### ROOMS #####
def blue_door_room():
    '''
    The player finds a treasure chest, options to investigate the treasure chest or soldier.

    If player chooses
    - Treasure chest: show its contents; option to take treasure or ignore it (proceeds to soldier)
    - soldier: After checking treasure chest, ignoring treasure chest to check soldier, it calls soldier() function
    '''
    # So our treasure_box list contains 4 items.
    treasure_box = ["Health potion", "Energy potion", "Boots", "Lazer Pistol"]
    print("You see a room with a metal box on the left, and a sleeping soldier on the right in front of the door")

    # Ask player what to do.
    action = input("What do you do, go left or right? > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!")

        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the soldier is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_box list, print the treasure.
            for treasure in treasure_box:
                print(treasure)

            # So much treasure, what to do? Take it or leave it.
            print("What do you want to do?")
            # Get number of items in treasure chest with len))
            num_items_in_chest = len(treasure_box)

            print(f"Take all {num_items_in_chest} treasure, press '1'")
            print("Leave it, press '2'")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                treasure_box.remove("Lazer Pistol")
                print("\tYou take the gun from the treasure box. It does looks exceedingly shiney.")
                print("\tWoohoo! Bounty and a shiney new gun. /drops your crappy dagger in the empty treasure box.")
                
                temp_treasure_list = treasure_box[:]
                treasure_contents = ", ".join(treasure_box)
                print(f"\tYou also receive {treasure_contents}.")

                # Removing all the rest of the items in the treasure chest
                for treasure in temp_treasure_list:
                    # Use list remove() function to remove each item in the chest.
                    treasure_box.remove(treasure)

                # Add the old sword in place of the new sword
                treasure_box.append("crappy dagger") 
                print(f"\tYou close the lid of the chest containing {treasure_box} for the next adventurer. /grins")
                print("Now onward to get past this sleeping soldier and the door to freedom.")
            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this soldier")
        elif choice == "2":
            print("Who needs treasure, let's get out of here.'")
    elif action.lower() in ["soldier", "right"]:
        print("Let's have fun with the soldier.")
    else:
        print("Well, not sure what you picked there, let's poke the soldier cos it's fun!")
    soldier()

def red_door_room():
    '''
    The red door rooom contains a giant mutant bunny.
    
    If a player types "flee" as an answer, player returns to the room with two doors,
    otherwise the player dies.
    '''
    print("There you see a giant mutant frog.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("flee or stay> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")
### END ROOMS ###

def get_player_name():
    '''
    Gets players name, may or may not be renamed depending on player's choice.
    Returns: Player name back (altered or unaltered)
    '''
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    name = input('A mechanical voice from a speaker in the cieling asks "What is your name?" > ')

    # This is just an alternative name that the game wants to call the player
    alt_name = "Meat Puppet"
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print(f"You are fun, {name.upper()}! Let's begin our adventure!")

    elif answer.lower() in ["n", "no"]:
        print(f"Ok, picky. {name.upper()} it is. Let's get started on our adventure.")
    else:
        print(f"Trying to be funny? Well, you will now be called {alt_name.upper()} anyway.")
        name = alt_name

    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in 
    # get_player_name() function. 
    # This is why indentation is important, variables declared in this block only exists in that block
    return name
    
def start_adventure():
    '''
    This function starts the adventure by allowing two options for 
    players to choose from: red or blue door

    Chosen option will print out the door chosen.
    '''
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    print("The red door has a picture of an animal on it")
    print("The blue door has a picture of a gun on it")
    door_picked = input("Do you pick the red door or blue door? > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")


def play_intro():
    ban = open("banner.txt", "r")
    print(ban.read())
    print("Everything is black...")
    print("But slowly the world comes into light and focus")
    print("You have awoken on the floor of a very clean, very empty room")

def main():
    '''
    Gets the players name by calling get_player_name() before starting the adventure.
    '''
    play_intro()
    player_name =  get_player_name()

    # Modify the code
    # - add taunting the soldier or talking
    # - sword fight with the soldier, and keep track of health points (HP)
    # - modifiy blue_door_room()'s if statement
    #   so it takes into account player typing "right" or "soldier"
 
    start_adventure()
    
    print("\nThe end\n")
    print(f"Thanks for playing, {player_name.upper()}")


if __name__ == '__main__':
    main()
    