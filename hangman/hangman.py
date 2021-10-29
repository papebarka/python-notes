import game_data as game
import random
import pickle

total_score = 0
player_name = ''

def player_information():
    name = input("What is our name?: ")
    with open(game.score_file, 'wb') as scores:
        pass

def random_word():
    """ Choose a random word from the word list"""
    return game.word_lists[random.randrange(len(game.word_lists))]