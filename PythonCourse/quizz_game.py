
questions = ("How many elements are in periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A.116", "B.117", "C.118", "D.119 "),
           ("A.Whale", "B.Crocodile ", "C.Elephant ", "D.Ostrich"),
           ("A.Nitrogen", "B.Oxygen", "C.Carbon-Dioxide", "D.Hydrogen"),
           ("A.206", "B.207 ", "C.208 ", "D.209 "),
           ("A.Mercury", "B.Venera ", "C.Earth", "D.Mars"),)

answers = ("C", "D", "A", "A", "B")    #correct answers
guesses = [] #посочените от нас отговори
score = 0
question_number = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter (A, B, C or D):").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"Answer: {answers[question_number]} is the correct answer: ")

    question_number += 1

print("--------------------------")
print("       RESULTS            ")
print("--------------------------")

print("answers", end = " ")
for answer in answers:
    print(answer, end= " ")
print()

print("guesses", end = " ")
for guess in guesses:
    print(guess, end= " ")

print()
score = int(score / len(guesses) * 100)
print(f"Your score is {score}%")