def solve(expression):
    num1 = float(expression.split()[0])
    num2 = int(expression.split()[2])
    ext = expression.split()[1]
    result = ''
    if ext == '*':
        result = num1 * num2
    elif ext == '/':
        result = num1 / num2
    elif ext == '+':
        result = num1 + num2
    elif ext == '-':
        result = num1 - num2
    elif ext == '^':
        result = pow(num1, num2)
    print(f'{result:.2f}')
