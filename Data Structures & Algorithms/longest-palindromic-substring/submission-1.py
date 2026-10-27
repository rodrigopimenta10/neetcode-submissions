class Solution:
    def longestPalindrome(self, s: str) -> str:
        #if len(s) == 1:


        def is_palindrome(start,end):
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        
        res = 0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if is_palindrome(i,j) and (j-i+1) > res:
                    res = max(res,j-i+1)
                    ret = s[i:j+1]
                #print(f'i:{i},j:{j},res:{res}')
        
        return ret