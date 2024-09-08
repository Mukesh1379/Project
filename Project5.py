def getMaxToys(prices, money):
    max_toys = 0
    current_sum = 0
    start = 0
    for end in range(len(prices)):
        current_sum += prices[end]
        
        while current_sum > money:
            current_sum -= prices[start]
            start += 1
        max_toys = max(max_toys, end - start + 1)
    return max_toys
n = 7
prices = [1, 4, 5, 3, 2, 1, 6]
money = 6
print(getMaxToys(prices, money))
