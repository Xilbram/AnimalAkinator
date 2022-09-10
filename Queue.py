#a buffer is an example of queue


class Queue():
    def __init__(self, size: int):
        self.__size = size
        self.__queue = []
        self.__pos = -1

        for _ in range(self.__size):
            self.__queue.append(None)

    def showQueue(self):
        return self.__queue

    def isFull(self):
        if (self.__size == self.__pos):
            return True
        return False
    def isEmpty(self):
        if(self.__pos == -1):
            return True
        return False


    def insert(self, pData):
        if self.isFull():
            return "Full Queue"

        self.__pos += 1
        self.__queue[self.__pos] = pData
        return self.__queue[self.__pos]

    def remove(self):
        if self.isEmpty():
            return "Empty Queue"

        result = self.__queue[0]
        for i in range(self.__pos):
            self.__queue[i] = self.__queue[i+1]
        self.__queue[self.__pos] = None
        self.__pos -=1


        return result


queue1 = Queue(10)

for i in range(10):
    queue1.insert(i+10)

print("Original %s " %queue1.showQueue())

for i in range(5):
    queue1.remove()

    print(queue1.showQueue())

for i in range(4):
    queue1.insert(i+10)

    print(queue1.showQueue())