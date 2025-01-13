class Solution:
    def calculate(self, s: str) -> int:
        """
        Calculate the result of a string mathematical expression with parentheses.
        Args:
            s: String containing mathematical expression
        Returns:
            int: Result of the calculation
        """
        stack = []
        operand = 0
        res = 0  # For the on-going result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                # Evaluate the expression to the left
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == "-":
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == "(":
                # Save the result and sign on the stack
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                operand = 0
            elif ch == ")":
                # Add the last operand
                res += sign * operand
                # Multiply by sign at top of stack
                res *= stack.pop()
                # Add saved result from stack
                res += stack.pop()
                operand = 0
            # Skip spaces
            elif ch == ' ':
                continue

        return res + sign * operand
      