# While Loop by De Mesa, Adrian ^^

food = True

while food == True:
    cook = input("Is the food cooked? (yes/no): ").lower()
    if cook == 'no':
        print("Cooking for 15 minutes....")
        continue
    else:
        print("Your food is cooked 100%🔥")
        break
