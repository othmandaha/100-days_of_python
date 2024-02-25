from art import logo

print(logo) 

alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'}


def caesar(text, shift, direction):
    
    result = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                shifted = (index + shift)
                if shifted > 25:
                    shifted = (shifted - 26)
                result += alphabet[shifted]
            elif direction == "decode":
                shifted = (index - shift)
                if shifted < 0:
                    shifted = (shifted + 26)
                result += alphabet[shifted]
        else: 
            result += letter 
    print(f"Your {direction}d message is {result}") 
        

decision = 'yes' 
while decision == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    

    
    

