def move_capitals_to_front(word):
     # Initialize an empty string to store capital letters
    capital = '' 
    # Initialize an empty string to store lowercase letters
    small = ''  

    # Iterate through each character in the word
    for char in word:
        # Check if the character is uppercase
        if char.isupper():  
            # Append uppercase letters to the capitals string
            capital += char  
        else:
            # Append lowercase letters to the lowercase string
            small += char  

    # Concatenate the capitals and lowercase strings
    result = capital + small

    return result

# Test the function
word = "HelloWorld"
print(move_capitals_to_front(word))  # Output: "HWelloorld"

   