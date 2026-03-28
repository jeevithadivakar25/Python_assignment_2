import os
import cohere
from dotenv import load_dotenv

load_dotenv()

# 1. API Configuration
co = cohere.Client(api_key=os.getenv("COHERE_API_KEY"))

# 2. Query Function
def query_cohere(prompt):
    """Query Cohere models"""
    try:
        response = co.chat(
            model='command-a-03-2025', 
            message=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter the prompt for Cohere: ")
    print("Querying Cohere...")
    result = query_cohere(user_prompt)
    print(f"\nResponse:\n{result}")