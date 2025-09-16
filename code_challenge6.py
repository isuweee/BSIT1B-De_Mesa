# Odd Summation by De Mesa, Adrian :D

print("Enter 7 Numbers")

result = 0
for odd in range(7):
    num = eval(input("Enter Number: "))
    if num % 2 != 0:
        result += num

print("The sum of all odd numbers u input is:", result)
