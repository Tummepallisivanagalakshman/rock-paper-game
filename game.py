import random

while True:
    user_select = int(input("enter 0 for rock, 1 for paper, 2 for scissor: "))

    if user_select > 2 or user_select < 0:
        print("invalid input 😡")
    else:
        print("user_select: ", user_select)
        computer_select = random.randint(0, 2)
        print("computer_select: ", computer_select)

        if user_select == computer_select:
            print("draw🪢")
        elif (user_select == 0 and computer_select == 2) or \
             (user_select == 1 and computer_select == 0) or \
             (user_select == 2 and computer_select == 1):
            print("user win🏆")
        else:
            print("you lose🪦")