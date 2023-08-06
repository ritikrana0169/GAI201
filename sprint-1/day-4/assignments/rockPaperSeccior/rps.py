import random


def userChoiceFun():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def checkWinner(userChoice,computerChoice):
    if userChoice == computerChoice:
        return "draw"
    elif (userChoice == "rock" and computerChoice == "scissors") or \
         (userChoice == "scissors" and computerChoice == "paper") or \
         (userChoice == "paper" and computerChoice == "rock"):
        return "user"
    else:
        return "computer"
     
def main():
    user_score=0
    computer_score=0
    draw=0

    print("Welcome To Rock Paper Scissors Game")

    while True:
        userChoice=userChoiceFun()
        computerChoice=random.choice(["rock", "paper", "scissors"])

        print(f"Your Choice Is {userChoice},Computer chose {computerChoice}")

        result=checkWinner(userChoice,computerChoice)

        if result=="user":
            user_score+=1
            print("You Win this Round")
        elif result=="computer":
            computer_score+=1
            print("Computer wins this round!")
        else:
            draw+=1
            print("Game Draw")

        print(f"Score: User {user_score} - Computer {computer_score} - Draws {draw}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
        



main()