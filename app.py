import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word_to_guess = ""
        self.guesses_remaining = 6
        self.guessed_letters = set()
        self.initialize_game()

    def initialize_game(self):
        self.word_to_guess = random.choice(self.word_list).lower()
        self.guesses_remaining = 6
        self.guessed_letters.clear()

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def make_guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            return "You already guessed that letter."
        elif letter in self.word_to_guess:
            self.guessed_letters.add(letter)
            if self.display_word() == self.word_to_guess:
                return "Congratulations! You've guessed the word: " + self.word_to_guess
            return "Correct guess!"
        else:
            self.guessed_letters.add(letter)
            self.guesses_remaining -= 1
            if self.guesses_remaining == 0:
                return "Game over! The word was: " + self.word_to_guess
            return "Incorrect guess. Guesses remaining: " + str(self.guesses_remaining)

def main():
    word_list = ["python", "hangman", "programming", "challenge"]
    game = HangmanGame(word_list)

    print("Welcome to Hangman!")

    while True:
        print("\nWord: " + game.display_word())
        print("Guessed Letters: " + ", ".join(game.guessed_letters))
        print("Guesses Remaining: " + str(game.guesses_remaining))
        guess = input("Enter a letter: ")

        result = game.make_guess(guess)
        print(result)

        if "_" not in game.display_word():
            print("Congratulations! You've won!")
            play_again = input("Play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
            else:
                game.initialize_game()

if __name__ == "__main__":
    main()
