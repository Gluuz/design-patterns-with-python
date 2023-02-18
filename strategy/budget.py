class Budget:
    def __init__(self, value: int):
        self.__value = value

    @property
    def value(self):
        return self.__value
