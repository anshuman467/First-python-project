def menu():
    name = input("enter your name : ")
    print("                                                                                                                 ")
    print(            'HELLO',name                                                                                           )
    print("                 THIS IS MY APLICATION :)                                                                        ")
    print("                            YOU CAN PLAY SONME GAMES AND GENERATE SOME RANDOM PASSWORDS                          ")
    print("                                                                                                                 ")
    print("                              |------------------------------------|                                             ")
    print("                              |                                    |                                             ")
    print("                              |    1. PASSWORD GENERATOR           |                                             ")
    print("                              |    2. COMPUTER QUIZ                |                                             ")
    print("                              |    3. THE ADVENTURE GAME           |                                             ")
    print("                              |    4. ROCK , PAPER AND SCISSORS    |                                             ")
    print("                              |                                    |                                             ")
    print("                              |------------------------------------|                                             ")
    print("                                                                                                                 ")
    print("                                                                                                                 ")                            
    lst = int(input("enter no. according to index : \nor pess 0 for exit : "))
    

    if lst == 1 :
        def password():
            print ("Hi",name)
            ans=input("Do you want to generate password for your device (yes/no) : ")
            while 0<1 :
                if ans == 'yes':
                    import random

                    lower = "abcdefghijklmnopqrstuvwxyz"
                    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    numbers = "1234567890"
                    symbols = "!@#$%^&*()_-:;,.?"

                    string= lower + upper + numbers + symbols
                    length = 9
                    password = "".join(random.sample(string,length))
                    print ("the password is  : ",password)

                    option = input("Press y to go main menu\nPress n for generrate password again (y/n) : ")
                    if option == 'y':
                        menu()
                        break
                elif ans == 'no' :
                    print("GoodBye")
                    menu()
                    break
                else:
                    print("wrong input")
                    break
        password()     




    elif lst == 2 :
        print("Welcome to my computer quiz!")

        playing = input("Do you want to play? (y/n) ")
        while 0<1 :
            if playing == 'y':
            
                print("Okay! Let's play :)")
                score = 0

                print(" Q1. What does CPU stand for? ")
                answer = input(" = ")
                if answer == "central processing unit":
                    print('Correct!')
                    score += 1
                else:
                    print("Incorrect!")


                print(" Q2. What does GPU stand for? ")
                answer = input(" = ")
                if answer == "graphics processing unit":
                    print('Correct!')
                    score += 1
                else:
                    print("Incorrect!")


                print(" Q3. What does RAM stand for? ")
                answer = input(" = ")
                if answer == "random access memory":
                    print('Correct!')
                    score += 1
                else:
                    print("Incorrect!")


                print(" Q4. What does PSU stand for? ")
                answer = input(" = ")
                if answer == "power supply unit":
                    print('Correct!')
                    score += 1
                else:
                    print("Incorrect!")

                print("You got " + str(score) + " questions correct!")
                print("You got " + str((score / 4) * 100) + "%. ")


                playing = input("Do you want to play again ? ")

            elif playing == 'n' :
                print("GoodBye")
                break
          




    elif lst == 3 :
        print("Welcome", name, "to this adventure!")

        answer = input(
            "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")

        if answer == "left":
            answer = input(
                "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

            if answer == "swim":
                print("You swam acrross and were eaten by an alligator.")
            elif answer == "walk":
                print("You walked for many miles, ran out of water and you lost the game.")
            else:
                print('Not a valid option. You lose.')

        elif answer == "right":
            answer = input(
                "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

            if answer == "back":
                print("You go back and lose.")
            elif answer == "cross":
                answer = input(
                    "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

                if answer == "yes":
                    print("You talk to the stanger and they give you gold. You WIN!")
                elif answer == "no":
                    print("You ignore the stranger and they are offended and you lose.")
                else:
                    print('Not a valid option. You lose.')
            else:
                print('Not a valid option. You lose.')

        else:
            print('Not a valid option. You lose.')

        print("Thank you for trying", name)




    elif lst == 4 :
        
        import random

        user_wins = 0
        computer_wins = 0

        options = ["rock", "paper", "scissors"]
        optionss = ['r','p','s']

        print("welcome",name,"\nChoose among and play the rock ,paper,scissors game. ")

        while True:
            user_input = input("Type r (Rock)/p (Paper)/s (Scissors) or Q to quit: ")
            if user_input == "q" or user_input == "Q":
                break

            if user_input not in optionss:
                continue

            random_number = random.randint(0, 2)
            # rock: 0, paper: 1, scissors: 2
            computer_pick = options[random_number]
            print("Computer picked", computer_pick + ".")

            if user_input == "r" and computer_pick == "scissors":
                print("You won!")
                user_wins += 1

            elif user_input == "p" and computer_pick == "rock":
                print("You won!")
                user_wins += 1

            elif user_input == "s" and computer_pick == "paper":
                print("You won!")
                user_wins += 1

            elif user_input == "r" and computer_pick == "rock" or user_input == "p" and computer_pick == "p" or user_input == "sa" and computer_pick == "scissors" :
                print("Both take rock/paper/scissors \nNo scorce")
                

            else:
                print("You lost!")
                computer_wins += 1

        print("You won", user_wins, "times.")
        print("The computer won", computer_wins, "times.")
        print("Goodbye!")


    elif lst == 0:
        print("BYE thanks for using")
        exit

    
menu()
