text = input()
key = int(input()).to_bytes(2, byteorder='little')
print(''.join([chr(ord(char) + sum(key)) for char in text]))
