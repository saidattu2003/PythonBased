import random

user_wins=0;
computer_wins=0;

while True:
    user_input=input("Type Rock(R) / Paper(P) / Scissor(S)  or q (QUIT)").lower()
    if user_input=="q":
        quit()
    if user_input not in ["rock","r","scissors","s","paper","p"]:
        print("pls type correctly")

    






