# quiz game

# tuple of questions
questions = ("How many elements are in the periodic table?: ",
             "Which animal always the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

# 2d list of options
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# tuple of answers
answers = ("C", "D", "A", "A", "B")

# list of guesses
guesses = []

# score counter
score = 0

# question number counter
question_num = 0

# iterate through each question in questions tuple
for question in questions:
    print ("-------------------------")
    print (question)
    # iterate through each option in options 2d list (include brackets)
    for option in options[question_num]:
        print (option)

    # prompt user to choose an answer
    guess = input("Enter (A, B, C, D): ").upper()
    # add that guess to the list of guesses
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print ("CORRECT!")
    else: 
        print ("INCORRECT!")
        print (f"{answers[question_num]} is the correct answer")
    # increment question number to print new options
    question_num +=1

print ("-------------------------")
print ("         RESULTS         ")
print ("-------------------------")

# prints out the answers of the quiz
print ("answers: ", end=" ")
for answer in answers:
    print (answer, end=" ")
print ()

# prints out the guesses you had
print ("guesses: ", end=" ")
for guess in guesses:
    print (guess, end=" ")
print ()

score = int(score / len(questions) * 100)
print (f"Your score is: {score}%")