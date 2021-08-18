import random

user_score = 0
computer_score = 0

while True:
    user_input = input("Type 'R' for Rock , 'P' for Paper , 'S' for Scissors or q to quit :\n").lower()
    if user_input == "q":
        break

    if user_input not in ['r' , 'p' , 's']:
        print ('Invalid letter . Try again ...')
        continue
        
    computer_pick = random.choice(['rock' , 'paper', 'scissors'])
    print("Computer picked : " + computer_pick)


    if user_input == "r" and computer_pick == "scissors":
        print("You won !")
        user_score += 1
        

    elif user_input == "p" and computer_pick == "rock":
        print("You won !")
        user_score += 1
        

    elif user_input == "s" and computer_pick == "paper":
        print("You won !")
        user_score += 1

    elif user_input == "r" and computer_pick == "rock":
        print("Draw !")
        user_score += 0
        

    elif user_input == "p" and computer_pick == "paper":
        print("Draw !")
        user_score += 0
        

    elif user_input == "s" and computer_pick == "scissors":
        print("Draw !")
        user_score += 0
        
    else:
        print("You lost !")
        computer_score += 1

print("Your Score : " + str(user_score))
print("Computer Score : " + str(computer_score))
print("Good Bye :-)")
