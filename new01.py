def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
print("Bye")

