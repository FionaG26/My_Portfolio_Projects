#!/usr/bin/env python3
"""
Interactive Quiz on Common Python Coding Interview Questions

This script presents the user with a series of multiple-choice questions related to
Python programming. The user is prompted to select the correct option for each question.
After completing the quiz, the user receives feedback on their performance and sees
their final score.

The questions, options, and correct answers are defined in lists. The user's input is
compared to the correct answers to calculate the score.

Usage:
    Run the script, and the quiz will start. The user should enter their choice (a, b, c, or d)
    for each question. After answering all the questions, the script will display the final
    score and feedback.

Author:
    Fiona Githaiga
"""
def quiz():
    # Define the quiz questions, options, and correct answers
    questions = [
        "1. What is the output of the following code?\n\n"
        "   print(2 + 2 * 3 - 4)",

        "2. What will be the value of 'result' after the following code?\n\n"
        "   numbers = [1, 2, 3, 4, 5]\n"
        "   result = [x * 2 for x in numbers if x % 2 == 0]",

        "3. Which of the following is used to add an element at the end of a list in Python?",

        "4. What is the time complexity of searching for an element in a Python list using the 'in' keyword?",

        "5. What does the 'pass' keyword do in Python?",

        "6. What is the output of the following code?\n\n"
        "   num_list = [1, 2, 3, 4, 5]\n"
        "   print(num_list[-2])",

        "7. What does the 'yield' keyword do in Python?",

        "8. Which of the following is used to read user input in Python?",

        "9. What is the purpose of the 'self' keyword in Python class methods?",
    ]

    options = [
        ["a) 6", "b) 8", "c) 4", "d) 2"],
        ["a) [2, 4, 6]", "b) [4, 8]", "c) [8, 4]", "d) [2, 6, 4]"],
        ["a) append()", "b) add()", "c) insert()", "d) extend()"],
        ["a) O(1)", "b) O(n)", "c) O(log n)", "d) O(n^2)"],
        ["a) It raises an exception", "b) It continues to the next iteration of a loop",
         "c) It is used as a comment placeholder", "d) It terminates the program"],
        ["a) 4", "b) 3", "c) 5", "d) 2"],
        ["a) It defines a new class", "b) It creates an iterator",
         "c) It is used to pause and resume a function's execution", "d) It raises an exception"],
        ["a) read()", "b) input()", "c) get()", "d) scan()"],
        ["a) It is used to access class variables", "b) It is a reference to the current instance of the class",
         "c) It defines a new instance method", "d) It is used for exception handling"]
    ]

    correct_answers = ["c", "b", "a", "b", "c", "b", "c", "b", "b"]

    # Initialize the score
    score = 0

    # Welcome message
    print("Welcome to the Python Coding Interview Quiz!")
    print("Choose the correct option (a, b, c, or d) for each question.")

    # Display questions and get user input
    for i in range(len(questions)):
        print("\n" + questions[i])
        for option in options[i]:
            print(option)
        user_answer = input("Your answer: ").lower()

        # Check if the user's answer is correct
        if user_answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", options[i][0])

    # Display final score and feedback
    print("\nQuiz completed!")
    print("Your final score:", score, "out of", len(questions))
    if score == len(questions):
        print("Congratulations! You got a perfect score!")
    elif score >= len(questions) // 2:
        print("Well done! You did a good job.")
    else:
        print("Keep practicing to improve your Python coding skills!")

if __name__ == "__main__":
    quiz()
