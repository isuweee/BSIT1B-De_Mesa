number1 = eval(input("Enter your first number: "))
number2 = eval(input("Enter your second number: "))

add = number1 + number2
minus = number1 - number2
multiply = number1 * number2
division = number1 / number2

print("\nThe sum of", number1, "and", number2, "is", add)
print("The difference of", number1, "and",number2,"is", minus)
print("The product of", number1, "and",number2,"is", multiply)
print("The quotient of", number1, "and",number2,"is", division)
print(number1, "exponent by", number2, "is",number1**number2)
print("The remainder of", number1, "and",number2,"is", number1%number2)
print("The floor division of", number1, "and",number2,"is",number1//number2)
