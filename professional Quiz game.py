import random

def quiz():
    print("🎮 Welcome to the Python Quiz Game!")
    name = input("Enter your name: ")
    print(f"\nHello {name}, get ready! 🚀")

    # Difficulty levels
    levels = {
        "easy": {
            "questions": {
                "1. What is 2 + 2?": "a",
                "2. Which one is an even number?": "c",
            },
            "options": [
                ["a. 4", "b. 5", "c. 6"],
                ["a. 3", "b. 5", "c. 8"],
            ]
        },
        "medium": {
            "questions": {
                "1. What is the capital of Germany?": "b",
                "2. Who developed Python?": "a",
            },
            "options": [
                ["a. Paris", "b. Berlin", "c. Rome"],
                ["a. Guido van Rossum", "b. Elon Musk", "c. Bill Gates"],
            ]
        },
        "hard": {
            "questions": {
                "1. Which year was Python released?": "b",
                "2. What does HTML stand for?": "c",
            },
            "options": [
                ["a. 2000", "b. 1991", "c. 1985"],
                ["a. Hyper Trainer Marking Language", "b. High Text Machine Language", "c. Hyper Text Markup Language"],
            ]
        }
    }

    # Choose difficulty
    print("\nChoose difficulty: Easy / Medium / Hard")
    choice = input("Enter level: ").lower()

    if choice not in levels:
        print("Invalid choice! Defaulting to Easy 😅")
        choice = "easy"

    questions = list(levels[choice]["questions"].items())
    options = levels[choice]["options"]

    # Randomize questions
    combined = list(zip(questions, options))
    random.shuffle(combined)

    score = 0
    correct = 0
    wrong = 0

    # Quiz loop
    for (q, ans), opts in combined:
        print("\n" + q)
        for opt in opts:
            print(opt)

        user_ans = input("Enter your answer (a/b/c): ").lower()

        if user_ans == ans:
            print("✅ Correct!")
            score += 1
            correct += 1
        else:
            print("❌ Wrong!")
            wrong += 1

    total = len(questions)
    percentage = (score / total) * 100

    # Summary
    print("\n📊 QUIZ SUMMARY 📊")
    print(f"Player: {name}")
    print(f"Total Questions: {total}")
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"Score: {score}/{total} ({percentage:.2f}%)")

    if score == total:
        print("🏆 Excellent! Perfect score!")
    elif score >= total/2:
        print("👍 Good job, keep practicing!")
    else:
        print("😅 Better luck next time!")

    # Replay option
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == "y":
        quiz()
    else:
        print(f"👋 Thanks for playing, {name}!")


if __name__ == "__main__":
    quiz()
