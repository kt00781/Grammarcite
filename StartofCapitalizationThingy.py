'Capitalizes only the first letter but that is all I have got' 
file_r = input("Input name of txt file: ")

fr = open('{}.txt'.format(file_r))
text = fr.read()
fr.close
Caps = text.capitalize()

print(Caps)

file_w = input("Input name of new file: ")

fw = open('{}.txt'.format(file_w),'w')
fw.write(separator2.join(changeline))
fw.close
