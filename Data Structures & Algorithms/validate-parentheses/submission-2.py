class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in '({[':
                stack = stack + [i]
            if i in ')}]':
                o = [k for k, v in hm.items() if v == i]
                if stack and stack[-1] == o[0]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
