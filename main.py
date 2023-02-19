# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            if len(opening_brackets_stack)==0 or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            else:
                opening_brackets_stack.pop(-1)
            # Process closing bracket, write your code here
                pass
        
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
        


def main():
    text = input("ievad")
    mismatch = find_mismatch(text)
    if not mismatch:
        print('Success')
    else:
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
