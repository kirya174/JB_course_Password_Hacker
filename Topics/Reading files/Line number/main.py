# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
lines = 0
for _ in file:
    lines += 1
print(lines)
file.close()
