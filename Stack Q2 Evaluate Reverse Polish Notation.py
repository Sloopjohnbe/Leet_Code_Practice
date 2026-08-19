"""Stack Q2 Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


"""
#11ms
#Beats34.37%
#13.61MB
#Beats43.44%
class Solution(object):
    def evalRPN(self, tokens):
        work = []
        for i in tokens:
            if i.lstrip("-").isdigit():
                work.append(int(i))
            else:
                first = work.pop()
                second = work.pop()

                if i == "+":
                    work.append(second + first)
                elif i == "-":
                    work.append(second - first)
                elif i == "*":
                    work.append(second * first)
                elif i == "/":
                       work.append(int(float(second) / first))

        return(work[0])

        
Output = Solution()
print(Output.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


#0ms
"""class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # Division truncated toward zero
                    if a * b < 0:
                        stack.append(-(abs(a) // abs(b)))
                    else:
                        stack.append(abs(a) // abs(b))

        return stack[-1]"""