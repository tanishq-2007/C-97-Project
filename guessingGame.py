import random

number= random.randint(1,9)
chances=0
while chances <5:
    guess=int(input('enter your guess: '))
    if guess ==number:
        print('Congratulations you won')
        break
    elif guess<number:
        print('Your Guess was too low, Guess the number higher than',guess)
    else:
        print('Your guess was too high, Guess the number lower than',guess)
    chances += 1
if not chances <5:
    print('You lose!!! The number is',number)