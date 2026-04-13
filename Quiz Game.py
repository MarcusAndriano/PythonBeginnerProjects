# Python Quiz Game

questions = ("Who is my favorite player of all time?: ",
             "How many champions league trophies does Man City have?: ",
             "Who is number 11 on man city?: ",
             "Who is the worst team in the premier league?: ",
             "What opponent does UEFA like to milk games against City?: ")

options = (("A. Sergio Aguero","B. Kevin De Bruyne","C. Jeremy Doku","D. Christian Benteke"),
           ("A. 0","B. 1","C. 2","D. 3"),
           ("A. Rodri","B. Nico Gonzalez","C. Jeremy Doku","D. Pep Guardiola"),
           ("A. Tottenham Hotspur","B. Manchester City (Wrong)","C. Leeds United","D. Arsenal"),
           ("A. Real Madrid","B. Arsenal","C. DC United","D. Inter Miami"))

answers = ("A", "B", "C", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} was the correct answer!")
    question_num += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers:", end= " ")
for answer in answers:
    print(answer, end= " ")
print()

print("guess:  ", end= " ")
for guess in guesses:
    print(guess, end= " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")