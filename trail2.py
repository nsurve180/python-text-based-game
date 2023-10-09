import time
import random

visited_locations = []  # To store visited locations
player_inventory = []  # To store items the player collects

def introduction():
    print("Welcome, Chosen One, to the Treasure Hunt!")
    time.sleep(1)
    player_name = input("What is your name, Chosen One? ")
    print(f"Welcome, {player_name}, to the Treasure Hunt!")
    time.sleep(1)
    print(f"{player_name}, you find yourself on a remote island with a mysterious treasure map in hand.")
    time.sleep(1)
    print("It is said that only the Chosen One can unlock the secrets of this treasure.")
    time.sleep(1)
    print("Your goal is to follow the clues and find the hidden treasure.")
    time.sleep(1)
    print("Let's begin your adventure!")

def beach():
    print("\nYou start your journey on a beautiful sandy beach.")
    time.sleep(1)
    options = []

    if 'jungle' not in visited_locations:
        print("1. Follow the path into the dense jungle.")
        options.append("1")
    if 'cliffs' not in visited_locations:
        print("2. Explore the rocky cliffs to your left.")
        options.append("2")
    if 'shipwreck' not in visited_locations:
        print("3. Check the old shipwreck on your right.")
        options.append("3")

    if options:
        choice = input("Which path will you choose? (" + "/".join(options) + "): ")

        if choice == '1' and 'jungle' not in visited_locations:
            jungle()
        elif choice == '2' and 'cliffs' not in visited_locations:
            cliffs()
        elif choice == '3' and 'shipwreck' not in visited_locations:
            shipwreck()
        else:
            print("Invalid choice. Try again.")
            beach()
    else:
        print("You have already explored all available paths.")
        continue_exploring()

def jungle():
    visited_locations.append('jungle')
    print("\nYou venture into the dense jungle.")
    time.sleep(1)
    print("The path is overgrown, and it's getting darker as you go deeper.")
    time.sleep(1)

    # Encounter with locals who provide a hint
    print("You meet some locals who recognize you as the Chosen One.")
    time.sleep(1)
    print("They say, 'The treasure you seek lies deep within this jungle, Chosen One.'")
    time.sleep(1)

    # Encounter with a demon
    print("As you proceed, a fierce demon blocks your path!")
    time.sleep(1)
    print("You must fight the demon to continue.")

    # Player's choice to fight or flee
    choice = input("Do you want to fight the demon or flee? (fight/flee): ")

    if choice == 'fight':
            print("The demon was too strong, and you were defeated. You wake up on the beach.")
            beach()
    elif choice == 'flee':
        print("You wisely choose to flee from the demon.")
        visited_locations.remove('jungle')  # Allow the player to revisit the jungle later
        beach()
    else:
        print("Invalid choice. Try again.")
        jungle()

def cliffs():
    visited_locations.append('cliffs')
    print("\nYou climb the rocky cliffs to explore.")
    time.sleep(1)
    print("From the top, you have a great view of the island.")
    time.sleep(1)

    # Encounter with a fisherman who provides a hint
    print("You meet a fisherman who recognizes you as the Chosen One.")
    time.sleep(1)
    print("He says, 'Legend has it that the treasure lies near a waterfall, Chosen One.'")
    time.sleep(1)
    print("You find an ancient riddle carved into the rocks:")
    time.sleep(1)
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind.")
    options = ["a) an echo", "b) a shadow", "c) a secret"]
    print("Choose the correct answer by typing the letter:")
    print("\n".join(options))
    answer = input("Your choice (a/b/c): ").lower()



    if answer == 'a':
        print("You've solved the riddle! You may proceed.")
        waterfall()
    else:
        print("That's not the correct answer. The riddle seems to be unsolvable for now.")
        # Unable to find the treasure outcome
        print("Unfortunately, you are unable to find the treasure.")
        time.sleep(1)
        print("But remember, Chosen One, legends never truly die.")
        time.sleep(1)
        print("You return to the village with stories of your adventure.")
        time.sleep(1)
        print("Thanks for playing!")

def shipwreck():
    visited_locations.append('shipwreck')
    print("\nYou investigate the old shipwreck.")
    time.sleep(1)

    # Discovery of a hidden chest
    print("The ship is in ruins, but you find a hidden chest inside:")
    time.sleep(1)
    print("1. Open the chest.")
    time.sleep(1)
    print("2. Leave the shipwreck and continue exploring.")
    choice = input("What will you do? (1/2): ")

    if choice == '1':
        treasure_found()
    elif choice == '2':
        continue_exploring()
    else:
        print("Invalid choice. Try again.")
        shipwreck()


def waterfall():
    visited_locations.append('waterfall')
    print("\nYou follow the path uphill and discover a beautiful waterfall.")
    time.sleep(1)

    # Decision to enter the cave with a riddle
    print("There's a small cave behind the waterfall:")
    time.sleep(1)

    # Riddle with options
    print("Inside the cave, you find an engraving on the wall:")
    time.sleep(1)
    print(
        "I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?")

    options = ["a) a fire", "b) a tree", "c) a river"]
    print("Choose the correct answer by typing the letter:")
    print("\n".join(options))

    answer = input("Your choice (a/b/c): ").lower()

    if answer == 'b':
        print("You've solved the riddle! You may proceed.")
        cave()
    else:
        print("That's not the correct answer. The riddle remains unsolved.")
        # Unable to find the treasure outcome
        print("Unfortunately, you are unable to find the treasure.")
        time.sleep(1)
        print("But remember, Chosen One, legends never truly die.")
        time.sleep(1)
        print("You return to the village with stories of your adventure.")
        time.sleep(1)
        print("Thanks for playing!")


def cave():
    visited_locations.append('cave')
    print("\nYou enter a dark cave.")
    time.sleep(1)
    print("It's damp and echoey, and you can hear the sound of dripping water.")
    time.sleep(1)

    # Riddle with options
    print("You find a puzzle on the cave wall:")
    time.sleep(1)
    print(
        "I'm taken from a mine, and shut up in a wooden case, from which I'm never released, and yet I am used by almost every person.")

    options = ["a) a treasure", "b) a secret", "c) a pencil lead"]
    print("Choose the correct answer by typing the letter:")
    print("\n".join(options))

    answer = input("Your choice (a/b/c): ").lower()

    if answer == 'c':
        print("You've solved the puzzle! You may proceed.")
        treasure_found()
    else:
        print("That's not the correct answer. The puzzle remains unsolved.")
        # Unable to find the treasure outcome
        print("Unfortunately, you are unable to find the treasure.")
        time.sleep(1)
        print("But remember, Chosen One, legends never truly die.")
        time.sleep(1)
        print("You return to the village with stories of your adventure.")
        time.sleep(1)
        print("Thanks for playing!")


def treasure_found():
    print("\nAs you venture deeper into the cave, you stumble upon a hidden treasure chest!")
    time.sleep(1)
    print("You've found the treasure!")
    time.sleep(1)
    print("Congratulations, Chosen One! You have fulfilled the prophecy and become a successful treasure hunter!")
    time.sleep(1)
    print("You return to the village as a hero, and your name is remembered for generations.")
    time.sleep(1)
    print("Thanks for playing!")
    exit()

def continue_exploring():
    print("\nYou decide to leave the shipwreck and continue exploring the island.")
    time.sleep(1)
    print("You search for more clues and keep your hopes up.")
    time.sleep(1)

    # Unable to find the treasure outcome
    print("Unfortunately, you are unable to find the treasure.")
    time.sleep(1)
    print("But remember, Chosen One, legends never truly die.")
    time.sleep(1)
    print("You return to the village with stories of your adventure.")
    time.sleep(1)
    print("Thanks for playing!")

# Main game loop
introduction()
beach()
