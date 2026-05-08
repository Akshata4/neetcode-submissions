class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## prep the string

        s = s.replace(' ', '').lower()
        s = [i  for i in s if i not in '!?\';.,[]-)(@#$%^&*<<>?:"{})']

        mid = len(s)//2

        f, l = 0, len(s)-1
        while f <= l:
            print(s[f], s[l])
            if s[f]!=s[l]:
                return False
            f += 1
            l -= 1
        return True
