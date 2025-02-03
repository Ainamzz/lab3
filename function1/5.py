import itertools
def permutations():
    str = input("Write a string:")
    p = [''.join(perm) for perm in itertools.permutations(str)]
    print(p)
permutations()