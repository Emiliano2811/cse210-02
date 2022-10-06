from colorama import init, Fore
import random
individual_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
user_score = 300
# this stops the color to just adjust to one print statement
# init(autoreset=True)

# print(Fore.MAGENTA + r"""\
#              _____   ___  ____________   _____   ___  ___  ___ _____
#             /  __ \ / _ \ | ___ \  _  \ |  __ \ / _ \ |  \/  ||  ___|
#             | /  \// /_\ \| |_/ / | | | | |  \// /_\ \| .  . || |__
#             | |    |  _  ||    /| | | | | | __ |  _  || |\/| ||  __|
#             | \__/\| | | || |\ \| |/ /  | |_\ \| | | || |  | || |___
#              \____/\_| |_/\_| \_|___/    \____/\_| |_/\_|  |_/\____/

#     """)


def main():
    start_game = int(input("\nPlease enter 1 to play or 2 to exit: "))

    run = True
    if start_game == 1:
        while run == True:
            game_interface()
            keep_playing = play_again()
            if keep_playing == True:
                run = True
            elif keep_playing == False:
                run = False

    elif start_game == 2:
        print("\nSee you next time")

    
def game_interface():
    print("\nLet's play!")
    print("")
    print("The card is: ")
    #random_decision = input(print("Higher or Lower? [h/l] "))
    print("Next card was: ")
    print("Your score is: ")


def play_again():
    play_again = input("\nPlay again? ")
    if play_again.lower() == "y":
        return True
    elif play_again.lower() == "n":
        return False


def game_points(): 
    #player starts with 300 points 
    #if guessed correctly 100 points
    #if they guessed incorrectly loses 75 points
    print("Your score is: {} points")



def start_game():
    individual_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    start_number = random.choice(individual_cards)
    return start_number 
    
    


def individual_cards():
    user_score = 300
    individual_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    while True:
        random_card = random.choice(individual_cards)

        old_random_card = 0 
        if old_random_card > 0:
            print(f"The card is: {old_random_card}") 
            higher_or_lower = str(input("Higher or Lower? [h/l] "))
            start_number = old_random_card 
        elif old_random_card == 0:
            start_number = start_game()
            print(f"The card is: {start_game()}")
            higher_or_lower = str(input("Higher or Lower? [h/l] "))
            

        if higher_or_lower == "l" and start_number > random_card:
            user_score = user_score+100
            print(f"Your score: {user_score}")
            print(f"The card number is:{random_card}")
            random_card = old_random_card 
            return old_random_card 
            
        elif higher_or_lower == "h" and start_number < random_card:
            user_score = user_score+100
            print(f"Your score: {user_score}")
            print(f"The card number is:{random_card}")
            random_card = old_random_card 
            return old_random_card 
            
        elif higher_or_lower == "l" and start_number < random_card:
            user_score = user_score-75
            print(f"Your score: {user_score}")
            print(f"The card number is:{random_card}")
            random_card = old_random_card 
            return old_random_card 
            
        elif higher_or_lower == "h" and start_number > random_card:
            user_score = user_score-75
            print(f"Your score: {user_score}")
            print(f"The card number is:{random_card}")
            random_card = old_random_card 
            return old_random_card 
            
        else:
            break



individual_cards()

# def higher_or_lower():
#     if random_card == 

if __name__ == "__main__":
    main()
