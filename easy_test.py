# Easy Test by De Mesa, Adrian

print("Problem 1:\n")
for i in range(1,6,1):
    for x in range(6,i,-1):
        print(" ",end='')
    for y in range(1,2*i,1):
        print("*",end='')
    print()

print("\nProblem 2:\n")
for i in range(1,6,1):
    for x in range(1,i+1,1):
        print(i,end='')
    print()
