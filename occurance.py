import re
def countX(re,x): 
    count = 0
    for ele in re: 
        if (ele == x): 
            count = count + 1
    return count 
   
txt = "I love apples, apples are my favorite fruit"

re=re.findall(r"\w",txt)
for i in re:
	print('{} {}'.format(i,countX(re,i)))
		
	