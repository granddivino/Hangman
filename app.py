import random

# Random words = ''
word_bank = ['hoebag', 'bitches', 'tramp', 'skank', 'twat', 'fugly']

# Get the random word
def get_random_word():
    return random.choice(word_bank).upper()
    

class Word():
    def __init__(self, chosen_word=None):
        self.chosen_word = get_random_word()
        pass # This method splits the word up into a list of dictionaries with 2 attributes:
        pass # The letter/character, and a boolean representing whether or not it has been guessed
    
    def split_string(self):
        word_to_list = list(self.chosen_word)
        print(word_to_list)

    def print_word(self):
        print('Hit print word', self.chosen_word)

    def check_letter(self):
        print('Hit check letter')

answer = Word()
# Test random word gets selected and split into list
answer.print_word()
answer.split_string()


def decrease_round():
    print('starting round', game['guesses_left'])
    game['guesses_left'] -= 1
    print('rounds left,', game['guesses_left'])


def logic():
    pass 
    if game['guesses_left'] > 0:
        guess = input('Guess a letter ').upper()
        # Check whether guessed letter is in word
        print(guess)
        win_scenario()
    else:
        print('You suck, out of guesses!')


def win_scenario():
    if game['current_word'] == answer.chosen_word:
        print('You win then I guess')


# Game object
game = {
    'current_word': ' _ ' * len(answer.chosen_word),
    'guessed_letters': [],
    'guesses_left': 8
}


logic()