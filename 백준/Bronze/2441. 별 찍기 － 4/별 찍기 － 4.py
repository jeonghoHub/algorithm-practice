n = int(input())

space = ''
for i in range(n, 0, -1):
    print(space + "*" * i)
    space += ' '