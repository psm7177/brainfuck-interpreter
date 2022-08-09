from decorator import validate_pointer


class Memory:
    def __init__(self,size = 1024):
        self._pointer = 0
        self.size = size
        # self.data = [0] * size
        self.data = bytearray(size)

    @property
    def current(self):
        return self.data[self._pointer]
    
    @current.setter
    def current(self,value):
        self.data[self._pointer] = value % 256

    @property   
    def pointer(self):
        return self._pointer

    @pointer.setter
    @validate_pointer
    def pointer(self,value):
        self._pointer = value
    
    def clear(self):
        self._pointer = 0
        self.data = bytearray(self.size)