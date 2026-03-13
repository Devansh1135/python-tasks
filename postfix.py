def infixtopostfix(expr):
    postfix = ""
    operators = []
    
    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    for char in expr:
        
        if char.isalpha():                 # operand
            postfix += char
        
        elif char == "(":                  # left parenthesis
            operators.append(char)
        
        elif char == ")":                  # right parenthesis
            while operators and operators[-1] != "(":
                postfix += operators.pop()
            operators.pop()                # remove "("
        
        else:                              # operator
            while (operators and operators[-1] != "(" and
                   priority[char] <= priority[operators[-1]]):
                postfix += operators.pop()
            operators.append(char)

    while operators:                       # pop remaining operators
        postfix += operators.pop()

    return postfix


print(infixtopostfix("(a+b)*(c+d)"))