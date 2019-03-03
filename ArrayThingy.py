from spellchecker import SpellChecker

fr = open('test.txt')
text = fr.read()
fr.close
Array = text.split(" ")

spell = SpellChecker()

#spell.word_frequency.load_words(['hello', 'I', 'am', 'a', 'pottaot'])
#spell.known(['hello', 'I', 'am'])
#misspelled = spell.unknown(['a', 'pottaot'])
change = []

for word in Array:
    #print(spell.correction(word))
    #print(spell.candidates(word))
    change.append(spell.correction(word))
#for word in change:
    #print(word)
separator = " "
print(separator.join(change))

fw = open('fixedtest.txt','w')
fw.write(separator.join(change))
fw.close