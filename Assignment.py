class Calculation:
    def add(self, x, y):
        return x+y
    
    def sub(self, x, y):
        return x-y
    
    def Product(self, x, y):
        return x*y
    
    def divide(self, x, y):
        return x/y
    
    obj1 = Calculation()
    print(obj1.add(5,5))
    print(obj1.sub(10,5))
    print(obj1.product(5,4))
    print(obj1.divide(20,2))
    
    obj2 = Calculation()
    print(obj2.add(5,6))
    print(obj2.sub(20,10))
    print(obj2.product(5,4))
    print(obj2.divide(40,4))