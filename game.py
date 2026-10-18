import random
secret = random.randint(1,100)
attempts = 0
while True:
    try:
        guess = int(input("Guess the number (1-100): "))
    except ValueError:
        print("Please enter a number")
        continue
    attempts +=1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You got it in {attempts} tries.")
        break