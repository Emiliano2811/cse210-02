from game.card import Card


class Director:
    def __init__(self):
        self.score = 0
        self.total_score = 0
        self.guess_score = 100
        self.failed_Score = 75
        self.run_game = True

    def start_game(self):
        """Start the game, it will run the loop to play
        """
        score = self.score
        total_score = 300
        while self.run_game:
            self.game_interface()
            keep_playing = self.play_again()
            if keep_playing == True:
                self.run_game = True
            elif keep_playing == False:
                self.run_game = False

    def game_interface(self):
        """This will show the interface and information of the game"""
        total_score = 300

        print("\nLet's play!")
        print("")
        card = Card()
        card_value = card.random_card()
        print(f"The card is: {card_value}")

        # the user will guess if higher or lower for the next card
        guess = self.higher_or_lower()

        # next card will be created
        next_card_value = card.random_card()
        print(f"Next card was: {next_card_value}")

        # sum or subtract points if guessed or not
        if next_card_value > card_value and guess == "h":
            total_score += self.guess_score
        elif next_card_value > card_value and guess == "l":
            total_score -= self.failed_Score
        elif next_card_value < card_value and guess == "l":
            total_score += self.guess_score
        elif next_card_value < card_value and guess == "h":
            total_score -= self.failed_Score
        final_score = total_score
        print(f"Your score is: {final_score}")

    def higher_or_lower(self):
        guess = input("Higher or lower? [h/l] ")
        return guess

    def play_again(self):
        """This will ask the player to play again or quit"""
        play_again = input("Play again? ")
        if play_again.lower() == "y":
            return True
        elif play_again.lower() == "n":
            return False
