d = eval(input("Enter the amount of deposit: "))

a1 = d // 1000
d = d % 1000
a2 = d // 500
d = d % 500
a3 = d // 200
d = d % 200
a4 = d // 100
d = d % 100
a5 = d // 50
d = d % 50
a6 = d // 20
d = d % 20
a7 = d // 10
d = d % 10
a8 = d // 5
d = d % 5
a9 = d // 1
d = d % 1

print(a1, "- 1000")
print(a2, "- 500")
print(a3, "- 200")
print(a4, "- 100")
print(a5, "- 50")
print(a6, "- 20")
print(a7, "- 10")
print(a8, "- 5")
print(a9, "- 1")
