def evaluate_postfix(expr: str):
    stack = []

    for char in expr:
        if char.isdigit():
            stack.append(int(char))
        elif char in ('+', '-', '*', '/'):
            if len(stack) < 2:
                raise RuntimeError("Invalid expression")
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = evaluate_operation(operand1, operand2, char)
            stack.append(result)
        elif char == ' ':
            continue
        else:
            raise ValueError("Invalid character in expression")

    if len(stack) != 1:
        raise RuntimeError("Invalid expression")

    return stack[0]

def evaluate_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero")
        return operand1 / operand2
