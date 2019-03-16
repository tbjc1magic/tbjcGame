


class Vector(tuple):
    def __init__(self, *array):
        return


    def __new__(cls, *args):
        return super().__new__(cls, args)


    def __add__(self, v):

        if not hasattr(v, '__len__'):
            return Vector([_+v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")
    

        return Vector(*[i+j for i,j in zip(self,v)])

    def __div__(self,v):

        if not hasattr(v, '__len__'):
            return Vector(*[_/v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")

        return Vector(*[i/j for i,j in zip(self,v)])


    def __mul__(self, v):

        if not hasattr(v, '__len__'):
            return Vector([_*v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")

        return Vector(*[i*j for i,j in zip(self,v)])


class Position2D(Vector):

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]    
        
    def __new__(cls, *args):
        if len(args) != 2:
            raise Exception("wrong number of arguments for Position2D")
        return super().__new__(cls, *args)




if __name__ == "__main__":
    v = Vector(0,1,2)
    p = Position2D(1,2)
    print(p+(1,2))