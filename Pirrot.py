class Pirrot():
    # Атрибут класса
    spec = "Птица"

    # Инициализация конструктора
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Создаем экземпляры класса
kesha = Pirrot("Кеша", 10)
zhorik = Pirrot("Жорик", 15)

# Получаем доступ к атрибутам класса
print(f'Кеша - {kesha.__class__.spec}')
print(f'Жорик - {zhorik.__class__.spec}')

# Получаем доступ к атрибутам экземпляра
print(f'Мой попугай {kesha.name}, ему {kesha.age} лет')
print(f'Попугай друга {zhorik.name}, ему {zhorik.age} лет')

