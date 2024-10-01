from random import randint
rand_num = randint(1, 10)

guess = 0

while guess != rand_num:
    guess = int(input("Enter you guess: "))

    if guess < rand_num:
        print("You guess in Smaller than real")
    elif guess > rand_num:
        print("Your guess is Larger than real")
    else:
        print("You hit the Jackpot!!!")