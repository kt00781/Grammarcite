from spellchecker import SpellChecker

#input("Hello, How was your day?")
#print("No one cares.")
file_r = input("Input name of txt file: ")

fr = open('{}.txt'.format(file_r))
text = fr.read()
fr.close
Array = text.splitlines()
spell = SpellChecker()
change = []
changeline = []
separator1 = " "
separator2 = '\n'

for line in Array:
    Array2 = line.split()
    for word in Array2:
        change.append(spell.correction(word))
    changeline.append(separator1.join(change))
    change.clear()
print(separator2.join(changeline))

file_w = input("Input name of new file: ")

fw = open('{}.txt'.format(file_w),'w')
fw.write(separator2.join(changeline))
fw.close