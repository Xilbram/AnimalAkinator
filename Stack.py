#-1 is useful to indicate that a stack is empty


class Stack():
    def __init__(self, size: int):
        self.__size = size
        self.__pos = -1
        self.stack = [None] * self.__size


    def push(self, pData):
        if self.isFull():
            return IndexError

        self.__pos += 1
        self.stack[self.__pos] = pData
        return self.stack[self.__pos]


    def pop(self):
        if self.isEmpty():
            return IndexError

        self.stack[self.__pos] = None
        self.__pos -= 1
        return self.stack[self.__pos +1]


    def isFull(self):
        if(self.__size == self.__pos -1):
            return True

        return False


    def isEmpty(self):
        if(self.__pos == -1):
            return True

        return False




stack1 = Stack(10)

for i in range(5):
    print(stack1.push(10+i))



