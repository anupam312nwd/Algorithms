
input_str = input("type the string: ")
str_length = input("type the true string length: ")

def URLify(in_str, str_len):

    new_str = in_str[:str_len]

    return new_str.replace(" ", "%20")

if __name__ == "__main__":

    print(URLify(input_str, int(str_length)))
