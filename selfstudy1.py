print("Basic Information")

name = input("What is your name? ")

print("Got ya,", name)

print(" ")

age_input = input("How old are you? ")

try:
    age = int(age_input)
    if age >= 18:
        print("Ohh, you're an adult. ")
    elif age < 18:
        print("Ohh, you're a minor. ")
except ValueError:
    print("It must be confidential...")

print(" ")

sex = input("Are you a male or female? (M/F): ").strip().upper()

if sex in ["MALE", "M"]:
    print("You're a Male!")
elif sex in ["FEMALE", "F"]:
    print("You're a Female!")
else:
    print("You must be non-binary.")
    
print(" ")

address = input("Where do you live? ")

print("Okay, got it!")

print (" ")

while True:
    contact_input = input("Contact no: ")

    try:
        contact = int(contact_input)
        print("Okay, I wrote it!")
        break
    except ValueError:
        print("Please enter numbers.")
    
print(" ")

print("Here is your basic information:")

print("Name: ", name)
print("Age: ", age_input)
print("Sex: ", sex)
print("Address: ", address)
print("Contact: ", contact_input)

print(" ")

print("Thank you for answering!")
