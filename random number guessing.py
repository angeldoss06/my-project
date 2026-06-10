import random
print("welcome to the number guessing game!!!")
low=int(input("enter lower bound:"))
high=int(input("enter upper bound:"))
num=random.randint(low,high)
print("you have 7 chances to guess the number between",low, "to" ,high)
ch=7
gc=0
while gc<ch:
    gc+=1
    guess=int(input("enter the guessed number:"))
    if guess==num:
        print("you guessed the number correctly at",gc,"chances")
        break
    elif gc>=ch and guess!=num:
        print("sorry..better luck next time")
    elif guess>num:
        print("its too high")
    else:
        print("too low ")
