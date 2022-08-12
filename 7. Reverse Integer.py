class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        string = string[::-1]
        answer = int(string)
        if answer >= 2**31-1 or answer <= -2**31: #checking the 64 bit constraint
            return 0
        elif x<0:
            return -1*answer
        else:
            return answer
