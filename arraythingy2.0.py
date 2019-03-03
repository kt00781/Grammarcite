from spellchecker import SpellChecker

input("Hello, How was your day?")

print("No, One cares.")
file_r = input("Input name of txt file: ")

fr = open('{}.txt'.format(file_r))
text = fr.read()
fr.close
Array = text.split(" ")
spell = SpellChecker()
change = []

for word in Array:
    change.append(spell.correction(word))
separator = " "
print(separator.join(change))

file_w = input("Input name of new file: ")

fw = open('{}.txt'.format(file_w),'w')
fw.write(separator.join(change))
fw.close