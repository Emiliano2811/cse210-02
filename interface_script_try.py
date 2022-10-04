
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


if __name__ == "__main__":
    main()
