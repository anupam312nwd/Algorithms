from enum import Enum


class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2


if __name__ == '__main__':
    redc = Color.RED
    bluec = Color.BLUE
    greenc = Color.GREEN

    print(f'if redc is red: {redc == Color.RED}')
    print(f'if bluec is blue: {bluec == Color.BLUE}')
