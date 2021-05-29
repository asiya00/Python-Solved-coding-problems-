class Animal:
	element=0
	def __init__(self,name,height,weight,sound):
		self._name=name
		self._height=height
		self._weight=weight
		self._sound=sound
		
		Animal.element+=1
	
	def get_name(self):
		return self._name
	
	def get_height(self):
		return self._height
		
	def get_weight(self):
		return self._weight
	
	def get_sound(self):
		return self._sound
		
	def get_type(self):
		print("Animal")
	
	'''def __str__(self):
		return "{} is {} cm tall, {} in weight and sounds {}".format(self._name,self._height,self._weight,self._sound)'''
		
class dragon(Animal):
	_breath=" "
	
	def __init__(self,name,height,weight,sound,breath):
		self._breath=breath
		super(dragon,self).__init__(name,height,weight,sound)
		
	def set_breath(self,breath):
		self._breath=breath
		
	def get_breath(self):
		return self_breath
	
	def __str__(self):
			return "{} is {} cm tall, {} in weight and sounds {} and breathes {} ".format(self._name,self._height,self._weight,self._sound,self._breath)
			
	def multiplesounds(self,time=None):
		if time==None:
			print(self.get_sound())
		else:
			print(self.get_sound(),str(time),"times!")
			
cat = Animal("Cat",33,40,"meow")
mydragon=dragon("Methyldragon",33,50,"Rawr","The breath of song")
print(mydragon)
mydragon.multiplesounds()
mydragon.multiplesounds(2)
print(mydragon.element)
print(cat.element)
#print(cat)
#print(cat.get_name())

		