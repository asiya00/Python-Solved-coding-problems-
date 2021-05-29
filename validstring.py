string = "{[}]"
b = len(string)
st = ""

for i in range(len(string)):
	if "()" in string:
		j = string.index("()")
		string = string[:j] + string[j+2:]
		st = st + "()" 
		if len(st)==b:
			print(True)
			break
		
	if "[]" in string:
		j = string.index("[]")
		st = st + "[]" 
		string = string[:j] + string[j+2:]
		if len(st)==b:
			print(True)
			break
			
	if "{}" in string:
		j = string.index("{}")
		string = string[:j] + string[j+2:]
		st = st + "{}" 
		if len(st)==b:
			print("True")
			break
	
else:
		print(False)
		