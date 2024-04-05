#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


names = []
letter = ""
with open(r"Day24-Files_directories_path\Mail Merge Project Start\Input\Names\invited_names.txt", 'r') as f:
    names = f.readlines()

with open(r"Day24-Files_directories_path\Mail Merge Project Start\Input\Letters\starting_letter.txt") as f:
    letter = f.read()

for i, name in enumerate(names):
    striped_name = name.strip("\n")
    new_letter = letter.replace("[name]", striped_name)
    with open(rf"Day24-Files_directories_path\Mail Merge Project Start\Output\ReadyToSend\letter {i}.txt", 'w') as f:
        f.write(new_letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp