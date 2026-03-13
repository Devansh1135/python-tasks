## Check balanced parantheses

def checkparanthesis(str):
    stack = []
    for char in str:
        if char == '(':
            stack.append(char)
        else :
            stack.pop()
    if len(stack) == 0:
        return "Yay its balanced!!!"
    
    return "IMBALANCED!!!"


## Postfix evaluator

def postfix(str):
    stack = []
    s = "0123456789"
    for char in str:
        if char in s:
            stack.append(char) 
        else:
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())
            operator = char
            if operator == '+':
                stack.append(operand1 + operand2)
            elif operator == '-':
                stack.append(operand1 - operand2)
            elif operator == '*':
                stack.append(operand1 * operand2)
            elif operator == '/':
                stack.append(operand1 / operand2)
            else:
                raise TypeError
        
        
    return stack

    
## Infix to Postfix

def infixtopostfix(expr):
    postfix = ""
    operators = []
    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
    }

    for char in expr:
        if char.isalpha():
            postfix+=char
        
        elif char == "(":
            operators.append(char)

        elif char == ")":
            while operators and operators[-1] != "(" :
                postfix+=operators.pop()
            operators.pop()

        else:
            while (operators and operators[-1] != "(" and priority[char] <= priority[operators[-1]]):
                postfix+=operators.pop()
            operators.append(char)

    while operators:
        postfix+= operators.pop()


    
    return postfix

print(infixtopostfix("(a+b)*(c+d)"))



