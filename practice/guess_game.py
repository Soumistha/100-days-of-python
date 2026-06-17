# number guessing game
import random as r

print("Welcome to the guessing game")
print("I am thinking of a number b/w 1 and 100")
diff = input("choose ur difficulty level:(easy or hard) ")

number = r.randint(1,101)
print(number)
attempts = 10 if diff == "easy" else 5

for i in range(attempts):
    guess = int(input("What is your guess: "))
    
    if guess == number:
        print("Congrats, it's correct!")
        break
    elif guess > number:
        print("Too high, try again.")
    else:
        print("Too low, try again.")
else:
    # this runs only if the loop wasn't broken
    print(f"Sorry, better luck next time. The number was {number}")