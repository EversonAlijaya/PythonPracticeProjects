

import random

secret = random.randint(1, 100)

attempts = 0

while True:

    guess = int(input("Guess (1-100): "))

    attempts += 1

    if guess < secret:

        print("Higher!")

    elif guess > secret:

        print("Lower!")

    else:

        print(f"Got it in {attempts} attempts!")
        break


