# String Formatting by De Mesa, Adrian 

fn = 'Adrian'
ln = 'De Mesa'
nn = 'Teki'

print(f"My whole name is {fn} {ln}, and my nickname is {nn}")

# String Formatting 'Factorial' version

num = int(input("Enter Number: "))
result = 1

for i in range(num, 0, -1):
    print(f"{result} × {i} = {result * i}")
    result *= i

print(f"Factorial of {num} is {result}")
