# Project 4: General Knowledge Quiz Game
# DecodersLabs - Python Programming Internship

def run_quiz():
    score = 0

    questions = [
        {
            "question": "1. What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
            "answer": "B"
        },
        {
            "question": "2. Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
            "answer": "C"
        },
        {
            "question": "3. How many sides does a triangle have?",
            "options": ["A. Three", "B. Four", "C. Five", "D. Six"],
            "answer": "A"
        }
    ]

    print("       GENERAL KNOWLEDGE QUIZ GAME")
    print("Answer the following 3 questions.")
    print("Each correct answer earns 1 point.\n")

    for question in questions:
        print(question["question"])

        for option in question["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid choice. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer: ").strip().upper()

        if user_answer == question["answer"]:
            print("Correct! You earned 1 point.\n")
            score += 1
        else:
            print(
                f"Incorrect. The correct answer is "
                f"{question['answer']}.\n"
            )

    print("=" * 45)
    print("               QUIZ RESULTS")
    print("=" * 45)
    print(f"Your final score: {score}/3")

    if score == 3:
        print("Excellent! You answered every question correctly.")
    elif score == 2:
        print("Great job! You did very well.")
    elif score == 1:
        print("Good effort! Keep learning.")
    else:
        print("Keep practicing. You will improve!")

    print("=" * 45)


if __name__ == "__main__":
    run_quiz()