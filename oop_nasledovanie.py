class Horse():
    is_horse = True


class Donkey():
    is_donkey = True


class Mulle(Horse, Donkey):
    pass


mull = Mulle()
print(mull.is_horse)
print(mull.is_donkey)



