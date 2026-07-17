class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "[":
                stack.append("]")
            elif bracket == "(":
                stack.append(")")
            elif bracket == "{":
                stack.append("}")
            else:
                if not stack or stack.pop() != bracket:
                    return False
                
        if stack:
            return False
        return True