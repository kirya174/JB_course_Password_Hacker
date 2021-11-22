import itertools
#
# first_names = list()
# middle_name = list()
for first, middle in itertools.product(first_names, middle_names):
    print(first, middle)
