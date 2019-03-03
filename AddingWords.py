from spellchecker import SpellChecker
spell = SpellChecker()
print("To exit, hit return without input!")
while True:
    word = input("Input the word that you would like to add to the system: ")
    if word == '':
        break
    word = word.lower()
    if word in spell:
        print ("Word ({}) already in Dictionary!".format(word))
    else:
        print ("Word ({}) is not currently in the Dictionary, would you like to add it?".format(word))
        new_word = input("Input y if you would like to add this word other wise click return: ")
        if word == '':
            break
        new_word = new_word.lower()
        if new_word == 'y':
            spell.word_frequency.add('{}'.format(word))
        else:
            print("Invalid input please click return to exit and rerun the program!")
            break