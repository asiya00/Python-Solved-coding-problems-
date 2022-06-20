s = "zoomlazapzo"
p = "oza"

def smallestWindow(s, p):
    if len(s) < len(p):
        return -1

    di1 = {i:0 for i in s}
    di2 = {j:0 for j in p}
    count = 0
    minimum_size = float("inf")
    start = 0
    start_ind = float("inf")

    for k in p:
        di2[k] += 1

    for end in range(0, len(s)):
        di1[s[end]] += 1
        if s[end] in di2:
            if di1[s[end]] <= di2[s[end]]:
                count += 1

        if count == len(p):
            while (s[start] in di2 and di1[s[start]] > di2[s[start]]) or s[start] not in di2:
                if s[start] in di2 and di1[s[start]] > di2[s[start]]:
                    di1[s[start]] -= 1
                start += 1
            if end-start+1 < minimum_size:
                minimum_size = end-start+1
                start_ind = start
    if start_ind == float("inf"):
        return -1
        
    return s[start_ind: start_ind+minimum_size]

print(smallestWindow(s, p))







