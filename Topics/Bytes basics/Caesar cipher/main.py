a = input()
output = ''.join(chr(ord(char) + 1) for char in a)
print(output)
