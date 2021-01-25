# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, br in enumerate(text):
        if br in "([{":
            opening_brackets_stack.append([br, i])
            continue
        if br in ")]}":
            if opening_brackets_stack:
                left = opening_brackets_stack.pop()
                matching = are_matching(left[0], br)
                if not matching:
                    return i+1
                continue
            else:
                return i + 1

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0][-1] + 1
    return "Success"




def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
