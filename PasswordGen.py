#This is a Password Generator
import secrets
import string

while True:
    # Define the full character set: letters (upper+lower), digits, and symbols
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ask the user to enter the desired password length
    length = int(input("The password length is: "))

    if length >= 8:
        # Guarantee at least 1 character from each category for password strength
        guaranteed = [secrets.choice(string.ascii_lowercase),  # 1 lowercase letter
                      secrets.choice(string.ascii_uppercase),  # 1 uppercase letter
                      secrets.choice(string.digits),           # 1 digit
                      secrets.choice(string.punctuation)]      # 1 symbol
       
        # Fill the remaining slots with random characters from the full set
        remaining = [secrets.choice(all_chars) for _ in range(length - 4)]
        # Combine guaranteed and remaining characters into one list
        password_list = guaranteed + remaining
        # Shuffle the list so guaranteed characters aren't always at the front
        secrets.SystemRandom().shuffle(password_list)
        # Join the list into a single string and print the final password
        password = "".join(password_list) 
        print(password)
    
    # Remind the user if the length is too short
    else: print("password at least 8 characters")