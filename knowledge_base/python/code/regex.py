import re

# pattern = r'(\d{3})-(\d{2})-(\d{4})'

pattern1 = "^a...s$"
user_input = input("Guess game. Enter a word that starts with 'a' and ends with 's':")


def find_pattern(pattern, user_input):
    points = 0
    # This methods checks if the user input matches the regex pattern. 
    # Returns a match object if it matches, otherwise returns None.
    if re.match(pattern, user_input):
        points += 5
        print(f"{user_input} matched our pattern!You won 5 points! Your total is {points} points.")
        

    else:
        points -= 2
        print(f"{user_input} did not match our pattern. You lost 2 points! Your total is {points} points.")
        
        
    


find_pattern(pattern1, user_input)