import random
import time
print("Welcome to the guessing game.\n You have 5 attempts to guess the number between 1 and 100.\n GOOD LUCK")

def Game():
    num= random.randint(1,100)
    #print(num)
    
    for i in range(1,5):
        a = i
        guess= int(input(f"Enter guess #{a}: "))

        if guess < num:
            print("go higher")
        elif guess > num:
            print("Go lower")
        else:
            print("You have guessed correctly")
            break
    guess2= int(input("Enter guess #5: "))

    if guess2 == num:
        print("You're in luck. Have guessed it correctly on your last try!")
    else:
        print(f"You're all out of guesses! The number was{num}")

Game()

while True:
    choice=input("Would you like to try again?(y/n): ")
    x=choice.lower()
    if x == "y":
        Game()
    if x== "n":
        print("Exiting game...")
        time.sleep(2)
        print("exited. GOODBYE")
        break
    else:
        print("enter valid option!!!!")
