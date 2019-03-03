from spellchecker import SpellChecker

spell = SpellChecker()
spell.word_frequency.load_text_file('./test.txt')

spell.word_frequency.load_words(['hello', 'I', 'am', 'a', 'pottaot'])
spell.known(['hello', 'I', 'am'])
misspelled = spell.unknown(['a', 'pottaot'])

for word in misspelled:
    print(spell.correction(word))
    print(spell.candidates(word))
