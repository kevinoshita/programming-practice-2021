import random
import time


def battle_chap1():
    print("Commencing battle")
    time.sleep(5)
    print("\n" * 2)

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 50

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nYou will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nEcurb will go first.")


        print("\nYour health: ", player_health, "Ecurb's health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            player_movelist = {"Slash": random.randint(18, 25),
                     "Slice and Dice": random.randint(10, 35),
                     "Heal": random.randint(20, 25)}
            enemy_movelist = {"Stab": random.randint(9, 13),
                     "Deeper Stab": random.randint(5, 18),
                     "Heal": random.randint(10, 13)}

            if player_turn:
                print("\nPlease select a move:\n1. Slash (Deal damage between 18-25)\n2. Slice and Dice (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,5) # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("You missed!")
                else:
                    if player_move in ("1", "slash"):
                        player_move = player_movelist["Slash"]
                        print("\nYou used Slash. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "slice and dice"):
                        player_move = player_movelist["Slice and Dice"]
                        print("\nYou used Slice and Dice. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True # heal activated
                        player_move = player_movelist["Heal"]
                        print("\nYou used Heal. It healed for ", player_move, " health.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Ecurb missed!")
                else:
                    if computer_health > 15:
                        if player_health > 75:
                            computer_move = enemy_movelist["Stab"]
                            print("\nEcurb used Stab. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 75: # computer decides whether to go big or play it safe
                            imoves = ["Stab", "Deeper Stab"]
                            imoves = random.choice(imoves)
                            computer_move = enemy_movelist[imoves]
                            print("\nEcurb used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 35:
                            computer_move = enemy_movelist["Deeper Stab"]
                            print("\nEcurb used Deeper Stab. It dealt ", computer_move, " damage.")
                    else: # if the computer has little health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1,2)
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = enemy_movelist["Heal"]
                            print("\nEcurb used Heal. It healed for ", computer_move, " health.")
                        else:
                            if player_health > 75:
                                computer_move = enemy_movelist["Stab"]
                                print("\nEcurb used Stab. It dealt ", computer_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Stab", "Deeper Stab"]
                                imoves = random.choice(imoves)
                                computer_move = enemy_movelist[imoves]
                                print("\nEcurb used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 35:
                                computer_move = enemy_movelist["Deeper Stab"]
                                print("\nEcurb used Deeper Stab. It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 50:
                        computer_health = 50
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nYour health: ", player_health, "Ecurb's health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nYour health: ", player_health, "Ecurb's health: ", computer_health)
            print("\nCongratulations! You have won. You proceed to insult Ecurb: 'foolishness disgusts me'.")
            break
        else:
            print("\nYour health: ", player_health, "Ecurb's health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. As Ecurb dealt the final stab, "
                  "your conscious fades.")

        print("\nWould you like to play again? (answer 'yes' or 'y' to play again. Otherwise, continue to next scenario.)")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False
    time.sleep(10)
    print("\n" * 5)














def battle_chap2():
    print("Commencing battle")
    time.sleep(5)
    print("The elf that bumped into you does not seem to have a menacing aura.")
    time.sleep(3)
    print("You decide to not kill her, believing that she just needs mutual understanding.")
    time.sleep(3)
    print("Killing her will end the game, leave her at an HP of 10 or lower to finish the battle.")
    time.sleep(4)
    print("\n" * 2)

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 70

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nYou will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nElf will go first.")


        print("\nYour health: ", player_health, "Elf health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            player_movelist = {"Slash": random.randint(18, 25),
                     "Slice and Dice": random.randint(10, 35),
                     "Heal": random.randint(0, 0)}
            enemy_movelist = {"Shot": random.randint(13, 18),
                     "Power Shot": random.randint(7, 25),
                     "Vital Shot": random.randint(99, 99),
                     "Heal": random.randint(14, 18)}

            if player_turn:
                print("\nPlease select a move:\n1. Slash (Deal damage between 18-25)\n2. Slice and Dice (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,5) # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("You missed!")
                else:
                    if player_move in ("1", "slash"):
                        player_move = player_movelist["Slash"]
                        print("\nYou used Slash. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "slice and dice"):
                        player_move = player_movelist["Slice and Dice"]
                        print("\nYou used Slice and Dice. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True # heal activated
                        player_move = player_movelist["Heal"]
                        print("\nYou used Heal. It healed for ", player_move, " health.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Elf missed!")
                else:
                    if computer_health > 21:
                        if player_health > 75:
                            computer_move = enemy_movelist["Shot"]
                            print("\nElf used Shot. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 75: # computer decides whether to go big or play it safe
                            imoves = ["Shot", "Power Shot"]
                            imoves = random.choice(imoves)
                            computer_move = enemy_movelist[imoves]
                            print("\nElf used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 35 and player_health > 10:
                            computer_move = enemy_movelist["Power Shot"]
                            print("\nElf used Power Shot. It dealt ", computer_move, " damage.")
                        elif player_health <= 10:
                            computer_move = enemy_movelist["Vital Shot"]
                            print("\nElf used Vital Shot. It dealt ", computer_move, " damage. You feel a very stinging"
                                                                                     " pain in your heart.")
                    else: # if the computer has little health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1,2)
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = enemy_movelist["Heal"]
                            print("\nElf used Heal. It healed for ", computer_move, " health.")
                        else:
                            if player_health > 75:
                                computer_move = enemy_movelist["Shot"]
                                print("\nElf used Shot. It dealt ", computer_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Shot", "Power Shot"]
                                imoves = random.choice(imoves)
                                computer_move = enemy_movelist[imoves]
                                print("\nElf used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 35 and player_health > 10:
                                computer_move = enemy_movelist["Deeper Stab"]
                                print("\nElf used Power Shot. It dealt ", computer_move, " damage.")
                            elif player_health <= 10:
                                computer_move = enemy_movelist["Vital Shot"]
                                print("\nElf used Vital Shot. It dealt ", computer_move, " damage. You feel a very "
                                                                                         "stinging pain in your "
                                                                                         "heart.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 70:
                        computer_health = 70
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "Dead Computer"
                        break
                    elif computer_health > 0 and computer_health <= 10:
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nYour health: ", player_health, "Elf's health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nYour health: ", player_health, "Elf's health: ", computer_health)
            print("\nCongratulations! You have won. You proceed to approach the elf.")
            break
        elif winner == "Dead Computer":
            print("\nYour health: ", player_health, "Elf's health: ", computer_health)
            print("\nYou've slain the innocent elf by accident.")
        else:
            print("\nYour health: ", player_health, "Elf's health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. The elf looks at you with furious eyes while"
                  " leaving you.")

        print("\nWould you like to play again? (answer 'yes' or 'y' to play again. Otherwise, continue to next scenario.)")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False
    time.sleep(10)
    print("\n" * 5)










def battle_chap2_1():
    print("Commencing battle")
    time.sleep(5)
    print("\n" * 2)

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 999

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nWanderer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nGolem will go first.")


        print("\nWanderer's health: ", player_health, "Golem's health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            player_movelist = {"Slash": random.randint(1, 1),
                     "Slice and Dice": random.randint(1, 2),
                     "Heal": random.randint(20, 25)}
            enemy_movelist = {"Whacc": random.randint(24, 30),
                     "Bigger Whacc": random.randint(19, 38),
                     "Omega Whacc": random.randint(99, 99)}

            if player_turn:
                print("\nPlease select a move:\n1. Slash (Deals 1 damage)\n2. Slice and Dice (Deal damage between 1-2)\n3. Heal (Restore between 20-25 health)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,5) # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("Wanderer missed!")
                else:
                    if player_move in ("1", "slash"):
                        player_move = player_movelist["Slash"]
                        print("\nWanderer used Slash. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "slice and dice"):
                        player_move = player_movelist["Slice and Dice"]
                        print("\nWanderer used Slice and Dice. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True # heal activated
                        player_move = player_movelist["Heal"]
                        print("\nWanderer used Heal. It healed for ", player_move, " health.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Golem missed!")
                else:
                    if player_health > 75:
                        computer_move = enemy_movelist["Whacc"]
                        print("\nGolem used Whacc. It dealt ", computer_move, " damage.")
                    elif player_health > 35 and player_health <= 75:  # computer decides whether to go big or play it safe
                        imoves = ["Whacc", "Bigger Whacc"]
                        imoves = random.choice(imoves)
                        computer_move = enemy_movelist[imoves]
                        print("\nGolem used ", imoves, ". It dealt ", computer_move, " damage.")
                    elif player_health <= 35 and player_health > 10:
                        computer_move = enemy_movelist["Bigger Whacc"]
                        print("\nGolem used Bigger Whacc. It dealt ", computer_move, " damage.")
                    elif player_health <= 10:
                        computer_move = enemy_movelist["Omega Whacc"]
                        print("\nGolem used Omega Whacc. It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 999:
                        computer_health = 999
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nWanderer's health: ", player_health, "Golem's health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nWanderer's health: ", player_health, "Golem's health: ", computer_health)
            print("\nYou're not supposed to win.")
        else:
            print("\nWanderer's health: ", player_health, "Golem's health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. The golem continues to wreck more havoc.")
            break

        print("\nWould you like to play again? (answer 'yes' or 'y' to play again. Otherwise, continue to next scenario.)")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False
    time.sleep(10)
    print("\n" * 5)









def battle_chap3A():
    print("Commencing battle")
    time.sleep(5)
    print("From your fight with Nairdirina and the golem, you have learned a new attack: Slashburst Flurry.")
    time.sleep(3)
    print("Accuracy has also been increased from 80% to 90%.")
    time.sleep(3)
    print("\n" * 2)

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 1000

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nWanderer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nBlue-eyes White Dragon will go first.")


        print("\nWanderer's health: ", player_health, "Blue-eyes White Dragon's health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            player_movelist = {"Slash": random.randint(18, 25),
                     "Slice and Dice": random.randint(10, 35),
                     "Heal": random.randint(20, 25),
                     "Slashburst Flurry": random.randint(8, 42)}
            enemy_movelist = {"Fireball": random.randint(20, 28),
                     "Fireblaze": random.randint(14, 38),
                     "Gust of Wind": random.randint(18, 25),
                     "Tail Slam": random.randint(10, 35),
                     "Hellfire Judgement": random.randint(999, 999)}

            if player_turn:
                print("\nPlease select a move:\n1. Slash (Deal damage between 18-25)\n2. Slice and Dice (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n4. Slashburst Flurry (Deal damage between 8-42)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,10) # 10% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("Wanderer missed!")
                else:
                    if player_move in ("1", "slash"):
                        player_move = player_movelist["Slash"]
                        print("\nWanderer used Slash. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "slice and dice"):
                        player_move = player_movelist["Slice and Dice"]
                        print("\nWanderer used Slice and Dice. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True # heal activated
                        player_move = player_movelist["Heal"]
                        print("\nWanderer used Heal. It healed for ", player_move, " health.")
                    elif player_move in ("4", "slashburst flurry"):
                        player_move = player_movelist["Slashburst Flurry"]
                        print("\nWanderer used Slashburst Flurry. It dealt ", player_move, " damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Blue-eyes White Dragon missed!")
                else:
                    if player_health > 75:
                        imoves = ["Fireball", "Gust of Wind"]
                        imoves = random.choice(imoves)
                        computer_move = enemy_movelist[imoves]
                        print("\nBlue-eyes White Dragon used ", imoves, ". It dealt ", computer_move, " damage.")
                    elif player_health > 35 and player_health <= 75:  # computer decides whether to go big or play it safe
                        imoves = ["Fireball", "Gust of Wind", "Fireblaze", "Tail Slam"]
                        imoves = random.choice(imoves)
                        computer_move = enemy_movelist[imoves]
                        print("\nBlue-eyes White Dragon used ", imoves, ". It dealt ", computer_move, " damage.")
                    elif player_health <= 35 and player_health > 2:
                        imoves = ["Fireblaze", "Tail Slam"]
                        imoves = random.choice(imoves)
                        computer_move = enemy_movelist[imoves]
                        print("\nBlue-eyes White Dragon used ", imoves, ". It dealt ", computer_move, " damage.")
                    elif player_health <= 2:
                        computer_move = enemy_movelist["Hellfire Judgement"]
                        print("\nBlue-eyes White Dragon used Hellfire Judgement, it was SUPER EFFECTIVE!!! It "
                              "dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 1000:
                        computer_health = 1000
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 850:
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nWanderer's health: ", player_health, "Blue-eyes White Dragon's health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nWanderer's health: ", player_health, "Blue-eyes White Dragon's health: ", computer_health)
            print("\nYou realized that you have exhausted yourself, so you can't attack anymore.")
            break
        else:
            print("\nWanderer's health: ", player_health, "Blue-eyes White Dragon's health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. Blue-eyes White Dragon continues "
                  "to scorch you alive.")

        print("\nWould you like to play again? (answer 'yes' or 'y' to play again. Otherwise, continue to next scenario.)")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False
    time.sleep(10)
    print("\n" * 5)




def battle_chap3B():
    print("Commencing battle")
    time.sleep(5)
    print("From your fight with Nairdirina and the golem, you have learned a new attack: Slashburst Flurry.")
    time.sleep(3)
    print("Accuracy is 100% because enemy is too big for you to miss.")
    time.sleep(3)
    print("\n" * 2)

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 1000

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nWanderer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nWurm will go first.")


        print("\nWanderer's health: ", player_health, "Wurm's health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            player_movelist = {"Slash": random.randint(18, 25),
                     "Slice and Dice": random.randint(10, 35),
                     "Heal": random.randint(20, 25),
                     "Slashburst Flurry": random.randint(8, 42)}
            enemy_movelist = {"Chomp": random.randint(20, 27),
                     "Suck": random.randint(12, 37),
                     "Burrow": random.randint(18, 25),
                     "Tremor": random.randint(10, 35),
                     "Terramorphic Erosion": random.randint(999, 999)}

            if player_turn:
                print("\nPlease select a move:\n1. Slash (Deal damage between 18-25)\n2. Slice and Dice (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n4. Slashburst Flurry (Deal damage between 8-42)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1, 5)
                if move_miss == 6: #since enemy is a big, wurm, there is no way you can miss
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("Wanderer missed!")
                else:
                    if player_move in ("1", "slash"):
                        player_move = player_movelist["Slash"]
                        print("\nWanderer used Slash. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "slice and dice"):
                        player_move = player_movelist["Slice and Dice"]
                        print("\nWanderer used Slice and Dice. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True # heal activated
                        player_move = player_movelist["Heal"]
                        print("\nWanderer used Heal. It healed for ", player_move, " health.")
                    elif player_move in ("4", "slashburst flurry"):
                        player_move = player_movelist["Slashburst Flurry"]
                        print("\nWanderer used Slashburst Flurry. It dealt ", player_move, " damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 6:    #since enemy is a wurm, its attacks cannot miss
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Wurm missed!")
                else:
                    if player_health > 75:
                        imoves = ["Chomp", "Burrow"]
                        imoves = random.choice(imoves)
                        computer_move = enemy_movelist[imoves]
                        print("\nWurm used ", imoves, ". It dealt ", computer_move, " damage.")
                    elif player_health > 35 and player_health <= 75:  # computer decides whether to go big or play it safe
                        imoves = ["Chomp", "Burrow", "Suck", "Tremor"]
                        imoves = random.choice(imoves)
                        computer_move = enemy_movelist[imoves]
                        print("\nWurm used ", imoves, ". It dealt ", computer_move, " damage.")
                    elif player_health <= 35 and player_health > 2:
                        imoves = ["Suck", "Tremor"]
                        imoves = random.choice(imoves)
                        computer_move = enemy_movelist[imoves]
                        print("\nWurm used ", imoves, ". It dealt ", computer_move, " damage.")
                    elif player_health <= 2:
                        computer_move = enemy_movelist["Terramorphic Erosion"]
                        print("\nWurm used Terramorphic Erosion, it was SUPER EFFECTIVE!!! It "
                              "dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 1000:
                        computer_health = 1000
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 850:
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nWanderer's health: ", player_health, "Wurm's health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nWanderer's health: ", player_health, "Wurm's health: ", computer_health)
            print("\nDue to its attacks, the distance between you and the wurm has gotten farther,"
                  " you can't attack anymore.")
            break
        else:
            print("\nWanderer's health: ", player_health, "Wurm's health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. Wurm procceeds to consume you.")

        print("\nWould you like to play again? (answer 'yes' or 'y' to play again. Otherwise, continue to next scenario.)")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False
    time.sleep(10)
    print("\n" * 5)






def battle_chap4_training():
    print("Commencing battle")
    time.sleep(5)
    print("All your attacks deal higher damage and some names are changed.")
    time.sleep(3)
    print("Healing ability has also increased.")
    time.sleep(3)
    print("New attack has been added: Slice of luck")
    time.sleep(3)
    print("Health has also increased.")
    time.sleep(3)
    print("\n" * 2)

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 200
        computer_health = 200

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nWanderer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nCommander Langdorf will go first.")


        print("\nWanderer's health: ", player_health, "Commander Langdorf's health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            player_movelist = {"Strike": random.randint(28, 35),
                     "Cutting Edge Strike": random.randint(20, 45),
                     "Better Heal": random.randint(35, 50),
                     "Raging Slash": random.randint(18, 52),
                     "Slice of Luck": random.randint(0, 80)}
            enemy_movelist = {"Strike": random.randint(28, 35),
                     "Cutting Edge Strike": random.randint(20, 45),
                     "Better Heal": random.randint(35, 50),
                     "Raging Slash": random.randint(18, 52),
                     "Slice of Luck": random.randint(0, 80)}

            if player_turn:
                print("\nPlease select a move:\n1. Strike (Deal damage between 28-35)\n2. Cutting Edge Strike (Deal damage between 35-50)\n3. Better Heal (Restore between 35-50 health)\n4. Raging Slash (Deal damage between 18-52)\n5. Slice of Luck (Deal damage between 0-80)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,10) # 10% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("Wanderer missed!")
                else:
                    if player_move in ("1", "strike"):
                        player_move = player_movelist["Strike"]
                        print("\nWanderer used Strike. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "cutting edge strike"):
                        player_move = player_movelist["Cutting Edge Strike"]
                        print("\nWanderer used Cutting Edge Strike. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "better heal"):
                        heal_up = True # heal activated
                        player_move = player_movelist["Better Heal"]
                        print("\nWanderer used Better Heal. It healed for ", player_move, " health.")
                    elif player_move in ("4", "raging slash"):
                        player_move = player_movelist["Raging Slash"]
                        print("\nWanderer used Raging Slash. It dealt ", player_move, " damage.")
                    elif player_move in ("5", "slice of luck"):
                        player_move = player_movelist["Slice of Luck"]
                        print("\nWanderer used Slice of Luck. It dealt ", player_move, " damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,10)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Commander Langdorf missed!")
                else:
                    if computer_health > 35:
                        if player_health > 150:
                            computer_move = enemy_movelist["Strike"]
                            print("\nCommander Langdorf used Strike. It dealt ", computer_move, " damage.")
                        elif player_health > 70 and player_health <= 150:  # computer decides whether to go big or play it safe
                            imoves = ["Strike", "Cutting Edge Strike", "Raging Slash", "Slice of Luck"]
                            imoves = random.choice(imoves)
                            computer_move = enemy_movelist[imoves]
                            print("\nCommander Langdorf used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 70:
                            imoves = ["Raging Slash", "Slice of Luck"]
                            imoves = random.choice(imoves)
                            computer_move = enemy_movelist[imoves]
                            print("\nCommander Langdorf used ", imoves, ". It dealt ", computer_move, " damage.")
                    else:  # if the computer has little health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1, 2)
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = enemy_movelist["Better Heal"]
                            print("\nCommander Langdorf used Heal. It healed for ", computer_move, " health.")
                        else:
                            if player_health > 150:
                                computer_move = enemy_movelist["Strike"]
                                print("\nCommander Langdorf used Strike. It dealt ", computer_move, " damage.")
                            elif player_health > 70 and player_health <= 150:  # computer decides whether to go big or play it safe
                                imoves = ["Strike", "Cutting Edge Strike", "Raging Slash", "Slice of Luck"]
                                imoves = random.choice(imoves)
                                computer_move = enemy_movelist[imoves]
                                print("\nCommander Langdorf used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 70:
                                imoves = ["Raging Slash", "Slice of Luck"]
                                imoves = random.choice(imoves)
                                computer_move = enemy_movelist[imoves]
                                print("\nCommander Langdorf used ", imoves, ". It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 200:
                        player_health = 200 # cap max health. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 200:
                        computer_health = 200
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nWanderer's health: ", player_health, "Commander Langdorf's health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nWanderer's health: ", player_health, "Commander Langdorf's health: ", computer_health)
            print("\nCongratulations! You have won. You have proved your competence to the Commander.")
            time.sleep(3)
            print("Commander Langdorf: 'Nice, just like my expectations.'")
            break
        else:
            print("\nWanderer's health: ", player_health, "Commander Langdorf's health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. It seems you still have more to learn.")
            time.sleep(3)
            print("Commander Langdorf: 'Relax kid, you did well.'")
            break
    time.sleep(10)
    print("\n" * 5)




def battle_chap4_valorex():
    print("Commencing battle")
    time.sleep(5)
    print("\n" * 2)

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 200
        computer_health = 150

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nWanderer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nValorex will go first.")


        print("\nWanderer's health: ", player_health, "Valorex's health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            player_movelist = {"Strike": random.randint(28, 35),
                     "Cutting Edge Strike": random.randint(20, 45),
                     "Better Heal": random.randint(35, 50),
                     "Raging Slash": random.randint(18, 52),
                     "Slice of Luck": random.randint(0, 80)}
            enemy_movelist = {"??": random.randint(30, 37),
                     "???": random.randint(22, 47),
                     "+++": random.randint(35, 50),
                     "!!!": random.randint(20, 54)}

            if player_turn:
                print("\nPlease select a move:\n1. Strike (Deal damage between 28-35)\n2. Cutting Edge Strike (Deal damage between 35-50)\n3. Better Heal (Restore between 35-50 health)\n4. Raging Slash (Deal damage between 18-52)\n5. Slice of Luck (Deal damage between 0-80)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,3) # 33.3% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("Wanderer missed!")
                else:
                    if player_move in ("1", "strike"):
                        player_move = player_movelist["Strike"]
                        print("\nWanderer used Strike. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "cutting edge strike"):
                        player_move = player_movelist["Cutting Edge Strike"]
                        print("\nWanderer used Cutting Edge Strike. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "better heal"):
                        heal_up = True # heal activated
                        player_move = player_movelist["Better Heal"]
                        print("\nWanderer used Better Heal. It healed for ", player_move, " health.")
                    elif player_move in ("4", "raging slash"):
                        player_move = player_movelist["Raging Slash"]
                        print("\nWanderer used Raging Slash. It dealt ", player_move, " damage.")
                    elif player_move in ("5", "slice of luck"):
                        player_move = player_movelist["Slice of Luck"]
                        print("\nWanderer used Slice of Luck. It dealt ", player_move, " damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,10)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("Valorex missed!")
                else:
                    if computer_health > 35:
                        if player_health > 150:
                            computer_move = enemy_movelist["??"]
                            print("\nValorex used ??. It dealt ", computer_move, " damage.")
                        elif player_health > 70 and player_health <= 150:  # computer decides whether to go big or play it safe
                            imoves = ["??", "???", "!!!"]
                            imoves = random.choice(imoves)
                            computer_move = enemy_movelist[imoves]
                            print("\nValorex used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 70:
                            computer_move = enemy_movelist["!!!"]
                            print("\nValorex used !!!. It dealt ", computer_move, " damage.")
                    else:  # if the computer has little health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1, 2)
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = enemy_movelist["+++"]
                            print("\nValorex used +++. It healed for ", computer_move, " health.")
                        else:
                            if player_health > 150:
                                computer_move = enemy_movelist["??"]
                                print("\nValorex used ??. It dealt ", computer_move, " damage.")
                            elif player_health > 70 and player_health <= 150:  # computer decides whether to go big or play it safe
                                imoves = ["??", "???", "!!!"]
                                imoves = random.choice(imoves)
                                computer_move = enemy_movelist[imoves]
                                print("\nValorex used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 70:
                                computer_move = enemy_movelist["!!!"]
                                print("\nValorex used !!!. It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 200:
                        player_health = 200 # cap max health. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 150:
                        computer_health = 150
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 1  # cap minimum health at 1
                        winner = "Player"
                        break
                    elif computer_health > 0 and computer_health <= 20:
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 1  # cap minimum health at 1
                        winner = "Computer"
                        break
                    elif player_health > 0 and player_health <= 20:
                        winner = "Computer"
                        break

            print("\nWanderer's health: ", player_health, "Valorex's health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nWanderer's health: ", player_health, "Valorex's health: ", computer_health)
            print("\nCongratulations! You have won.")
            time.sleep(5)
            print("As you are about to deliver the killing blow, Valorex does a backflip and throws a smoke bomb.")
            time.sleep(5)
            print("Valorex: 'Same as the old days, ey? You’re as readable as those fairy tales that your "
                  "mom told you every night.'")
            time.sleep(5)
            print("Wanderer: 'What? Wait, how do you know me? Who the hell are you?'")
            time.sleep(4)
            print("\n" * 5)
            break
        else:
            print("\nWanderer's health: ", player_health, "Commander Langdorf's health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you.")
            time.sleep(5)
            print("Valorex is about to stab your neck, but as the dagger gets very close to your neck, the dagger"
                  " stops.")
            time.sleep(5)
            print("Valorex: 'See, 'peaceful' right? You live, I live.'")
            time.sleep(3)
            print("Wanderer: 'At least you are a man of your word, why don’t you finish me off?'")
            time.sleep(4)
            print("Valorex: 'Killing you now is not worth it. The next time we meet, checkmate.'")
            time.sleep(4)
            print("Valorex: 'I am actually here to confirm something, and now i know it.'")
            time.sleep(4)
            print("Wanderer: 'What do you know of me? Tell me this instance. Tell me who you are?'")
            time.sleep(4)
            print("\n" * 5)
            break