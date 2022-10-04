from colorama import init, Fore 
import random 

init(autoreset=True) #this stops the color to just adjust to one print statement 

print(Fore.MAGENTA + r"""\
             _____   ___  ____________   _____   ___  ___  ___ _____ 
            /  __ \ / _ \ | ___ \  _  \ |  __ \ / _ \ |  \/  ||  ___|
            | /  \// /_\ \| |_/ / | | | | |  \// /_\ \| .  . || |__  
            | |    |  _  ||    /| | | | | | __ |  _  || |\/| ||  __| 
            | \__/\| | | || |\ \| |/ /  | |_\ \| | | || |  | || |___ 
             \____/\_| |_/\_| \_|___/    \____/\_| |_/\_|  |_/\____/ 
                                                            
    """)
 

def game_interface():
    
    while True: 
        print("The card is: {}")
        #random_decision = input(print("Higher or Lower? [h/l] "))
        print("Next card was: ")
        print("Your score is: {}")
        play_again = str(input(print("Play again? [y/n] ")))
        if play_again =="y":
            game_interface()
        else: 
            pass



start_game = input(print("Please enter 1 to play press 2 to exit"))
if start_game == "1": 
    game_interface()

else: 
    print("Okay goodbye")
