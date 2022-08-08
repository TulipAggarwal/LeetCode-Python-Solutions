class RomanInt:
    def romanToInt(self, s: str) -> int:
        romanconvert = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000,
        }
        integersol = 0
        for i in range (len(s)-1): #len(s)-1 because otherwise string will go out of index
            if romanconvert[s[i+1]] > romanconvert[s[i]]:
                integersol-= romanconvert[s[i]]
            else:
                integersol+= romanconvert[s[i]]
                
        integersol+= romanconvert[s[len(s)-1]] #Accessing and adding the last digit here
        return integersol
