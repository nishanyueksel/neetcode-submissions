class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        
        idea: use stack, every time operation is given,
        remove top two numbers
        use the operation 
        add newest number
        ex: tokens = ["1","2","+","3","*","4","-"]
        stack = []
        we add 1, 2 then get +
        add 1, 2 get 3 => stack only has three
        stack.append(3) stack has [3,3]
        operation is *, so 3*3 = 9, add 9 to stack
        then we get 4, and minus so 9-4 = 5 
        """
        stack = []
        operations = {
            "+" : lambda x, y : x + y,
            "-" : lambda x, y : x - y,
            "*" : lambda x, y : x * y,
            "/" : lambda x, y : int(x / y)
        }
        for i in tokens:
            if i in operations:
                op = operations.get(i)
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = op(operand2, operand1)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack.pop()

        