#!/usr/bin/env python


def reverse_string(s: str):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])


if __name__ == "__main__":
    s = "string"
    print(reverse_string(s))
