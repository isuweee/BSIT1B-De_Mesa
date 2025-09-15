# The Factorial Program by De Mesa, Adrian :)

result = 1
num = eval(input("Enter the number you'll factor: "))

for factor in range(1, num + 1):
    result *= factor

print("The factorial of", num, "is", result)
