from spellchecker import SpellChecker

spell = SpellChecker()

while True:
    word = input('Enter the word: ')
    word = word.lower()

    if word in spell:
        print(f'{word} is spelled correctly!')
    else:
        correct_words = spell.correction(word)
        print(f'The best suggestion for {word} is {correct_words}')