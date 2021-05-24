import random, sys
tools = ['r', 'p', 's']

print("_______________________________")

max_score = int(input("Set max score: "))
max_score -= 1

print("""    <----Instruction---->
       Rock    -> 'r'
       Paper   -> 'p'
       Scisors -> 's' """)
print("""        [ PC : You ]
    <------------------->""")


guest_score = 0
pc_score = 0



def game():
    global guest_score, pc_score
    while pc_score <= max_score and guest_score <= max_score:
        pc = str(random.choice(tools))
        print("_______________________________")
        guest = str(input("Your bet: "))

        if guest == pc:
            print("Draw !")

        elif guest == 'r' and pc == 'p':
            print("+1 for Computer")
            pc_score += 1

        elif guest == 'r' and pc == 's':
            print("+1 for You")
            guest_score += 1

        elif guest == 'p' and pc == 'r':
            print("+1 for You")
            guest_score += 1

        elif guest == 'p' and pc == 's':
            print("+1 for Computer")
            pc_score += 1

        elif guest == 's' and pc == 'r':
            print("+1 for Computer")
            pc_score += 1

        elif guest == 's' and pc == 'p':
            print("+1 for You")
            guest_score += 1
        print(pc)
        print(f"[ {pc_score} : {guest_score} ]")

    else:
        if guest_score > pc_score:
            print("You won.")
        else:
            print("Computer won.")
        again()


def again():
    global pc_score, guest_score, max_score
    print("_______________________________")
    answer = input("Again ? ( yes / no ) ")
    answer = answer.lower()
    if answer == 'yes':
        max_score = 0
        max_score = int(input("Set max score: "))
        max_score -= 1
        guest_score = 0
        pc_score = 0
        game()
    else:
        sys.exit()

while True:
    game()