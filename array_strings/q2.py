


"""
Approach:


Time Complexity:  O(n)
Space Complexity:  O(n)
"""


def isPermutation(str1, str2):


    if len(str1) != len(str2):
        return False


    countDict1 = {}
    countDict2 = {}


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

    return True
    



if __name__ == "__main__":


    print(isPermutation("afefef", "afefea"))