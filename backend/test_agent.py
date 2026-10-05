from agent import ask_agent


questions = [
    "What was the profit in March?",
    "What was March's profit margin?",
    "Compare January and March."
]


for question in questions:

    print("\n================================")
    print("QUESTION:", question)
    print("================================")

    answer = ask_agent(question)

    print("\nFINAGENT:")
    print(answer)