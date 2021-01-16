from structures.queues import Stack

LEFT_PARENTHESIS = '('
RIGHT_PARENTHESIS = ')'


def is_expression_valid(expression: str) -> bool:
    stack = Stack[str]()
    for char in expression:
        if char == LEFT_PARENTHESIS:
            stack.push(char)
        elif char == RIGHT_PARENTHESIS:
            if len(stack) > 0 and stack.front() == LEFT_PARENTHESIS:
                stack.pop()
            else:
                return False
    return not len(stack) > 0


if __name__ == '__main__':
    case = '((()))'
    print(f'{case}, is valid: {is_expression_valid(case)}')

    case = '((()()))'
    print(f'{case}, is valid: {is_expression_valid(case)}')

    case = '((())))'
    print(f'{case}, is valid: {is_expression_valid(case)}')

    case = '((()))('
    print(f'{case}, is valid: {is_expression_valid(case)}')