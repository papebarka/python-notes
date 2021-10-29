### Hangman

1. The computer randomly choses a word of maximum 8 characters from a list.

2. Player attempts to find the characters that make the word one step at the time.
- If the character is in the word, the computer displays the word with the character.
- The characters who are yet to be correctly guessed are replaced with a star (*)
- The player has at most 8 attempts after which he'll lose.
3. If the player hasn't played yet, his starting score is 0.
4. After each game, his remaining number of attempts, which is considered as his score, will be added to his saved score to make his total score since he started the game.

The scores will be saved in file nammed 'scores'. Score will be saved as: PLAYER_NAME: PLAYER_SCORE.

If the file doesn't exist, we create an empty file with empty score dictionary.

If the file exists and the player is not in the dictionary then he is added with a score of 0. 

When the game starts, it asks he user to enter his name