from spellchecker import SpellChecker

spell = SpellChecker()

misspelled = spell.unknown(['pythn', 'is', 'populr', 'languge'])

for word in misspelled:
    print(spell.correction(word))