from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

class Shop():
    def __init__(self, name, weight, category, __file_name = 'products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        zapiska = file.read()
        file.close()
        print(f'{zapiska}')
    def __add__(self, *pruduct):
        for i in pruduct:
            tovar = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if tovar in f:
                print(f'Продукт {tovar} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{tovar}')
                file.close()













s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())