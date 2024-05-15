import random
#choice number between 1 and 10
computer_number=random.randint(1,10)                               
print("Welcome to Number Guessing Game:")
user_input=int(input("Enter the Number in the Range of 100:"))
if computer_number > user_input:
    print("Computer number is :",computer_number)
    print("Please try again and enter high number")
elif computer_number < user_input:
    print("Computer number is :",computer_number)
    print("Please try again and enter low number")
else:
    print("Computer number is :",computer_number)
    print("Congratulation You Win")