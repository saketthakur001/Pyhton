import random

while True:
    # taking input from user
    user_pass = input("Enter your password: ")

    # storing alphabet letter to use thm to crack password
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
                'w', 'x', 'y', 'z',]

    # initializing an empty string
    guess = ""

    attemt_no = 1
    # using while loop to generate many passwords untill one of
    # them does not matches user_pass
    while (guess != user_pass):
        guess = "" 
        # generating random passwords using for loop
        for letter in range(len(user_pass)):
            guess_letter = password[random.randint(0, 25)]
            guess = str(guess_letter) + str(guess)
            attemt_no += 1
    print(attemt_no)
        
        
    # printing the matched password
    print("Your password is",guess)
