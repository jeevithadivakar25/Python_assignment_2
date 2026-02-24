#function to count words
def count_words(text):
    words = text.split()
    return len(words)

#function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

#function to count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

#reversing text
def reverse_text(text):
    return text[::-1]

#checking palindrome
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

#removing vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

#Calculating word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# finding longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

#main logic
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    
    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")
    
    print("Without vowels:", remove_vowels(text))
    
    longest = longest_word(text)
    print(f"Longest word: {longest} ({len(longest)} letters)")
    
    freq = word_frequency(text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")

#taking user input
text = input("Enter text: ")
analyze_text(text)