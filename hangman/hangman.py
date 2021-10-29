import game_data as game
import random
import pickle

# Player get to guess a word

# When the game starts, it asks he user to enter his name

def random_word():
    """ Choose a random word from the word list"""
    return game.word_lists[random.randrange(len(game.word_lists))]