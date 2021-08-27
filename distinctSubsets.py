def get_distinct_subsets(str):
    str = sorted(str)
    result = []
    def helper(slate, n):
        result.append(slate)
        if n == len(str):
            return
        unique = {}
        
        for index in range(n, len(str)):
            if str[index] not in unique:
                unique[str[index]] = 1
                helper(slate + str[index], index+1)
    
    helper("", 0)
    return result