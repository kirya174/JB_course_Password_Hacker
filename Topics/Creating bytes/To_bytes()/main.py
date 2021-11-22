
a = (int(input())).to_bytes(2, byteorder='little')
print(sum(elem for elem in a))
