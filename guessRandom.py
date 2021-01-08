import random

name=input('Enter your name:')
randomnumber=random.randint(1,20)
print(randomnumber)

for noguess in range(1,5):
    guessnumber=int(input('Guess the number:'))
    if guessnumber > randomnumber:
        print('your guess is too high')

    elif guessnumber < randomnumber:
        print('guess no is too low')

    else:
        break

if guessnumber == randomnumber:
    print('good job '+str(name)+' you guess the number in '+str(noguess)+' guesses')
else:
    print('you could not guess correctly , correct number is '+str(randomnumber))
