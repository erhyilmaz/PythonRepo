import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

while True:
    print("----"*6)
    # Write your code below this line 👇
    my_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors\n"))
    comp_choice = random.randint(0, 2)

    if my_choice == 0:  # rock
        print("My choice is Rock")
        print(rock)
        # print(game_images[my_choice])

        if comp_choice == 0:  # rock
            print("Comp choice is Rock")
            print(rock)
            print("Draw!")
        elif comp_choice == 1:  # Paper
            print("Comp choice is Paper")
            print(paper)
            print("Comp. wins!")
        elif comp_choice == 2:  # Scissors
            print("Comp choice is Scissors")
            print(scissors)
            print("I win!")
    elif my_choice == 1:  # Paper
        print("My choice is Paper")
        print(paper)
        if comp_choice == 0:  # rock
            print("Comp choice is Rock")
            print(rock)
            print("I win!")
        elif comp_choice == 1:  # Paper
            print("Comp choice is Paper")
            print(paper)
            print("Draw!")
        elif comp_choice == 2:  # Scissors
            print("Comp choice is Scissors")
            print(scissors)
            print("Comp. wins!")

    elif my_choice == 2:  # Scissors
        print("My choice is Scissors")
        print(scissors)
        if comp_choice == 0:  # rock
            print("Comp choice is Rock")
            print(rock)
            print("Comp wins!")
        elif comp_choice == 1:  # Paper
            print("Comp choice is Paper")
            print(paper)
            print("I win!")
        elif comp_choice == 2:  # Scissors
            print("Comp choice is Scissors")
            print(scissors)
            print("Draw!")
    else:
        print("Wrong input!")
        break
