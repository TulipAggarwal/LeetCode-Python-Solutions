class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dictionary = {"--X" : -1, "X--" : -1,
                 "++X" : 1, "X++" : 1}
        return sum(dictionary[i] for i in operations)
