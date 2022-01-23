def guess(chosen_word, word_with_blanks, number_of_guesses, guessed_letter_list):
  guessed_letter = input('Guess a letter: ')
  if guessed_letter in guessed_letter_list:
    print('Letter already guessed, try again. \n')
    guessed_letter = ''
    return word_with_blanks, number_of_guesses, guessed_letter
  elif guessed_letter.isalpha() == False:
    print('This is not a letter, try again. \n')
    guessed_letter = ''
    return word_with_blanks, number_of_guesses, guessed_letter
  elif len(guessed_letter) != 1:
    print('Please print one letter at a time. \n')
    guessed_letter = ''
    return word_with_blanks, number_of_guesses, guessed_letter
  else:
    guessed_letter = guessed_letter.lower()
    chosen_word = list(chosen_word)
    word_with_blanks = list(word_with_blanks)
    for i in range(0,len(chosen_word)):
      if guessed_letter == chosen_word[i]:
        word_with_blanks[i] = guessed_letter
    if guessed_letter in chosen_word:
      print('The letter is in the word.')
    if guessed_letter not in chosen_word:
      print('The letter is wrong, guess again.')
      number_of_guesses = number_of_guesses - 1
    print('You have ' + str(number_of_guesses) + ' guesses left. \n')
    return word_with_blanks, number_of_guesses, guessed_letter
    