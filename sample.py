from spellchecker import SpellChecker
spell = SpellChecker()
print("To exit, hit return without input!")
while True:
    word = input('Input a word to spell check: ')
    if word == '':
        break
    word = word.lower()
    if word in spell:
        print("'{}' is spelled correctly!".format(word))
    else:
        cor = spell.correction(word)
        print("The best spelling for '{}' is '{}'".format(word, cor))

        print("If that is not enough; here are all the possible corrections")
        print(spell.candidates(word))