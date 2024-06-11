#shows questions 
question_list = ["Question 1: What is the capital city of New Zealand?", "Question 2: What are the primary colors?", "Question 3: How many days are in a week?", "Question 4: What are the vowels of the alphabet?", "Question 5: What is the tallest animal in the world?"]


#print version
print("Version 2 (Final)")

#asks the user if they wanted to play
ask = input("Hello, would you like to play the quiz? ")
print("-----------------------------------------------------------")

#keep going 
keep_going = ""
while keep_going == "":

  #if user says yes
    if ask == "yes" or ask == "y" or ask == "Yes":

#score
      score = 0
      score = int(score)

      #correct answers added to list
      correct_user_questions = []


        #multiple choice
      q1a = "A"
      q2a = "B"
      q3a = "C"

        #introduction
      print("Hello! Welcome to the General Knowledge Quiz...")
      name = input("What is your name? ")
      if name == (""):
        print("Please type in  your name..")
      else:
        print(
            "Hello {}! I will ask you 5 questions and give you three choices for each question."
            .format(name))
      print("You will select a choice between A, B or C for your answer.")
      print(
            "At the end of the quiz you will get to know what your score is.")
      print("Let's play!")
      print("-----------------------------------------------------------")

        #question1
      print(question_list[0])
      print("A) Auckland")
      print("B) Wellington")
      print("C) Dunedin")
      print("")

      q1 = input("Your answer: ")
      if q1 == "b" or q1 == "B":
          score += 1  #<- gives 1 point
          correct_user_questions.append(1)
          print("Well done! {}) is correct!".format(q2a))
          print(
                "-----------------------------------------------------------")

      else:
          print("Incorrect! The answer is {}) Wellington...".format(q2a))
          print(
                "-----------------------------------------------------------")

        #question2
      print(question_list[1])
      print("A) Red, Yellow & Blue")
      print("B) Green, Orange & Purple")
      print("C) Black & White")
      print("")
      q2 = input("Your answer: ")

      if q2 == "a" or q2 == "A":
          score += 1
          correct_user_questions.append(2)
          print("Well done! {}) is correct!".format(q1a))
          print(
                "-----------------------------------------------------------")
      else:
          print("Incorrect! The answer is {}) Red, Yellow & Blue...".format(
                q1a))
          print(
                "-----------------------------------------------------------")

        #question3
        
      print(question_list[2])
      print("A) 10")
      print("B) 5")
      print("C) 7")
      print("")
      q3 = input("Your answer: ")

      if q3 == "c" or q3 == "C":
          score += 1
          correct_user_questions.append(3)
          print("Well done! {}) is correct!".format(q3a))
          print(
                "-----------------------------------------------------------")
      else:
          print("Incorrect! The answer is {}) 7".format(q3a))
          print(
                "-----------------------------------------------------------")

    #question4
      print(question_list[3])
      print("A) A, B, C, D, E")
      print("B) A, E, I, O, U")
      print("C) V, W, X, Y, Z")
      print("")
      q4 = input("Your answer: ")

      if q4 == "b" or q4 == "B":
          score += 1
          correct_user_questions.append(4)
          print("Well done! {}) is correct!".format(q2a))
          print(
                "-----------------------------------------------------------")
      else:
          print("Incorrect! The answer is {}) A, E, I, O, U".format(q2a))
          print(
                "-----------------------------------------------------------")

    #question5
      print(question_list[4])
      print("A) Ostrich")
      print("B) Elephant")
      print("C) Giraffe")
      print("")
      q5 = input("Your answer: ")

      if q5 == "c" or q4 == "C":
          score += 1
          correct_user_questions.append(5)
          print("Well done! {}) is correct!".format(q3a))
          print(
                "-----------------------------------------------------------")
      else:
          print("Incorrect! The answer is {}) Giraffe".format(q3a))
          print(
                "-----------------------------------------------------------")

        #shows score and correct answers
      print("Your final score is: {}".format(score))
      print("You have correctly answered questions", correct_user_questions)

        #User can have an option to keep going or end the program
      keep_going = input("Press <enter> to play again or any key to quit ")
      print("-----------------------------------------------------------")

    #end the program
    elif ask == "no" or ask == "n":
        print("...")
        keep_going = "end"

    else:
        print("Please enter yes or no.")
        keep_going = "end"
