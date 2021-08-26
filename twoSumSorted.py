def pair_sum_sorted_array(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == target:
            return [i, j]
        elif sum < target: 
            i += 1
        else:
            j -= 1
            
    return [-1,-1]