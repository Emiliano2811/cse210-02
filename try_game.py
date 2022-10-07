import random
from typing import ParamSpecArgs
user_score = 1 


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






# user_score = 300

# while True:
#     press = str(input("If you press y +100 if you press n -75"))
#     if press == "y":
#         user_score = user_score + 100
#         print(f"current score: {user_score}")
#     elif press == "n":
#         user_score = user_score - 75
#         print(f"current score: {user_score}")
#     else:
#         break
