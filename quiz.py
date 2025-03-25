# quiz.py - A simple Python quiz app

def run_quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 8 + 3?": "11",
        "Which planet is known as the Red Planet?": "Mars"
    }
    
    score = 0
    
    for question, correct_answer in questions.items():
        answer = input(question + " ").strip().capitalize()
        if answer == correct_answer:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer is {correct_answer}.")
    
    print(f"\nYou scored {score}/{len(questions)}.")

if __name__ == "__main__":
    print("Welcome to the Quiz App! 🎉")
    run_quiz()
