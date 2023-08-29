import random

while True:
    player_one_choice = input("Rock, Paper, Scissors: ")
    
    choices=["Rock","Paper","Scissors"]
    
    x=random.choice(choices)
    print("Computer chose: "+ x)

    if player_one_choice == x:
        print("Tie!")
    elif player_one_choice == "Rock" and x == "Scissors":
        print("You Win!")
        break
    elif player_one_choice == "Rock" and x == "Paper":
        print("Computer Wins!")
        break
    elif player_one_choice == "Paper" and x == "Rock":
        print("You Win!")
        break
    elif player_one_choice == "Paper" and x == "Scissors":
        print("Computer Wins!")
        break
    elif player_one_choice == "Scissors" and x == "Paper":
        print("You Win!")
        break
    elif player_one_choice == "Scissors" and x == "Rock":
        print("Computer Wins!")
        break
    else:
        print("Choose Rock, Paper, or Scissors!")

print("End of Game!")