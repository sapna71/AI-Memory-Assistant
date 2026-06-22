from dotenv import load_dotenv
from langchain_groq import ChatGroq

from tools import (
    save_user_memory,
    recall_user_memory
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

class MemoryAgent:

    def invoke(self, inputs):

        user_input = inputs["input"]

        memories = recall_user_memory(user_input)

        prompt = f"""
You are a Memory Assistant.

Relevant Memories:
{memories}

Current User Message:
{user_input}

Use memories when relevant.

If user shares:
- name
- favorite things
- goals
- skills
- interests

remember them.
"""

        response = llm.invoke(prompt)

        triggers = [
            "my name is",
            "i like",
            "my favorite",
            "my goal",
            "remember that",
            "i am"
        ]

        if any(t in user_input.lower() for t in triggers):
            save_user_memory(user_input)

        return {
            "output": response.content
        }

agent_executor = MemoryAgent()