def factorial(n):
    n = abs(n)
    total = 1
    for i in range(2, n+1):
        total *= i
    return total

print(factorial(7))
