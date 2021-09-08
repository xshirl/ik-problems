class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}
        res = []
        if len(digits) == 0:
            return res
        def dfs(path, res):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            next_num = digits[len(path)]
            for char in keyboard[next_num]:
                path.append(char)
                dfs(path, res)
                path.pop()
        dfs([], res)
        return res