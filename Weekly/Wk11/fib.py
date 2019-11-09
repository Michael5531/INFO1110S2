def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
while True:
    a = input("Number you want to calculate the fibonacci value: ")
    print(fibonacci(a))
    if a == "stop":
        break