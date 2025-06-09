import random
mode = input("Choose mode: AI, or VS ")
options = ["Coop", "Def"]
Op_choice = ""
your_socre = 0
Op_score = 0

if mode == "AI" or mode == "ai" or mode == "Ai":
    pass
elif mode == "VS" or mode == "Vs" or mode == "vs":
    rounds = int(input("how many rounds? "))
    AI = input("Choose algorithem: tit for tat (1), random (2) ")
    if AI == "2":
        for i in range(0, rounds):
            Op_choice = random.choice(options)
            your_choice = input("choose C or D. case sensative, MAKE LOWERCASE (sorry to lazy to fix ¯\_( ͡° ͜ʖ ͡°)_/¯) ")
            if your_choice == "c" and Op_choice == "Coop":
                your_socre = your_socre + 3
                Op_score = Op_score + 3
                print("Both Cooperated. Your Score: " + str(your_socre) + " Op score: " + str(Op_score))
            elif your_choice == "d" and Op_choice == "Coop":
                your_socre = your_socre + 5
                Op_score = Op_score
                print("Secessful Deflect. Your Score: " + str(your_socre) + " Op score " + str(Op_score))
            elif your_choice == "d" and Op_choice == "Def":
                your_socre = your_socre + 1
                Op_score = Op_score + 1
                print("Unsecessful Deflect. Your Score: " + str(your_socre) + " Op score " + str(Op_score))
            elif your_choice == "c" and Op_choice == "Def":
                your_socre = your_socre
                Op_score = Op_score + 5
                print("You were Deflected. Your Score: " + str(your_socre) + " Op score " + str(Op_score))
            if your_socre >= 20 or Op_score >= 20:
                print("Game Over")
                if your_socre > Op_score:
                    print("You Win!")
                elif your_socre < Op_score:
                    print("You Lose!")
                else:
                    print("Draw!")
                break
    elif AI == "1":
        pass
    else:
        print("not defined :(")
        for i in range(0, 100):
            print(">:(")