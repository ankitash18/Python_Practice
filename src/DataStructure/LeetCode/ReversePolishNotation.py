"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid.
That means the expression would always evaluate to a result and there won't be any divide by zero operation.

"""


def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in '+-*/':
            num2, num1 = stack.pop(), stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append((num1 / num2))
        else:
            stack.append(int(token))
    return stack[0]



tokens =  ["2", "1", "+", "3", "*"]
a= evalRPN(tokens)
print(a)


