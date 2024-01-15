# A pangram is a sentence that contains every single letter
# of the alphabet at least once. For example, the sentence 
# "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).
#Given a string, detect whether or not it is a pangram. Return True 
# if it is, False if not. Ignore numbers and punctuation.
def is_pangram(s):
#     convert the sentence into lower case and remove the non alphabetic characters
    clean_sentence = ''.join(char.lower() for char in s if char.isalpha())
#     create a set of unique characters in the cleaned set
    unique_char = set(clean_sentence)
#     check if the set of unique characters contains alphabets
    return set('abcdefghijklmnopqrstuvwxyz') <=unique_char
# write your pangram sentence
s = "The quick brown fox jumps over the lazy dog"
# call the function
result = is_pangram(s)
# print the results
print(result)

  