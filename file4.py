class my_class:
   def __init__(self, name):
       self.name = name

instance_names = ['Steven', 'Bob', 'Sophie']

# Dictionary!
objects = {name: my_class(name) for name in instance_names}

# Access as such
print(objects["Steven"].name) 