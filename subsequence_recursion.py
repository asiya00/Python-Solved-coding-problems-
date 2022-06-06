# s = "abbcac"
# # s = "abcdef"
# # s = "afabrabat"

# def substring(s, output="", li=[0]):
#     if len(s) == 0:
#         if len(output) != 0 and len(output) % 2 == 0:
#         	mid = len(output)//2
#         	if output[:mid] == output[mid:]:
#         		if li[0] < len(output):
#         			li[0] = len(output)
#         return li
#     output1 = output
#     output2 = output + s[0]
#     substring(s[1:], output1)
#     substring(s[1:], output2)
#     return li

# maximum = 0

# for i in range(len(s)):
# 	maxi_ans = substring(s[:len(s)-i]+s[len(s)-i:][::-1])
# 	maximum = max(maximum, maxi_ans[0]) 

# print(maximum)


n = 3
x = 1
y = 1
s = "ABA"

def substring(s, x, y, original, output="", li=[]):
    if len(s) == 0:
        count_A = output.count("A")
        count_B = len(output) - count_A
        if len(output) and output in original and count_A - count_B >= x and count_A - count_B <= y:
            li.append(output)
        return li
    output1 = output
    output2 = output + s[0]
    substring(s[1:], x, y, original, output1)
    substring(s[1:], x, y, original, output2)
    return li

print(len(substring(s, x, y, s)))
