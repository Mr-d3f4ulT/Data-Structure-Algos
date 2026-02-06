#Madlibs Game is a word game where one player prompts another for a list of words to substitute for blanks in a story, before reading the - often comical or nonsensical - story aloud. The game is frequently played as a party game or as a pastime.
#The game is also used as a language learning tool, as it encourages players to think about parts of speech and sentence structure.

#Here is a simple implementation of a Madlibs Game in Python:

print("--- Welcome to the Python Mad Libs! ---")
print("Fill in the blanks to create a ridiculous story.\n")

# 1. Gathering inputs from the user
adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb_ed = input("Enter a verb (past tense): ")
place = input("Enter a place: ")
adj2 = input("Enter another adjective: ")
noun2 = input("Enter a plural noun: ")
animal = input("Enter an animal: ")

# 2. Creating the story template using f-strings
story = f"""
Once upon a time, there was a {adj1} {noun1} who loved to code. 
One day, they {verb_ed} all the way to {place}. 
It was a {adj2} sight! People were throwing {noun2} in the air, 
and a giant {animal} was dancing in the street. 
The {noun1} decided that Python was definitely the magic behind it all.
"""

# 3. Printing the final masterpiece
print("\n--- Here is your story! ---")
print(story)