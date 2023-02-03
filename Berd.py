class Berd():

    def __init__(self):
        print('Птица готова')

    def who(self):
        print('Птица')

    def fly(self):
        print('Летает быстрее')


class Peng(Berd):

    def __init__(self):
        super().__init__()  # Обращается к конструктору из родительского класса
        print('Пингвин готов')

    def who(self):
        print('Пингвин')

    def run(self):
        print('Быстрее бегает')


ping = Peng()
ping.who()
ping.fly()
ping.run()
