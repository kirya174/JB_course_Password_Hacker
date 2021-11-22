str_a = input()
str_b = input()
word = ''
for let_a, let_b in zip(str_a, str_b):
    word += let_a + let_b
print(word)