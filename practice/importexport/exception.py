try:
    int('a')
except ValueError as e:
    print("oops, can't do that", e)

print('This is the end of the program')