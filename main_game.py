from colorama import init, Fore
import random


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
    if start_game == 1:
        game_interface()

    else:
        print("Okay goodbye")


def game_interface():
    run = True
    while run:
        print("The card is: ")
        #random_decision = input(print("Higher or Lower? [h/l] "))
        print("Next card was: ")
        print("Your score is: ")
        play_again = input("Play again? [y/n] ")
        if play_again == "y":
            game_interface()
        elif play_again == "n":
            run = False


if __name__ == "__main__":
    main()
