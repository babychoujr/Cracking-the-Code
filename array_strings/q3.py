

"""
Approach


Time Complexity:  O(n)
Space Complexity:  O(1)


"""


def URLify(test_string):

    split_string = test_string.split(' ')
    result = ""


    for i in range(len(split_string)):
        if i != len(split_string)- 1:
            result += split_string[i] + "%20"
        else:
            result += split_string[i]

    return result






if __name__ == "__main__":

    print("Final String: ", URLify("Mr John Smith"))