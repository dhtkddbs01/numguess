from random import randint

# create answer range
answer = randint(1,100)
print(answer)

# get user's name, guess

user_name = input('hello, there! what is your name?'
guess = input(f'hi. {user_name}. guess the number(1-100): ')

# print to check
print(user_name, guess)

# check and print correct or not
if guess==answer:
    print('congrats!')
else:
    print(f"you are wrong! the answer was {answer}.")

