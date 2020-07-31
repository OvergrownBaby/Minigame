score = 0


def gameinit():
    import time

    age_requirementint = 5

    print ("Welcome to my first IQ game!")

    time.sleep(2)

    name = input ("What is your name? ")

    time.sleep(1.5)

    print ("Hello " + name + "!")

    time.sleep(2)

    age = input ("How old are you? ")

    is_int = True
    try:
        # convert to integer
        int(age)
    except ValueError:
        is_int = False

    if is_int:

        if int(age)>=age_requirementint:

            time.sleep(3)

            print ("The age required to play this game is 5 years old.", end ="")

            time.sleep(2)

            print ("Since you are " + str(age) + " years old,", end = "")

            time.sleep(2)

            print ("you are old enough to play.")

            time.sleep(3)

            print ("This game consists of 5 IQ questions.")

            time.sleep(2.5)

            print ("To win, you have to answer at least 4 questions correctly.")

            time.sleep(2.5)

            print ("You will have 3 tries to each question.")

            time.sleep(3)

            def game():
                import time

                response1 = input("Let's begin! Shall we? (yes/no)")

                if response1.lower() == "yes":
                    time.sleep(2)
                    print("Alright. The first question is...")

                    def question1():

                        tries = 0
                        while True:
                            time.sleep(2)
                            response2 = input("What appears twice in a week, none in a month, and once in a year? ")

                            if response2.lower() == "e" or response2.lower() == "letter e" or response2.lower() == "the letter e":
                                time.sleep(2)
                                print("That's right!")
                                global score
                                score += 1
                                break

                            else:
                                time.sleep(2)
                                print ("WRONG!")
                                tries += 1
                                print ("Number of tries: " + str(tries))

                                time.sleep(2)

                                response3 = input("Do you want to try again, or receive a hint? (retry/hint)")

                                if response3.lower() == "retry":
                                    print("Alright...")

                                elif response3 == "hint":
                                    time.sleep(2)
                                    print("hint: think alphabetically")
                                    time.sleep(2)

                                else:
                                    print ("I don't understand what you're saying! Retrying Question 1...")

                            if tries >= 3:
                                time.sleep(2)
                                print(
                                    "Oops! It seems like you have used up all your tries. Moving to the next question...")
                                break

                    question1()

                    def question2():

                        tries = 0
                        while True:
                            time.sleep(2)
                            response4 = input("How many times you can subtract the number 5 from 25? ")

                            if response4.lower() == "once" or response4.lower() == "1" or response4.lower() == "one time":
                                time.sleep(2)
                                print("That's right!")
                                global score
                                score += 1
                                break

                            else:
                                time.sleep(2)
                                print("WRONG!")
                                tries += 1
                                print("Number of tries: " + str(tries))

                                time.sleep(2)

                                response5 = input("Do you want to try again, or receive a hint? (retry/hint)")

                                if response5 == "retry":
                                    print("Alright...")

                                elif response5 == "hint":
                                    time.sleep(2)
                                    print(
                                        "hint: After the first calculation, you will be subtracting 5 from 20, then 5 from 15, and so on.")
                                    time.sleep(2)

                                else:
                                    print("I don't understand what you're saying! Retrying Question 1...")

                            if tries >= 3:
                                time.sleep(2)
                                print(
                                    "Oops! It seems like you have used up all your tries. Moving to the next question...")
                                break

                    question2()

                    def question3():

                        tries = 0
                        while True:
                            time.sleep(2)
                            response6 = input("How many animals of each species did Adam take with him on the ark? ")

                            if response6.lower() == "none" or response6.lower() == "0" or response6.lower() == "no animals" or response6.lower() == "zero animals" or response6.lower() == "0 animals":
                                time.sleep(2)
                                print("That's right!")
                                global score
                                score += 1
                                break

                            else:
                                time.sleep(2)
                                print("WRONG!")
                                tries += 1
                                print("Number of tries: " + str(tries))

                                time.sleep(2)

                                response7 = input("Do you want to try again, or receive a hint? (retry/hint)")

                                if response7 == "retry":
                                    print("Alright...")

                                elif response7 == "hint":
                                    time.sleep(2)
                                    print("hint: Adam didn’t have an ark. Noah did.")
                                    time.sleep(2)

                                else:
                                    print("I don't understand what you're saying! Retrying Question 1...")

                            if tries >= 3:
                                time.sleep(2)
                                print(
                                    "Oops! It seems like you have used up all your tries. Moving on to the next question...")
                                break

                    question3()

                    def question4():

                        tries = 0
                        while True:
                            time.sleep(2)
                            response8 = input("I ate a ball with a curvy tail. What is it? ")

                            if response8.lower() == "9" or response8.lower() == "nine" or response8.lower() == "the number nine" or response8.lower() == "the number 9":
                                time.sleep(2)
                                print("That's right!")
                                global score
                                score += 1
                                break

                            else:
                                time.sleep(2)
                                print("WRONG!")
                                tries += 1
                                print("Number of tries: " + str(tries))

                                time.sleep(2)

                                response9 = input("Do you want to try again, or receive a hint? (retry/hint)")

                                if response9 == "retry":
                                    print("Alright...")

                                elif response9 == "hint":
                                    time.sleep(2)
                                    print("hint: It is a number.")
                                    time.sleep(2)

                                else:
                                    print("I don't understand what you're saying! Retrying Question 1...")

                            if tries >= 3:
                                time.sleep(2)
                                print(
                                    "Oops! It seems like you have used up all your tries. Moving on to the next question...")
                                break

                    question4()

                    def question5():

                        tries = 0
                        while True:
                            time.sleep(2)
                            response10 = input("What was missing when the turkey turned the key? ")

                            if response10.lower() == "n" or response10.lower() == "the letter n" or response10.lower() == "letter n":
                                time.sleep(2)
                                print("That's right!")
                                global score
                                score += 1
                                break

                            else:
                                time.sleep(2)
                                print("WRONG!")
                                tries += 1
                                print("Number of tries: " + str(tries))

                                time.sleep(2)

                                response11 = input("Do you want to try again, or receive a hint? (retry/hint)")

                                if response11 == "retry":
                                    print("Alright...")

                                elif response11 == "hint":
                                    time.sleep(2)
                                    print("hint: It is an alphabet.")
                                    time.sleep(2)

                                else:
                                    print("I don't understand what you're saying! Retrying Question 1...")

                            if tries >= 3:
                                time.sleep(2)
                                print(
                                    "Oops! It seems like you have used up all your tries. Moving on to the next question...")
                                break

                    question5()

                    if score >= 4:
                        time.sleep(2)
                        print("Hurray! You won!")
                        time.sleep(2)
                        print("Your answerd " + str(score) + " questions correctly.")
                        time.sleep(2)
                        print("Congratulations, Future Einstein!")

                    else:
                        response8 = input("NEVERMIND... you've lost. Try again? (yes/no) ")
                        if response8 == "yes":
                            game()
                        else:
                            print("Goodbye, then! Have a nice day.")

                elif response1 == "no":
                    time.sleep(2)
                    print("WHY??? I hate you!")
                    time.sleep(2)
                    print("Goodbye! :(")
                    time.sleep(2)

                else:
                    print("Invalid response.")
                    game()

            game()

        elif int(age) < age_requirementint:
            time.sleep(2)
            print("Too bad, you are not old enough to play.")

        else:
            print("Invalid response.")
            gameinit()
    else:
        print("Please enter a number! Restarting game...")
        time.sleep(2)
        gameinit()


gameinit()
