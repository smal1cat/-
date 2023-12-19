def postfix_to_infix(postfix):
    stack = []
    operators = set (['+', '-', '*', '/'])

    for token in postfix:
        if token.isalnum():
            stack.append(token)
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = f"({operand1} {token} {operand2})"
            stack.append(expression)

    return stack.pop()

postfix_expression = ["A", "B", "C", "-", "D", "*", "+"]
infix_expression = postfix_to_infix(postfix_expression)
print(infix_expression)