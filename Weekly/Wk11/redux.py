def redux(n):
    if n % 2 == 0:
        return n / 2
    if n % 2 != 0:
        return 3 * n + 1
print(redux(10))