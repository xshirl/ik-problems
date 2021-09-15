def find_intersection(arr1, arr2, arr3):
    # Write your code here
    def intersection(a,b):
        i = 0
        j = 0
        res = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res
    n = intersection(arr1, arr2)
    m = intersection(n, arr3)
    return m if len(m) > 0 else [-1]