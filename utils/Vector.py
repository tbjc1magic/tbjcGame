


class Vector(tuple):
    def __init__(self, *array):
        return


    def __new__(cls, *args):
        return super().__new__(cls, args)

    def __rsub__(self,v):
        return self.__sub__(v)*-1

    def __sub__(self, v):
        return self.__add__(v*-1)

    def __add__(self, v):

        if not hasattr(v, '__len__'):
            return Vector(*[_+v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")
    
        return Vector(*[i+j for i,j in zip(self,v)])

    def __floordiv__(self,v):
        if not hasattr(v, '__len__'):
            return Vector(*[_//v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")

        return Vector(*[i//j for i,j in zip(self,v)])



    def __truediv__(self,v):
        if not hasattr(v, '__len__'):
            return Vector(*[_/v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")

        return Vector(*[i/j for i,j in zip(self,v)])

    def __rmul__(self, v):
        return self.__mul__(v)

    def __mul__(self, v):

        if not hasattr(v, '__len__'):
            return Vector(*[_*v for _ in self])  

        if len(self) != len(v):
            raise Exception("The sizes of the two vectors are not matching")

        return Vector(*[i*j for i,j in zip(self,v)])

    def __round__(self):
        return Vector(*[round(_) for _ in self])

class Vector2D(Vector):

    def __getattr__(self,k):
        if k in ['x','w','c']:
            return self[0]

        if k in ['y','h','r']:
            return self[1]
        
        raise Exception('unidentified attribute')

    def __new__(cls, *args):
        if len(args) != 2:
            raise Exception("wrong number of arguments for Position2D")
        return super().__new__(cls, *args)




if __name__ == "__main__":
    v = Vector(0,1,2)
    p = Vector2D(1,2)
    print(p//(1,2.))
    print(round(Vector2D(1.1,2.1)))
    #print(p+(1,2))
    print(2*p)
    print(p-1)
    print(1-p)

    print(p.x,p.w)