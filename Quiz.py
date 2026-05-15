# A very Basic Quiz Game
print("Welcome to the Quiz")

play_status=input("Do you want to Play ! yes/no : ")
score,total=0,0
if play_status.lower()!='yes':
    print("Bye  :(")
    quit()
else:
    answer = input("What is the Capital of India? ").lower()
    if answer == 'new delhi':
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    total+=1

    answer = input("Who is known as the Father of the Nation in India? ").lower()
    if answer == 'mahatma gandhi':
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    total+=1

    answer = input("Which planet is known as the Red Planet? ").lower()
    if answer == 'mars':
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    total+=1

    answer = input("What is the largest ocean in the world? ").lower()
    if answer == 'pacific ocean':
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    total+=1

    answer = input("Which programming language is known for AI and Machine Learning? ").lower()
    if answer == 'python':
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    total+=1

print("Your Score is "+ str((score/total)*100)+ " %")
        

