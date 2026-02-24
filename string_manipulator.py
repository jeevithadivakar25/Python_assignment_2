

#Taking user input
sentence = input("Enter a sentence: ")

print("Original:", sentence)

print("Characters (with spaces):", len(sentence))

#Removing spaces using replace()
no_spaces = sentence.replace(" ", "")
print("Characters (without spaces):", len(no_spaces))

#splitting into individual words
words = sentence.split()
print("Words:", len(words))

#converting into upper, lower, and title cases
print("UPPERCASE:", sentence.upper())
print("lowercase:", sentence.lower())
print("Title Case:", sentence.title())


#checking for edge case and printing first and last words
if len(words) > 0:
    print("First word:", words[0])
else:
    print("First word: None")


if len(words) > 0:
    print("Last word:", words[-1])
else:
    print("Last word: None")

#Reversing string using slicing technique
print("Reversed:", sentence[::-1])