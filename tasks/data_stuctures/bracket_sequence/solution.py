def is_correct_bracket_seq(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack
