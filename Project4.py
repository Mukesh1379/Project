def reduceTicketPrice(ticket, k):
    stack = []
    for digit in ticket:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    final_number = stack[:-k] if k > 0 else stack
    result = ''.join(final_number).lstrip('0')
    return result if result else '0'

ticket = input().strip()
k = int(input().strip())
print(reduceTicketPrice(ticket, k))
