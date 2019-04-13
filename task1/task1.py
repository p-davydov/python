class CountId(object):
    id = 0


countId = CountId()


class GiverId(object):
    @classmethod
    def addId(cls):
        countId.id += 1
        return countId.id

    @property
    def id(self):
        if not hasattr(self, '_id'):
            self._id = 0
        else:
            self._id = self.addId()
        return self._id


class Account(GiverId):
    pass


class Vehicle(GiverId):
    pass


class Player(Account):
    def __init__(self):
        object_id_collector = self.id


class Bot(Account):
    def __init__(self):
        object_id_collector = self.id


class Tank(Vehicle):
    def __init__(self):
        object_id_collector = self.id


print Player().id, Player().id, Tank().id, Bot().id, Player().id
