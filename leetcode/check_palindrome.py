def get_palindrome(s, left_index, right_index, str_len):
    while (left_index > 0) and (right_index < str_len + 1):
        if s[left_index - 1] == s[right_index + 1]:
            left_index -= 1
            right_index += 1
            continue
        break
    return s[left_index : right_index + 1], right_index


pal, ri = get_palindrome("abcbat", 1, 3, 6)
print(pal)
print(ri)
