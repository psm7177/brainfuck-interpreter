from exception import OutOfRangeMemoryException


def validate_pointer(func):
    def decorator(self,*arg):
        func(self,*arg)
        if not 0 <= self.pointer < self.size:
            raise OutOfRangeMemoryException(f"{self.pointer} is in [0,{self.size})")
    return decorator

