
from itertools import permutations

def isPalindrome(s): 
#   reverse string
    rev = s[::-1]
    return True if (s == rev) else False
  
def list_of_permutations(word):    
    word_permutations = permutations(list(word))
    list_of_permutations = []
    
    for item in word_permutations:
        temp_string = ""
        item_len = len(item)
        for index in range(0,item_len):
            temp_string = temp_string + item[index]
        list_of_permutations.append(temp_string)
    return (list_of_permutations)
    
    
def test_this_word_for_palindrome(word):
    permutations = list_of_permutations(word)
    found = False

    for specific_word in permutations:
        if (isPalindrome(specific_word) == 1):
            print (word + " -> True\n")
            found = True
            break
        
    if (found == False):
        print (word + " -> False\n")
        

if __name__== "__main__":
    
#*************
#Given a string, write a function to determine if a permutation of the string could form a palindrome.

#For example,
#"code" -> False, "aab" -> True, "carerac" -> True.
#*************
    
    # put words to test for palindrome into this list
    
    words_to_test = ["code", "aab", "carerac"]

    for word in words_to_test:
        test_this_word_for_palindrome(word)
    


        
        
    
    