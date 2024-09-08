from collections import deque

def findSteppingNumbers(n, m):
    result = []
    queue = deque(range(10))

    while queue:
        num = queue.popleft()
        
        if num > m:
            continue
        
        if n <= num <= m:
            result.append(num)
        
        last_digit = num % 10
        
        if last_digit > 0:
            next_num = num * 10 + (last_digit - 1)
            if next_num <= m:
                queue.append(next_num)
        
        if last_digit < 9:
            next_num = num * 10 + (last_digit + 1)
            if next_num <= m:
                queue.append(next_num)
    
    return sorted(result)

n, m = map(int, input().split())
print(' '.join(map(str, findSteppingNumbers(n, m))))
