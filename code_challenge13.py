# Odd Number Summation While Loop by De Mesa, Adrian ^^

print(f"========================\n  ODD NUMBER SUMMATION\n========================\n")

name = input("Enter your name: ")
odd = 0
num_name = ""

while True:
    num = eval(input("Enter a random number: "))
    if num == 0:
        print(f"Program STOPS!\nHello {name}, the total of ODD is: {odd}\nThe ODD components are: {num_name}")
        break
    elif num % 2 == 1:
        print("This is an ODD number!")
        odd += num
        num_name += str(num) + " "
        continue
    elif num % 2 == 0:
        print("This is an EVEN number!")
        continue
