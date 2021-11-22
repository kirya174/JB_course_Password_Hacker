# write your code here
with open('salary.txt', 'r') as in_file, \
        open('salary_year.txt', 'w') as out_file:
    for line in in_file:
        out_file.write(str(int(line.strip()) * 12) + '\n')
