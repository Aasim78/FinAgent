from ollama import chat


response = chat(
    model="qwen3:latest",
    messages=[
        {
            "role": "user",
            "content": "Explain profit margin in one simple sentence."
        }
    ]
)


print(response.message.content)