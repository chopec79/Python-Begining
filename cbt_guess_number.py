import random
guesses_made = 0
name = input('Hello! What is your name?')
number = random.randint(1,20)
print('Well I am thinking of a number between 1 and 20')

while guesses_made <6:
    guess =int(input('take a guess'))
    guesses_made += 1
    if guess < number:
        print('your numberis to low')
    if guess > number:
        print('your number is to high')
    if guess == number:
        print('you got it')
        break
print('All done')
        