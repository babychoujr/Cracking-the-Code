##Q1.1 Is Unique:
## Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?



"""
Approach:
1.Calculate the number of letters in the string
2. If two appear, return false

Time Complexity:  O(n)
Space Complexity:  O(n)

def isUnique(test_string):

    str_dict = {}

    for i in test_string:
        if i in str_dict:
            return False
        else:
            str_dict[i] = 1
    
    return True
"""

"""
2nd Approach:
1. Since there is only 128 characters possible,
    1. check the number of characters and if > 128, return not Unique
    2. create a boolean array where each array cell is equal to whether it has been seen or not before
    3. For example, each index would represent the input from the test_string
        IF 'X' is the test character, asiii code of 'X' is 120.
        SO fill in count_char[120] = True
        The next loop would loop over the next character and if the next character is also 'X' then the program would tell us that the test_string  is not Unique.

Time Complexity: O(n)
Space Complexity: O(1)  ? isn't it O(n) & not O(1)
"""

def isUnique(test_string):
    if len(test_string) > 128:
        return False

    count_char = [False] * 128


    for i in range(len(test_string)):
        val = ord(test_string[i])
        if count_char[val]:
            return False
        count_char[val] = True

    return True



if __name__ == "__main__":

    print("IsUnique: " , isUnique("sdfgh"))
