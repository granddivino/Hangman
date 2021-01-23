import random


class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.chosen_word_info = []
        for letter in chosen_word:
            # Create dictionary to hold letters of chosen word and a status to indicate whether word has been guessed
            chosen_word_dictionary = {}
            chosen_word_dictionary['letter'] = letter
            chosen_word_dictionary['guessed'] = False
            self.chosen_word_info.append(chosen_word_dictionary)

    def get_chosen_word(self):
        return self.chosen_word_info



class Game():
    # Initialize the game         
    def __init__(self):
        self.rounds = 8
        self.word_bank = ['hoebag', 'bitches', 'tramp', 'skank', 'twat', 'fugly']
        self.word = ''
        self.word_info = []
        self.guess = ''
        self.guessed_letters = set()
        self.guessed_letter_count = 0
    # Get word to be guessed
    def get_random_word(self):
        # Get random word from with word_bank
        get_word = Word(random.choice(self.word_bank).upper())
        # Store word_info dictionary to use to evaluate guesses
        self.word_info = get_word.chosen_word_info
        # Store the string
        self.word = get_word.chosen_word
        # Start the game
        self.logic()
    

    
    # Check if letter is part of your guessed word
    # Shoe if guess is correct or wrong
    # Check if winning logic is met
    # Decrease round by one
    def logic(self):
        # Show the word up to this point at the start of this round
        self.word_at_start_of_round()
        # Prompt user to guess a letter
        self.guess = input(' Please guess a letter ').upper()
        print(self.guess)
        self.rounds -= 1
        print('Rounds remaining: ',self.rounds)
        self.print_word()

    # Show word at beginning of round, and populate any letters that have already been guessed
    def word_at_start_of_round(self):
        for item in self.word_info:
            if item['guessed'] == True:
                print(item['letter'], end='')
            else:
                print(' _ ',end='')

        print(' GUESSED LETTERS: ', self.guessed_letters)


    # Print updated word after your guess has been checked
    def print_word(self):
        for item in self.word_info:
            if self.guess == item['letter']:
                print(item['letter'], end='')
                item['guessed'] = True
                self.guessed_letter_count += 1
                
            elif item['guessed'] == True:
                print(item['letter'], end='')
            else:
                self.guessed_letters.add(self.guess)
                print(' _ ',end='')
        print(' # OF GUESSED LETTERS:', self.guessed_letter_count)
        # Win scenario
        self.win_scenario()


    # Win logic: when # of guessed letters equals length of word being guessed
    def win_scenario(self):
        if self.guessed_letter_count == len(self.word):
            print('You won the game, good for you.')
        elif self.rounds > 0:
            self.logic()
        else:
            print('You suck. The word was', self.word)


# Initialize the whole game    
game = Game()

# Get random word to start game
game.get_random_word()