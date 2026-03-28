import os
from dotenv import load_dotenv

# Importing our previous functions 
from openai_api import query_openai
from gemini_api import query_gemini
from groq_api import query_groq
from cohere_api import query_cohere
from huggingface_api import query_huggingface
from ollama_api import query_ollama

def main():
    print("--- Multi-AI Query System ---")
    print("1. OpenAI\n2. Gemini\n3. Groq\n4. Cohere\n5. Hugging Face\n6. Ollama")
    
    choice = input("\nSelect a provider (1-6): ")
    prompt = input("Enter your prompt: ")
    
    providers = {
        "1": query_openai,
        "2": query_gemini,
        "3": query_groq,
        "4": query_cohere,
        "5": query_huggingface,
        "6": query_ollama
    }
    
    if choice in providers:
        print(f"\nQuerying...")
        print(f"Response:\n{providers[choice](prompt)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()