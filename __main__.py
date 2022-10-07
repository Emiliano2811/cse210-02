# from game.director import Director

# director = Director()
# director.start_game()

# from colorama import init, Fore
# import random
# individual_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# user_score = 300
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





# def game_points(): 
#     #player starts with 300 points 
#     #if guessed correctly 100 points
#     #if they guessed incorrectly loses 75 points
#     print("Your score is: {} points")



# def start_game():
#     individual_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#     start_number = random.choice(individual_cards)
#     return start_number 
    
    


# def individual_cards():
#     user_score = 300
#     individual_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#     while True:
#         random_card = random.choice(individual_cards)

#         old_random_card = 0 
#         if old_random_card > 0:
#             print(f"The card is: {old_random_card}") 
#             higher_or_lower = str(input("Higher or Lower? [h/l] "))
#             start_number = old_random_card 
#         elif old_random_card == 0:
#             start_number = start_game()
#             print(f"The card is: {start_game()}")
#             higher_or_lower = str(input("Higher or Lower? [h/l] "))
            

#         if higher_or_lower == "l" and start_number > random_card:
#             user_score = user_score+100
#             print(f"Your score: {user_score}")
#             print(f"The card number is:{random_card}")
#             random_card = old_random_card 
#             return old_random_card 
            
#         elif higher_or_lower == "h" and start_number < random_card:
#             user_score = user_score+100
#             print(f"Your score: {user_score}")
#             print(f"The card number is:{random_card}")
#             random_card = old_random_card 
#             return old_random_card 
            
#         elif higher_or_lower == "l" and start_number < random_card:
#             user_score = user_score-75
#             print(f"Your score: {user_score}")
#             print(f"The card number is:{random_card}")
#             random_card = old_random_card 
#             return old_random_card 
            
#         elif higher_or_lower == "h" and start_number > random_card:
#             user_score = user_score-75
#             print(f"Your score: {user_score}")
#             print(f"The card number is:{random_card}")
#             random_card = old_random_card 
#             return old_random_card 
            
#         else:
#             break



# individual_cards()

# # def higher_or_lower():
# #     if random_card == 

# if __name__ == "__main__":
#     main()
