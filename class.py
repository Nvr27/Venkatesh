class rectangle:
    def __init__(self,breadth,height):
        self.breadth=breadth
        self.height=height
    def area(self):
        return self.breadth*self.height
obj=rectangle(10,20)
print(obj.breadth)
print(obj.height)
print(obj.area())