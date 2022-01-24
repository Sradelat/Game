# POSSIBLE IMPROVEMENTS
# ?ghost creature gives reward for polite
# ?use while loop for enemy health
# Going back and using a Class would be a code update

# INTRO

print("Hello! What is your name?\n")
name = input(">")
print("We are going to play a game. You will be given a description of your surroundings.")
print("Then, you will be given a choice of what you would like to do.")
print("For example:")
print("There is a fork in the road. Would you like to go left or right?\n(left/right)")
print("     ^\n     | You must type one of the options to continue.\n\n")
print("Okay! Here we go.\n\n")
print(name + ", wake up!")

# TOOLS


def death_check(health):
    if health <= 0:
        print("\nYOU DIED.")
        print("\nWould you like start from the beginning?\n(yes/no)")
        choice = input(">").lower()
        if choice == "yes":
            forest(10, 5, False, False, False, False, False)
        if choice == "no":
            print("Thanks for playing!")
            quit()


def stats(health, mana):
    print("You have " + str(health) + " health and " + str(mana) + " mana.")


def invalid():
    print("Invalid command. Try again.")


# LOCATIONS

def forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle):
    print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
    print("You find yourself in a clearing surrounded by trees in a mossy forest. In one direction, you hear the sound")
    print("of rushing water. In the other, you spot a faint blue light in the mixture of trees and fog.")
    print("Do you follow the sound of the water or do you inspect the light among the trees?\n\n(water/trees)")
    while True:  # new update
        choice = input(">").lower()
        if choice == "water":
            water(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
        elif choice == "trees":
            trees(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
        elif choice == "stats":
            stats(health, mana)
        elif choice != "water" or "trees" or "stats":
            invalid()


def trees(health, mana, bubble, seed, c_trees, c_water, c_puzzle):
    print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
    if not c_trees:
        print("You begin moving towards the light. Each tree you pass is curling and fantastical. As you get closer to")
        print("the blue light, you realize the source of it is a tiny, ornate lamp mounted to a tree. Next to the")
        print("lamp is a small door.\n\n(knock/open/back)")
        choice = input(">").lower()
        if choice == "knock":  # trees
            print("A moment passes by unanswered. Then, a small ghostly creature opens the door. You are not")
            print("frightened by him, but his eyes seem to pierce right through you. He is terrified at what he sees.")
            print("You feel uneasy.\n\n(look around/make peace)")
            choice = input(">").lower()
            if choice == "look around":  # trees > knock
                print("You notice the ghost is not scared of you but of a large soul eating toad behind you. The")
                print("creature is without a bottom jaw, and you can feel your being getting pulled into the blackness")
                print("that replaces it.")
                print("\n(weave spell/slash)")
                choice = input(">").lower()
                if choice == "weave spell":  # trees > knock > look around > COMPLETE
                    mana = mana - 3
                    print("\nYou spend 3 mana. Leaving you with " + str(mana) + " mana.")
                    print("Your body reacts almost with familiarity as you fire a bright blue beam from\n")
                    print("your outstretched arm and the giant soul sucking toad melts to the ground.\n")
                    print("You turn to see the ghost cowering behind the door now only slightly ajar. After a moment,")
                    print("you see his expression change to a cheerful one. The little creature's body whistles as he")
                    print("withdraws back into his shelter chirping, " + name + "! " + name + "! It comes back out")
                    print("presenting you with what looks like a bubble. It physically acts like a normal bubble, but")
                    print("it does not pop as you handle it. Your new friend disappears into his shelter again and")
                    print("closes the door. You figure its best to head back before something else shows up.")
                    bubble = True
                    c_trees = True
                    forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
                if choice == "slash":  # trees > knock > look around > COMPLETE
                    print("You stare into the toad's abyss as it drags you in. You swore you saw something staring")
                    print("back. You snap out of a daze and your fingers elongate, sharp as knives. You frantically")
                    print("shred away at the toad's head until the abyss fades and the toad goes limp. You're still")
                    print("in one piece, but you feel faint.")
                    health = health - 5
                    print("\nYou lost 5 health.")
                    death_check(health)
                    print("You now have " + str(health) + " health.\n")
                    print("You turn to see the ghost cowering behind the door now only slightly ajar. After a moment,")
                    print("you see his expression change to a cheerful one. The little creature's body whistles as he")
                    print("withdraws back into his shelter chirping, " + name + "! " + name + "! It comes back out")
                    print("presenting you with what looks like a bubble. It physically acts like a normal bubble, but")
                    print("it does not pop as you handle it. Your new friend disappears into his shelter again and")
                    print("closes the door. You figure its best to head back before something else shows up.")
                    bubble = True
                    c_trees = True
                    forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            if choice == "make peace":  # trees > knock > make peace > DEATH
                print("You feel your substance being dragged from behind. Before you can turn around your mind goes\n"
                      "blank.")
                health = 0
                death_check(health)
        if choice == "open":  # trees
            print("You open the door and a small ghostly creature rips at your arm with its jagged teeth.\n")
            health = health - 3
            print("You lost 3 health.")
            death_check(health)
            print("You now have " + str(health) + " health.\n")
            print("You react quickly to the attack without hesitation.\n(bash/pry)")
            choice = input(">").lower()
            if choice == "bash":  # trees > open
                print("You bash the little creature still attached to your arm into the tree. The force of the impact")
                print("makes it shriek in pain. The creature then falls to the ground and its form slowly fades away.")
                print("\nThe commotion has grabbed the attention of something nearby. You notice a large soul eating")
                print("toad approaching you. The toad is without a bottom jaw, and you can feel your being getting")
                print("pulled into the blackness that replaces it.")
                print("\n(weave spell/slash)\n")
                # key = True
                choice = input(">").lower()
                if choice == "weave spell":  # trees > open > bash
                    mana = mana - 3
                    print("\nYou spend 3 mana. Leaving you with " + str(mana) + " mana.")
                    print("Your body reacts almost with familiarity as you fire a bright blue beam from\n"
                          "the palm of your hand and the giant soul sucking toad melts to the ground.\n")
                    choice = input(">").lower()
                if choice == "slash":  # trees > open > bash > COMPLETE
                    print("You stare into the toad's abyss as it drags you in. You swore you saw something staring")
                    print("back. You snap out of a daze and your fingers elongate, sharp as knives. You frantically")
                    print("shred away at the toad's head until the abyss fades and the toad goes limp. You're still")
                    print("in one piece, but you feel faint.")
                    health = health - 5
                    print("\nYou lost 5 health.")
                    death_check(health)
                    print("You now have " + str(health) + " health.\n")
                    print("You check inside the small door and you find a small bubble that doesn't pop as you handle"
                          "it like you expected it would. You also notice that your arm, no, your entire body is just"
                          "as transparent as the bubble is. Just before you turn around to leave, the door slowly"
                          "closes. Then you head back the way you came.")
                    bubble = True
                    c_trees = True
                    forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            if choice == "pry":  # trees > open > COMPLETE
                print("You pry the little ghostly figure off of your arm. You and the creature together realize")
                print("the two of you are of the same opacity. The little creature's body whistles as he withdraws")
                print("back into the doorway chirping, " + name + "! " + name + "! It comes back out presenting you")
                print("with what looks like a bubble. It physically acts like a normal bubble, but it does not pop as")
                print("you handle it.\n")
                print("Your new friend motions into the distance and brings your attention to a large shadow lurking")
                print("in the fog. When you turn back to the door, it is closed and locked. You decide it is best to")
                print("listen to the unsettling feeling you have and go back the way you came.")
                bubble = True
                c_trees = True
                forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
        if choice == "back":
            forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
    if c_trees:
        print("You return to the tree with the lamp and small door. Despite your efforts, it will not open again.")
        print("Therefore, you head back the way you came.")
        forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)


def water(health, mana, bubble, seed, c_trees, c_water, c_puzzle):
    print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
    if not c_water:
        print("You walk towards the sound of the rushing water and find a sparkling, green river.\n(drink/soak/back)\n")
        choice = input(">").lower()
        if choice == "drink":
            health = health + 5
            print("You take a sip of water.")
            print("\nYou gain 5 health.")
            print("You now have " + str(health) + " health.\n")
            c_water = True
        if choice == "soak":
            mana = mana + 3
            print("You take a dip in the water.")
            print("\nYou gain 3 mana.")
            print("You now have " + str(mana) + " mana. \n")
            c_water = True
        if choice == "back":
            print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
    if c_water:
        print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
        print("Looking up and down the wide river, you see a pathway that follows its curves. You also notice that")
        print("there is no fog near the water. You think the path will eventually lead you somewhere. Do you go")
        print("upstream, downstream, or back to the clearing?\n(downstream/upstream/back)\n")
        choice = input(">").lower()
        if choice == "downstream":
            if c_puzzle is False:
                print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
                print("Following the current eases your nerves. Perhaps its because the water is becoming more calm as you")
                print("move along. As the droning of the river fades, an eerie silence sets in. Just as strange, the")
                print("river that was deep and surging further upstream, has now dwindled to a slight trickle over the")
                print("river bed's pebbles. The stream, at its end, displays a stone tablet under a gleaming pillar of")
                print("sunlight. On the tablet is a series of symbols that you surmise is a language. The symbols begin to")
                print("glow green as you approach. There is a small glowing crater above each column of symbols and beside")
                print("each row. The only way to interact with it seems to be to touch the fingertip sized craters. When")
                print("you do, the symbols shift.")
                print("Attempt puzzle or go back? (puzzle/back)")
                choice = input(">").lower()
                if choice == "puzzle":
                    puzzle_grid = [
                        ["\\", "-", "/"],
                        ["-", ":", "x"],
                        ["/", ":", "\\"]
                    ]
                    print("TUTORIAL:")
                    print("Each interactable is labeled with a number. Simply input a number to interact with it.")
                    print("1 2 3")
                    print("\ - / 4")
                    print("- : x 5")
                    print("/ : \ 6\n\n")
                    print("Type back if you want to leave the area and reset the puzzle.\n")

                    row1 = puzzle_grid[0]
                    row2 = puzzle_grid[1]
                    row3 = puzzle_grid[2]
                    # attempts = 0
                    for row in puzzle_grid:
                        for col in row:
                            print(col, end=" ")
                        print()
                    while True:
                        ans = input("\nWhich button do you press? \n")
                        if ans == "back":
                            break
                        if ans == "4":
                            row1.insert(2, row1.pop(0))
                            for row in puzzle_grid:
                                for col in row:
                                    print(col, end=" ")
                                print()
                        if ans == "5":
                            row2.insert(2, row2.pop(0))
                            for row in puzzle_grid:
                                for col in row:
                                    print(col, end=" ")
                                print()
                        if ans == "6":
                            row3.insert(2, row3.pop(0))
                            for row in puzzle_grid:
                                for col in row:
                                    print(col, end=" ")
                                print()
                        if ans == "1":
                            row1.insert(0, row3.pop(0))
                            row2.insert(0, row1.pop(1))
                            row3.insert(0, row2.pop(1))
                            for row in puzzle_grid:
                                for col in row:
                                    print(col, end=" ")
                                print()
                        if ans == "2":
                            row1.insert(1, row3.pop(1))
                            row2.insert(1, row1.pop(2))
                            row3.insert(1, row2.pop(2))
                            for row in puzzle_grid:
                                for col in row:
                                    print(col, end=" ")
                                print()
                        if ans == "3":
                            row1.insert(2, row3.pop(2))
                            row2.insert(2, row1.pop(3))
                            row3.insert(2, row2.pop(3))
                            for row in puzzle_grid:
                                for col in row:
                                    print(col, end=" ")
                                print()
                        if puzzle_grid == [
                            ["\\", ":", "/"],
                            ["-", "x", "-"],
                            ["/", ":", "\\"]
                        ]:
                            print("The symbol glows radiantly and you are given a small perfectly spherical seed.")
                            print("There seems to be nothing else to do here, so you travel back upstream.")
                            seed = True
                            c_puzzle = True
                            break
                    water(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
                if choice == "back":
                    water(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            if c_puzzle is True:
                print("There seems to be nothing else to do here so you travel back upstream.")
                water(health, mana, bubble, seed, c_trees, c_water, c_puzzle)

            #       "Before you approach the tablet, something catches your eye in the sea of pebbles. You"
            #       "scan over the bed and see nothing. Maybe it was just the way the light hit water. Do you"
            #       "investigate the river bed or approach the tablet?(river bed/tablet/back)")
            # choice = input(">").lower()
            # if choice == "river bed":
            #     print("You trust your intuition and check over the river bed.")
            # if choice == "tablet":
            #     print('"It was nothing," you think to yourself. You traverse the bed and on the tablet you find ????')
            #     print("Your focus on the tablet is broken by what sounds like the faint sound of two pebbles
            #     colliding")
            #     print("You turn around ")
        if choice == "upstream":
            print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            print("You decide to travel against the flow of the river. The further you travel the more violent the")
            print("river becomes. The shimmering water now crashing against and rushing around large jagged rocks.")
            print("You hear a waterfall ahead long before you see it. There is brilliant green in freefall. At the")
            print("bottom the resulting mist never falls. It just floats and flutters into the sky glittering until")
            print("out of view. A curling and twisting tree trunk reaches from the bank and wraps around a large")
            print("jagged rock planted in front of the base of the waterfall. The rock appears to have some markings")
            print("on it. You traverse the tree trunk to get a closer look. Upon inspection you find two small but")
            print("smooth spherical impressions. There is also a symbol carved into the rock.")
            print("\ : /")
            print("- x -")
            print("/ : \ \n\n")
            # if bubble or seed == False:
            #     print("There seems to be nothing else to do here so you travel back downstream.")
            #     water(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            if bubble is False:
                print("There seems to be nothing else to do here, so you travel back downstream.")
                water(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            if seed is False:
                print("There seems to be nothing else to do here, so you travel back downstream.")
                water(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            if bubble and seed is True:
                print("You beat the game!")
                input("Press Enter to close.")
                quit()
        if choice == "back":
            print(health, mana, bubble, seed, c_trees, c_water, c_puzzle)
            forest(health, mana, bubble, seed, c_trees, c_water, c_puzzle)

# START GAME


forest(10, 5, False, False, False, False, False)
