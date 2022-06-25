class Flower:
	def __init__(self):
		self.name = "Rose"
		self.no_petals = 26
		self.price = 15.5

	def settingvalue(self,a,b,c):
		self.name = a 
		self.no_petals = b
		self.price = c 

	def flowername(self): 
		return self.name

	def petals(self):
		return self.no_petals

	def flowerprice(self):
		return self.price



obj = Flower()
obj.settingvalue('Sunflower',24,12.5)
print(obj.flowername())
print(obj.petals())
print(obj.flowerprice())
