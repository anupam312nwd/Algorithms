""" found this code online """

# assuming that max ascii characters we are considering are 128

input_str = input("input string: ")

def isUnique(input_str):

    len_str = len(input_str)
    len_set = len(set(input_str))

    if len_str > 128:
        return False
    else:
        return len_str == len_set

if __name__ == "__main__":

    val = isUnique(input_str)

    if val is True:
        print("input string is Unique")
    else:
        print("input string is NOT Unique")
