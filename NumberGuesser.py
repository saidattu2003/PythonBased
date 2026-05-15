import random
top_off=input("Type the top number : ")
if top_off.isdigit():
    top_off=int(top_off)

    if top_off<=0:
        print("pls enter more than 0")
        quit()
else:
    print("pls enter a number")
    quit()

r=random.randrange(top_off+1)
nguess=0
while(1):
    guess=int(input("Enter your Guess :"))
    nguess+=1
    if(guess>r):
        print("Your guess is greater")
    elif(guess<r):
        print("your guess is smaller")
    else:
        print("You Guessed it right !!")
        print("Total Guesses : " + str(nguess))
        break
