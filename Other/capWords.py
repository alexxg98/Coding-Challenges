# Given a string as an input, design a function that returns the string with the first letter to every word capitalized.
#
# Sample Input: "problem example word"
# Sample Output: "Problem Example Word"

def capEachWord(a):
    """ Returns the string where every word is capitalized. This solution only changes the string's first letter, so all other letters are preserved. """
    
    b = a.split()
    for i in range(len(b)):
        b[i] = b[i].replace(b[i][0], b[i][0].upper(), 1)
    return (' '.join(b))

# a = "hello worldS"
a = input("Enter string: ")
print(capEachWord(a))
