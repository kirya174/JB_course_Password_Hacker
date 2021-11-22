# read animals.txt
# and write animals_new.txt
file = open('animals.txt', 'r', encoding='utf-8')
newline = ''
for line in file:
    newline += line.strip() + ' '
file.close()
file = open('animals_new.txt', 'w', encoding='utf-8')
file.write(newline)
file.close()