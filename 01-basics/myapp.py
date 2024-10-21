
questions = ("What city do The Beatles come from?: ",
                       "Which team won the Premiere league title in season 23/24?: ",
                       "Where was the first modern Olympic Games held?:  ",
                       "How many bones are in the human body?: ",
                       "Which football team is known as ‘The Red Devils’?: ",
                       "How many planets are there in a solar system?: ")

options = (("A. Prague", "B. Dublin", "C. Liverpool", "D. London"),
                   ("A. Arsenal", "B. Brighton", "C. Chelsea", "D. Manchester City"),
                   ("A. Athens", "B. Prague", "C. Rome", "D. Budapest"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Nottingham Forest", "B. Manchester United", "C. Brentford", "D. West Ham United"),
                   ("A. 6", "B. 7", "C. 8", "D. 9"))

answers = ("C", "D", "A", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()



score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
print("----------------------")
