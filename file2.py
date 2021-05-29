class GFG(object): 
      __slots__=('a','b')
    
      def __init__(self, *args, **kwargs): 

                self.a = 1

                self.b = 2

if __name__ == "__main__": 

     instance = GFG() 

     print(instance.__slots__) 