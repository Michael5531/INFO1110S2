def spam(n):
    if n == 0:
        return n
    return spam(n - 1)
ham = spam(3)
print(ham)