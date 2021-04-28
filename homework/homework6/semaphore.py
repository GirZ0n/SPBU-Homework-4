from threading import Condition


class Semaphore:
    __size: int
    __condition: Condition

    def __init__(self, size: int = 1):
        if size < 0:
            raise ValueError("Semaphore initial size must be >= 0")

        self.__size = size
        self.__condition = Condition()

    def __enter__(self):
        with self.__condition:
            while self.__size == 0:
                self.__condition.wait()
            else:
                self.__size -= 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self.__condition:
            self.__size += 1
            self.__condition.notify()
