user=input("Welcome to the quiz, please enter your name.     ")
take=True

while take:
        answer=input("Are you prepared to start? Y/N   ")
        if answer == "Y":
                print("Then we shall begin")
                
        else:
                print("Come back when you are ready.")

        answer1=input("What is the capital of France?   ")
        if answer1 == "Paris":
                print("Correct +2 points")
        else:
                print("Inccorect, no points scored this question")

        answer2=input("What is the sum of 5674+9880?   ")
        if answer2 == "15554":
                print("Correct +4 points")
        else:
                print("Incorrect, no points scored this question")

        answer3=input("What is 5674-9880?    ")
        if answer3 == "-4206":
                print("Correct +3 points")
        else:
                print("Incorrect, no points scored this question")

        answer4=input("What is 5674x9880?    ")
        if answer4 == 5674*9880:
                print("Correct +3 points")
        else:
                print("Incorrect, no points scored this question")

        answer5=input("What is 5680 divided by 8?    ")
        if answer5 == 5680/8:
                print("Correct +2 points")
        else:
                print("Incorrect, no points scored this question")

        answer6=input("What is the remainder of 5679 divided by 9?   ")
        if answer6 == "0":
                print("Correct +3 points")
        else:
                print("Icorrect, no points were scored this question.")

        answer7=input("What is the answer to life, the universe and everything?   ")
        if answer7 == "42":
                print("Correct +5 points")
        else:
                print("Incorrect, you have scored no points this question")
        total=input("What is your total score?    ")
        if total >= "15":
                print("Congratulations", user, "You have passed the test")
        else:
                print("I'm not angry, just disappointed in your failiure", user)
        responce=input("Do you wish to try again?   Y?N     ")
        if responce == "Y":
                print("Please wait")
        elif responce =="Y":
                take=True
        else:
             print("You're no fun", user)
             take=False

