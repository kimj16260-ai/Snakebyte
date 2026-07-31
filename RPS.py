import random
sPlay = "Y"
while sPlay == "Y":
    print("ROCK")
    print("PAPER")
    print("SCISSORS")
    sChoice = input("Shoot!-(R/P/S):").upper()
    iComputer = random.randint(1, 3)
    if iComputer == 1:
        sEnemy = "ROCK"
    elif iComputer == 2:
        sEnemy = "PAPER"
    else:
        sEnemy = "SCISSORS"
    if sChoice == sEnemy:
        print("It's a tie!")
    elif sChoice == "R" and sEnemy == "SCISSORS":
        print("You win!")
    elif sChoice == "P" and sEnemy == "ROCK":
        print("You win!")
    elif sChoice == "S" and sEnemy == "PAPER":
        print("You win!")
    else:
        print("You lose!")
    sPlay = input("Play again? (Y/N): ").upper()
