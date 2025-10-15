# import random by De Mesa, Adrian
print("==YES, NO, MAYBE REPLIER RANDOMIZER (FOR FUN USE ONLY)==\nNote: Only ask questions answerable by yes, no or maybe!\n")

import random
num = random.randint(1,3)

question = input("Enter your question: ")

if num == 1:
    print(f"\nThe answer for the question '{question}' is Yes!")
elif num == 2:
    print(f"\nThe answer for the question '{question}' is No!")
else:
    print(f"\nThe answer for the question '{question}' is Maybe!")

# I did it differently from the 'Guess The Number Game' to test my other options 
# But I kept the main idea of the lesson here :)
