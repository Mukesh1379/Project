def findUniqueNumbers(arr):
    xor_result = 0
    for num in arr: xor_result ^= num
    rightmost_set_bit = xor_result & -xor_result
    unique1, unique2 = 0, 0
    for num in arr:
        if num & rightmost_set_bit:
            unique1 ^= num
        else:
            unique2 ^= num
    return sorted([unique1, unique2])
arr = [1, 2, 3, 2, 1, 4]
print(findUniqueNumbers(arr))  
arr = [2, 1, 3, 2]
print(findUniqueNumbers(arr))
