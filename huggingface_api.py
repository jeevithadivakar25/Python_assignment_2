import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# 1. API Configuration

MODEL_ID = "Qwen/Qwen2.5-7B-Instruct" 
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

# Using environment variable
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

# 2. Query Function
def query_huggingface(prompt):
    """Query Hugging Face using the 2026 Router API"""
    try:
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 500,
                "temperature": 0.7
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        
        response.raise_for_status()
        
        return response.json()[0]['generated_text']
        
        
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Hugging Face: ")
    print("Querying Hugging Face...")
    
    result = query_huggingface(user_prompt)
    print(f"\nResponse:\n{result}")