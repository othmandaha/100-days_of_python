import pandas

# Read the NATO alphabet CSV file into a DataFrame
nato = pandas.read_csv("Day26-nato_alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv")

# Create a dictionary mapping each letter to its corresponding NATO phonetic code
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

# Prompt the user to input a word
usr_in = input("Enter a word: ").upper()

# Convert each letter of the input word into its corresponding NATO phonetic code
result = [nato_dict[letter] for letter in usr_in]

# Print the list of NATO phonetic codes corresponding to the input word
print(result)

