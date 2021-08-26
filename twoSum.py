def two_sum(numbers, target):
    hashmap = {}
    for i, num in enumerate(numbers):
        diff = target - num
        if diff in hashmap:
            return [i, hashmap[diff]]
        hashmap[num] = i
    return [-1, -1]