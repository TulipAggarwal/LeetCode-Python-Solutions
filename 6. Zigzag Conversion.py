class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            res = [""]* numRows
            up = 1
            row = 0
            for i in s:
                res[row] += i
                row += up
                if row >= numRows-1 or row ==0:
                    up *= -1
            result = ""
            for index in res:
                result += index
            return result
