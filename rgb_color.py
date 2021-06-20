def rgb(r,g,b):
	round = lambda x: min(255, max(x, 0))
	return("{:02X}{:02X}{:02X}".format(round(r), round(g), round(b)))
	'''
	li = [r,g,b]
	color =""
	for i in li:
		if i < 0:
			color = color + '00'
		elif i > 255:
			color = color + 'FF'
		else:
			color = color + '{:2x}'.format(i)
	return color.upper()'''
	
print(rgb(-20,275,125))