# coding: utf-8
# Author: Mingjun Lei

age_of_oldboy = 56
for i in range(5):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("Yes! You got it!")
        break
    elif guess_age < age_of_oldboy:
        print("Try a bigger number.")
    else:
        print("Try a smaller number.")
else:
    print("You have tried too many times...fuck off!")
