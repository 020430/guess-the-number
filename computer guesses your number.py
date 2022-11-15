import random #allows a random number to be selected

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_num: 
            #if the persons guess is too low then print something
            print('Your guess is too low, try again.')
        elif guess > random_num: 
            # else if the guess is too high then print something
            print('Your guess is too high, try again.')
    #here if the number is right then the code breaks out the loop
    print(f'You got the number {random_num} !')

#guess(10)

def compGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'computer guessed the number {guess} correct! ')


compGuess(10)
