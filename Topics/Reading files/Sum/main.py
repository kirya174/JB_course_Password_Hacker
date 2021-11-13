# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    nums = line.strip().split()
    print(int(nums[0]) + int(nums[1]))
file.close()