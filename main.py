def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


count = int(input("How many numbers do you want? "))

for i in range(count):
    print(fibonacci(i))