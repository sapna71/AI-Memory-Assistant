from agent import agent_executor

print(" Memory Assistant")
print("Type exit to quit")
#check 
while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    result = agent_executor.invoke(
        {"input": user_input}
    )

    print("\nAssistant:")
    print(result["output"])
