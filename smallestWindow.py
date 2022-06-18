# brute force approach
s = "bdheedcfeeafhijabdbehhfaigjghiijabcfagjgcedbjhhehajgbgbiechagdfeaffejdhhihdhjjahbcgcgdfbfdadhdgefghchdhdigbjciehiebgahbahddhiidebcfaieefjgefaafhbfiabgdbjcfbaedgfhigbgibegjfjjgicjcgciccfdhehcgjdeccbfehdgcddighgagfbeheaccahgfggdbgeaiajeahegbcjadehajafjfcdbbjfgahhcjbaigfbfiifdegiafeejibcfbdecfeicbjgabhbhfdgebfjjjjbggfgcibhehchhffhcebcbdbcedbadjehffjihhdichhebajjgbehjacbbidagihdijjecfcjeibfadbdaehcfjfbjhgbdgbhdjggiajfgjfdifafgebdbjghbehceaiedabebhgigagehcfegjeaiehbfgedaddegiaahgacigafihahegefjgjhhijjfgbddhiafhbjiicjaaigeeeiiadj"
p = "cdaehaihiejehfcfajjcidcdhghfjejbgibadbbgbjegfhgggfgaefaaabcbgdiffdejdijebfebejhaccffehff"



# def smallestWindow(s, p):
#     if len(s) < len(p):
#         return -1
#     di = {i:0 for i in p}  #{o:2,1, z:2, 1, a:1}
#     start = 0 #1,2
#     li = []
#     start_ind = 0
#     last_ind = 0
#     minimum_size = len(s) #6, 5 
#     count = 0 #1,2,3
#     for end, val in enumerate(s):   #end=0,1,2,3,4,5,6  val=z,o,o,m,l,a,z
#         if val in di and di[val] == 0: #t  
#             di[val] = 1 
#             count += 1
#         else:
#             if val in di:
#                 di[val] += 1
#         # print(di)
#         while count == len(p):
#             print(count)
#             if end >= len(s):
#                 break
#             if end-start+1 < minimum_size:
#                 minimum_size = end-start+1
#                 start_ind = start
#                 last_ind = end

#             # minimum_size = min(minimum_size, end-start+1) #5-0+1 6-0+1 6-2+1
#             if s[start] in di: #start=0 s[start]=z, 
#                 if di[s[start]] == 1:
#                     # print(s[start:end+1])
#                     li.append(s[start:end+1])
#                     # print(di)
#                     break
#                 else:
#                     di[s[start]] -= 1
#                     start += 1
#             elif s[start] not in di:
#                 start += 1
#             # print(start, end)
#     return s[start_ind:last_ind+1], li

# # print(smallestWindow("zoomlazapzo", "oza"))
s = "bdheedcfeeafhijabdbehhfaigjghiijabcfagjgcedbjhhehajgbgbiechagdfeaffejdhhihdhjjahbcgcgdfbfdadhdgefghchdhdigbjciehiebgahbahddhiidebcfaieefjgefaafhbfiabgdbjcfbaedgfhigbgibegjfjjgicjcgciccfdhehcgjdeccbfehdgcddighgagfbeheaccahgfggdbgeaiajeahegbcjadehajafjfcdbbjfgahhcjbaigfbfiifdegiafeejibcfbdecfeicbjgabhbhfdgebfjjjjbggfgcibhehchhffhcebcbdbcedbadjehffjihhdichhebajjgbehjacbbidagihdijjecfcjeibfadbdaehcfjfbjhgbdgbhdjggiajfgjfdifafgebdbjghbehceaiedabebhgigagehcfegjeaiehbfgedaddegiaahgacigafihahegefjgjhhijjfgbddhiafhbjiicjaaigeeeiiadj"
p = "cdaehaihiejehfcfajjcidcdhghfjejbgibadbbgbjegfhgggfgaefaaabcbgdiffdejdijebfebejhaccffehff"
# print(smallestWindow(s, p))
