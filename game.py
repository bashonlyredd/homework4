import random

while True:
    result = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"), ("rock", "lizard"), ("lizard", "spock"),
              ("spock", "scissors"), ("scissors", "lizard"), ("lizard", "paper"), ("paper", "spock"), ("spock", "rock")]
    move = [res[1] for res in result]
    human_score, machine_score = (0, 0)
    human = input("Your choice rock,paper,scissors,lizard,spock ? : ")
    machine = random.choice(move)
    print("Your choice {}".format(human))
    print("Machine choice {}".format(machine))
    if human == machine:
        print("Draw")
    elif (human, machine) in result:
        print("Human WIN !")
        human_score += 1
    elif (machine, human) in result:
        print("Machine WIN :P")
        machine_score += 1
    else:
        print("You entered the wrong value, please select from this list: (rock,paper,scissors,lizard,spock) ")
        human = input("Your choice rock,paper,scissors,lizard,spock ? : ")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break






