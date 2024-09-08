def wordBreak(s, dictionary):
    word_set = set(dictionary)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return 1 if dp[n] else 0
n = 6
s = "ilike"
dictionary = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(wordBreak(s, dictionary)) 
s = "ilikesamsung"
print(wordBreak(s, dictionary))
