import requests
import json

# 1. API Configuration
# Ollama serves a local API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# 2. Query Function
def query_ollama(prompt):
    """Query local Ollama models""" 
    try:
        # Configuration for the local request
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False # Set to False for a single response string
        }
        
        # Send the prompt to the local AI API
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        
        # Return the AI response
        return response.json().get('response')
    except Exception as e:
        # Handle errors gracefully 
        return f"Error: {str(e)}" 

# 3. Main Execution
if __name__ == "__main__":
    # Get user input  
    user_prompt = input("Enter your prompt for Ollama: ")
    print("Querying Local API...")  
    
    # Display the AI response
    result = query_ollama(user_prompt)
    print("\nResponse:")
    print(result)