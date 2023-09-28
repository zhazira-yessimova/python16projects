from random import randint
# user_name = input("Hello! What is your name? ")
#
# print(f"{user_name}, let's play a 'Guess the number' game! \nI will choose a number between 1 and 100 and you will have 8 attempts to guess it. \nLet's go!")
#
# attempts = 0
# number = randint(1, 101)
#
# while True:
#     guess = int(input('Your guess: '))
#     attempts += 1
#     if guess <= 1:
#         print('Oh-oh, your nuber is out of range')
#     elif guess >= 100:
#          print('Oh-oh, your number is out of range')
#     elif guess <= number:
#          print('Go higher!')
#     elif guess >= number:
#          print('Go lower!')
#     elif guess == number:
#          print(f'You guessed using {attempts} attempts!')
#     else:
#         print('You ran out of attempts :(')

guess = 0
secret_number = randint(1, 100)
estimation = 0
name = input("Hello! What is your name? ")

print(f"{name}, let's play a 'Guess the number' game! \nI will choose a number between 1 and 100 and you will have 8 attempts to guess it. \nLet's go!")

while guess < 8:
    estimation = int(input('Your guess: '))
    guess += 1

    if estimation < secret_number:
        print('Go higher!')
    elif estimation > secret_number:
        print('Go lower!')
    else:
        print(f'Congrats, {name}! You guessed using {guess} attempts!')
        break
if estimation != secret_number:
    print(f"Sorry, you ran out of attempts. the secret number was {secret_number}")

