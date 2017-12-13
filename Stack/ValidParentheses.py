# Python program to determine if parentheses in a string match
# The string only contains parentheses characters


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use stack to store the left only
        stack = []
        dic = {'{':'}', '[':']', '(':')'}
        
        for c in s:
            # if it is left in the string, put it in the stack
            if c in dic:
                stack.append(c)
            # if it is right in the string
            else:
                # if the stack is empty or (not-empty-stack and c does not match the key for value of last element in the stack)
                if not stack or(stack and dic[stack.pop()] != c):
                    return False
                
        return not stack
        

s = '()[{}]'

a = Solution()
Ans = a.isValid(s)


if Ans:
    print "Parentheses match"
else:
    print "Parentheses do not match" 
