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

    str_dict = {}

    for i in test_string:
        if i in str_dict:
            return False
        else:
            str_dict[i] = 1
    
    return True




if __name__ == "__main__":

    print("IsUnique: " , isUnique("djfkadjfkasdf"))
