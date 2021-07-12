
### Book Solution #1
###Approach:
### Sort both strings and check if the characters are in the same order
### Clean way however not the most efficient

"""
Approach:
Check if both strings have the same character counts

Time Complexity:  O(n)
Space Complexity:  O(n)
"""


def isPermutation(str1, str2):


    if len(str1) != len(str2):
        return False


    countDict1 = {}
    countDict2 = {}

    """
    Approach:
    Check the letter count of both strings and compare

    Works Fine but some redundancy

    for i in str1:
        if i in countDict1:
            countDict1[i] += 1
        else:
            countDict1[i] =1

    for j in str2:
        if j in countDict2:
            countDict2[j] += 1
        else:
            countDict2[j] =1
    
    for i in str1:
        if countDict1[i] != countDict2[i]:
            return False
    """

    #Book Approach

    count_list = [0] * 128

    for i in str1:
        count_list[ord(i)] += 1

    for j in str2:
        count_list[ord(j)] -= 1
        if count_list[ord(j)] < 0:
            return False

    return True
    



if __name__ == "__main__":


    print(isPermutation("afe", "afe"))