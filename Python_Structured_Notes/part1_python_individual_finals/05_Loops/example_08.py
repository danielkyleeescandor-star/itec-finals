secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess (1-10): "))
    if guess != secret:
        print("Try again!")
print("Correct!")
