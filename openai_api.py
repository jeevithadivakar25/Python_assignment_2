import os
from openai import OpenAI
from dotenv import load_dotenv

# Loading variables from .env
load_dotenv()

# 1. API Configuration
# Initializing client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Query Function
def query_openai(prompt):
    """Query OpenAI GPT models"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500, 
            temperature=0.7 
        )
        return response.choices[0].message.content 
    except Exception as e:
        return f"Error: {str(e)}" 

# 3. Main Execution 
if __name__ == "__main__":
    user_prompt = input("Enter the prompt for OpenAI: ")  
    print("Querying API...") 
    result = query_openai(user_prompt)
    print("\nResponse:") 
    print(result) 