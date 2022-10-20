

class Cal:
    
    def __init__(self):
        self.var1=None
        self.var2 = None

    def sum(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.output = var1+var2
        return self.output
        
    def subtract(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.output = var1-var2
        return self.output 
        
    def multiply(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.output = var1*var2
        return self.output
    
    def division(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.output = var1/var2
        return self.output
        

p1 = Cal()

output = p1.sum(1,2)
print ("The sum is:", output)
print("\n")

output = p1.subtract(4,2)
print ("The difference is:", output)
print("\n")

output = p1.multiply(1,2)
print ("The product is:", output)
print("\n")

output = p1.division(5,2)
print ("The quotient is:", output)

