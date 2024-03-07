# solution 2

def solution(N):
  # stating the possible alphabets that exist
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  #  finding how many times the alphabets can be repeated
  repeats = N // 26
  # calculating the remaining characters after adding full repetitions
  remain = N % 26
  
  
  # constructing  the string by concatenating the alphabet string multiple times
  # first alphabet * repeats repeats the alphabet  string repeats times
  # if repeats is 2 then would result in all the alphabets repeated twice
  # alphabet[: remain] gets the first remain elements of the alphabet string and adds it to itself repeat times., so we add the remainder to it.
  # then they are added to bring the result
  result = alphabet * repeats + alphabet[:remain]
  
  return result

print(solution(3))
print(solution(5))
print(solution(30))