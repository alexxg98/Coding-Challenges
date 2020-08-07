# Solution to Longest Word Challenge using Python
#
# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.

import re

def LongestWord(sen):

  #delete all non-alphabet letters - if not a-zA-Z, replace with ''
  temp = re.compile('[^a-zA-Z ]').sub('', sen)
  wordsList = temp.split()
  longest = ""
  
  for word in wordsList:
    if len(word) > len(longest):
      longest = word

  return longest

print("Longest Word Challenge")
input = input("Enter a sentence/string: ")
print("Longest Word in '", input, "' is", LongestWord(input))
