class testclass:

    def __init__(self, y, z):
        self.f = y*3
        self.g = z*2
        #print(self.f)
        #print(self.g)

class childclass(testclass):
    def __init__(self, a, b):
        #self.a = a
        #self.b = b
        super().__init__(a,b)
        print(self.f)
        print(self.g)

class child2class(testclass):
    def __init__(self, c, d):
        pass

#obj1 = testclass(1,2)
obj2 = childclass(10,30)
