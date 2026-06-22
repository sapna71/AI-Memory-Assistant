from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

print("Loaded:", key[:15] + "..." if key else "NO KEY FOUND")