#rock, paper, scissors

from random import choice

print("Welcome to Rock Paper Scissors Game")
player_choice = input("(Enter your choice): ").lower()
ai_choice = choice(["rock", "paper", "scissors"])
print("(AI choice): " + ai_choice)
print("Shoot!")

if player_choice == ai_choice:
    print("Draw")
elif player_choice == "scissors":
    if ai_choice == "paper":
        print("Player Wins")
    elif ai_choice == "rock":
        print("AI Wins")
elif player_choice == "rock":
    if ai_choice == "paper":
        print("AI Wins")
    elif ai_choice == "scissors":
        print("Player Wins")
elif player_choice == "paper":
    if ai_choice == "scissors":
        print("AI Wins")
    elif ai_choice == "rock":
        print("Player Wins")
else:
    print("Enter rock, paper or scissors")

# if player_choice == ai_choice:
#     print("Draw")
# elif player_choice == "scissors" and ai_choice == "paper":
#         print("Player Wins")
# elif player_choice == "paper" and ai_choice == "rock":
#         print("Player Wins")
# elif player_choice == "rock" and ai_choice == "scissors":
#         print("Player Wins")
# elif player_choice == "paper" and ai_choice == "scissors":
#         print("AI Wins")
# elif player_choice == "scissors" and ai_choice == "rock":
#         print("AI Wins")
# elif player_choice == "rock" and ai_choice == "paper":
#         print("AI Wins")
# else:
#     print("Enter rock, paper or scissors")