class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0 :
            x = 1/x
            n = n * -1
            
        while n:
            if n &1:
                result = result * x
            n >>= 1
            x = x* x
        return result
