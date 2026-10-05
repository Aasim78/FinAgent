from ollama import chat

import time

from prompts import SYSTEM_PROMPT

from tools import (
    get_financial_data,
    calculate_profit,
    calculate_profit_margin,
    calculate_growth,
    compare_months,
    analyze_financial_performance
)


MODEL = "qwen3:latest"


tools = [
    get_financial_data,
    calculate_profit,
    calculate_profit_margin,
    calculate_growth,
    compare_months,
    analyze_financial_performance
]


available_tools = {
    "get_financial_data": get_financial_data,
    "calculate_profit": calculate_profit,
    "calculate_profit_margin": calculate_profit_margin,
    "calculate_growth": calculate_growth,
    "compare_months": compare_months,
    "analyze_financial_performance": analyze_financial_performance
}


def ask_agent(question: str):
    
    start_time = time.time()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    while True:

        llm_start = time.time()

        response = chat(
            model=MODEL,
            messages=messages,
            tools=tools,
            think=False
        )

        llm_time = time.time() - llm_start
        print(f"[Timing] LLM call: {llm_time:.2f} seconds")

        messages.append(response.message)

        # If the model does not request a tool,
        # return its final answer.
        if not response.message.tool_calls:
            return response.message.content

        # Execute requested tools
        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print("\n[Agent Tool Call]")
            print("Tool:", function_name)
            print("Arguments:", arguments)

            function = available_tools.get(function_name)

            if function is None:
                result = {
                    "error": f"Unknown tool: {function_name}"
                }

            else:
                result = function(**arguments)

            print("[Tool Result]")
            print(result)

            messages.append({
                "role": "tool",
                "tool_name": function_name,
                "content": str(result)
            })