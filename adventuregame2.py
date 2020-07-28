import time
import random
items = []

random_item = None
random_weapon = None

def monsters():
    list = ['Goblin the Illtempered Creep', 'Old Man Grabhands', 'The Leprechaun of infinite Terror']
    global random_item
    if not random_item:
        random_item = random.choice(list)

    return random_item

def weapons():
    fightstuff = ['The Sword of Ogoroth', 'The Wand of Mischeif', 'The Hankercheif of Darkness']
    global random_weapon
    if not random_weapon:
        random_weapon = random.choice(fightstuff)

    return random_weapon

def begin():
    global random_weapon
    random_weapon = None
    for e in range (3):
        print(weapons())

def start():
    global random_item
    random_item = None
    for i in range (3):
        print(monsters())

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt).lower()
        if option1 in choice:
            break
        elif option2 in choice:
            break
        else:
            print_pause("That is not an option. Try again.")
    return choice

def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that " + (monsters()) + " is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")

def where_to_go():
        print_pause("Enter '1' to knock on the door of the house.")
        print_pause("Enter '2' to peer into the cave.\n")
        choice = valid_input("What would you like to do?\n", "1", "2")
        if '1' in choice:
            knock()
        elif '2' in choice:
            cave()

def cave():
    print_pause("You peer cautiously into the cave.")
    if "fightstuff" in items:
        print_pause("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.")
        print_pause("You return to the field")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glimpse of something behind a rock.")
        print_pause("You have found " + (weapons()) + "!")
        print_pause("You disgard your silly old dagger and take "
                    + (weapons()) + " with you.")
        print_pause("You return to the field.")
        items.append("fightstuff")
    where_to_go()

def knock():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps " + (monsters()) + ".")
    print_pause("Eep! This is " + (monsters()) + "'s house!")
    if "fightstuff" in items:
        choice = valid_input("Would you like to fight(y) or flee(n)?\n"
                             "Please type 'y' or 'n'\n", "y", "n")
        if choice == "y":
            print_pause("As " + (monsters()) + " moves to attack, you unsheath "
                        "your new weapon.")
            print_pause("With " + (weapons()) + " held fiercly "
                        "in your hand as you brace yourself for "
                        "the attack.")
            print_pause("But " + (monsters()) + " takes one look at your "
                        "intimidating new toy and runs away!")
            print_pause("You have rid the town of " + (monsters()) + ".")
            print_pause("You are victorious!")
        else:
            print_pause("You run back to the field. Luckily, you don't seem "
                  "to have been followed.")
            where_to_go()
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        choice = valid_input("Would you like to fight(y) or flee(n)?\n"
                             "Please type 'y' or 'n'\n", "y", "n")
        if choice == "n":
                print_pause("You run back to the field. Luckily, you don't seem "
                      "to have been followed.")
                where_to_go()
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for " + (monsters()) + ".")
            print_pause("You have been defeated!")

def play_again():
    choice = valid_input("Would you like to play again?\n"
                         "Please enter 'y' or 'n'\n",
                         "y", "n")
    if "y" in choice:
        print_pause("Very good, restarting game...")
        play_game()
    else:
        print_pause("Ok, goodbye.")

def play_game():
    intro()
    where_to_go()
    play_again()

play_game()
