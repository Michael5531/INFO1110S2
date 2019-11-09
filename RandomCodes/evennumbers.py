import sys
i = int(sys.argv[2])
if i == 0:
    while i <= (int(sys.argv[1]) * 2):
        if i == 0:
            i += 1
        if i % 2 == 0:
            print(i)
        i += 1
if i > 0:
    i = (int(sys.argv[2]) * 2) + 2
    while i <= (int(sys.argv[2]) * 2 + int(sys.argv[1]) * 2):
        if i % 2 == 0:
            print(i)
        i += 1
