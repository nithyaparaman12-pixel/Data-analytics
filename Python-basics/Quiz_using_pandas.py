import pandas as pd

# Quiz questions using Pandas
data = {
    "Question": [
        "What is the capital of India?",
        "Which language is used for Data Analysis?",
        "What does CPU stand for?",
        "Which library is used for data analysis in Python?"
    ],
    "Answer": [
        "Delhi",
        "Python",
        "Central Processing Unit",
        "Pandas"
    ]
}

df = pd.DataFrame(data)

score = 0
print("🎮 Welcome to Pandas Quiz Game!\n")

for i in range(len(df)):
    print(f"Q{i+1}: {df.loc[i, 'Question']}")
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == df.loc[i, 'Answer'].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {df.loc[i, 'Answer']}\n")

print("🎯 Game Over")
print(f"Your Score: {score} / {len(df)}")

# Result using Pandas logic
result = "Pass" if score >= 2 else "Fail"
print("Result:", result)
