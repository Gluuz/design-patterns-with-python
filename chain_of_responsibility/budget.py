class Budget:
    def __init__(self):
        self.__items = []

    @property
    def value(self):
        total = 0.0
        for item in self.__items:
            total += item.value

        return total

    @property
    def total_itens(self):
        return len(self.__items)

    def get_items(self):
        return tuple(self.__items)

    def add_item(self, item):
        self.__items.append(item)
