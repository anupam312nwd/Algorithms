def reverse_string(str):
    if str == "":
        return str
    return reverse_string(str[1:]) + str[0]


if __name__ == '__main__':
    str = "abcd"
    rev_str = reverse_string(str)
    print(rev_str)
    print(str[-1])
    print(str[0])
    print(str[1:-1])
