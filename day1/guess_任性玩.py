# coding: utf-8
# Author: Mingjun Lei

age_of_oldboy = 56
count = 0
while count < 5:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("Yes! You got it!")
        break
    elif guess_age < age_of_oldboy:
        print("Try a bigger number.")
    else:
        print("Try a smaller number.")
    count += 1
    if count == 5:
        continue_confirm = input("Do you want to keep guessing? y/n........")
        if continue_confirm != "n":
            count = 0

