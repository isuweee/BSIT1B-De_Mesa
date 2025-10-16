# Medium Test by De Mesa, Adrian

num = int(input("Enter a number: "))

for i in range(1, 11):
    for x in range(1, num + 1):
        print(f"{i} x {x} = {i * x}\t", end='')
    print()
