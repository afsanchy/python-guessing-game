import random

number = random.randint(1, 10)

for i in range(3): #user gets 3 trials
    guess = int(input("guess the number (1-10): "))
    if guess == number:
        print("Corect!")
        break
    else:
        if guess<number:
            print("Number is higher, try again")
        else: print("Number is Lower, try again")

