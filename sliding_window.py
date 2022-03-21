def findSubString(s):
    di={i:0 for i in s}
    min_size = len(s)
    count = 0
    start = 0
    for end, val in enumerate(s):
        if di[val] == 0:
            count+=1
        di[val] +=1
        while count==len(di):
            min_size = min(min_size,end - start + 1)
            if di[s[start]]==1:
                break
            else:
                di[s[start]]-=1
                start+=1
    return min_size

print(findSubString("GEEKSGEEKSFOR"))
