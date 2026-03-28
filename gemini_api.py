import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# 1. API Configuration
# Initializing the Gemini API client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. Query Function
def query_gemini(prompt):
    """Query Google Gemini API with a prompt""" 
    try:
        # Sending the prompt to the AI API 
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text 
    except Exception as e:
        return f"Error: {str(e)}" 

# 3. Main Execution
if __name__ == "__main__":
    # Getting user input
    user_prompt = input("Enter the prompt for Gemini: ")
    print("Querying API...")
    
    # Calling the query function and display response 
    result = query_gemini(user_prompt)
    print("\nResponse:")
    print(result)