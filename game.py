import random
import time
num= random.randint(1,100)
print(num)

def Game():
    print("Welcome to the guessing game.\n You have 5 attempts to guess the number between 1 and 100.\n GOOD LUCK")
    for i in range(1,6):
        a = i
        guess= int(input(f"Enter guess #{a}: "))

        if guess < num:
            print("go higher")
        elif guess > num:
            print("Go lower")
        else:
            print("You have guessed correctly")
            exit

Game()

while True:
    choice=input("You're all out of guesses! Would you like to try again?(y/n): ")
    x=choice.islower
    if x == "y":
        Game()
    if x== "n":
        print("Exiting game...")
        time.sleep(2)
        print("exited. GOODBYE")
        break
    else:
        print("enter valid option!!!!")
