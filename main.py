"""
Name(s): Manas Chan
Name of Project: Hangman
"""


import list_of_words
import guess
import random
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

playing = True

while playing == True:
  random_word = random.choice(list_of_words.list_of_words)
  word_with_blanks = ''
  guessed_letter_list = []
  for i in range(0, len(random_word)):
    word_with_blanks += '_'
  number_of_guesses = 15
  print(word_with_blanks)

  while '_' in word_with_blanks and number_of_guesses > 0:
    word_with_blanks, number_of_guesses, guessed_letter =  guess.guess(random_word, word_with_blanks,number_of_guesses, guessed_letter_list)
    guessed_letter_list.append(guessed_letter)
    print(''.join(word_with_blanks))
    print('The letters you have guessed are ' + '(' + ','.join(guessed_letter_list) + ')')

  if number_of_guesses == 0:
    print('The word was ' + random_word + '.')
    print('Game over.')

  if '_' not in word_with_blanks:
    print('Congrats, you win!')

  play_again = input('Would you like to play again? Type 1 for Yes, and 2 for No: ')
  if play_again != '1' and play_again != '2':
    print('Please type in 1 or 2.')
    play_again = input('Would you like to play again? Type 1 for Yes, and 2 for No: ')
  elif play_again == '1':
    playing = True
  elif play_again == '2':
    playing = False
  