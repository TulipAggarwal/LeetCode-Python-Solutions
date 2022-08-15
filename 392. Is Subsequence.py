class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = ''
        j = 0
        for i in range(len(t)):
            if (j<len(s)): #condition to avoid going out of index
                if (s[j]==t[i]): #checking for equal values in s and t
                    temp += t[i] #adding values from string t to our temporary string
                    j += 1
        if (temp==s): #comparing the two strings to see if they're equal
            return True
        else:
            return False
            
            
