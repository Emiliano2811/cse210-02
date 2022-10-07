from game.card import Card


class Game:
    def __init__(self):
        self.score = 300
        self.run_game = True

    def start_game(self):
        """Start the game, it will run the loop to play
        """
        start_game = int(input("\nPlease enter 1 to play or 2 to exit: "))

        self.run_game
        if start_game == 1:
            while run == True:
                self.game_interface(self)
                keep_playing = self.play_again(self)
                if keep_playing == True:
                    run = True
                elif keep_playing == False:
                    run = False

        elif start_game == 2:
            print("\nSee you next time")

    def game_interface(self):
        print("\nLet's play!")
        print("")
        print("The card is: ")
        #random_decision = input(print("Higher or Lower? [h/l] "))
        print("Next card was: ")
        print("Your score is: ")

    def play_again(self):
        play_again = input("\nPlay again? ")
        if play_again.lower() == "y":
            return True
        elif play_again.lower() == "n":
            return False
