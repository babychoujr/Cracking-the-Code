##Q1.1 Is Unique:
## Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?



"""
Approach:
1.Calculate the number of letters in the string
2. If two appear, return false

Time Complexity:  O(n)
Space Complexity:  O(n)
"""
def isUnique(test_string):
    #test_string.sort()


    #for i in range(1, len(test_string)):
       # if test_string[i-1] == test_string[i]:
          #  return False

    #return True

    str_dict = {}

    for i in test_string:
        if i in str_dict:
            return False
        else:
            str_dict[i] = 1
    
    return True




if __name__ == "__main__":

    print("IsUnique: " , isUnique("djfkadjfkasdf"))
