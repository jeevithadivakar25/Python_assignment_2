import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# 1. API Configuration
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Query Function
def query_groq(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter the prompt for Groq: ")
    print("Querying Groq...")
    print(f"\nResponse:\n{query_groq(user_prompt)}")