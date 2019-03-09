
class Vector(tuple):
    def __init__(self, array):
        super(Vector, self).__init__(array)

    def __add__(self, v):

        if not hasattr(v, '__len__'):
            return Vector([_+v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")
    

        return Vector([i+j for i,j in zip(self,v)])

    def __div__(self,v):

        if not hasattr(v, '__len__'):
            return Vector([_/v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")

        return Vector([i/j for i,j in zip(self,v)])


    def __mul__(self, v):

        if not hasattr(v, '__len__'):
            return Vector([_*v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")

        return Vector([i*j for i,j in zip(self,v)])
