class Quota:
    def __init__(self, value, amount):
        self.value = value
        self.amount = amount


class Nfs:
    def __init__(self, id, number, name, quotas):
        self.id = id
        self.number = number
        self.name = name
        self.quotas = quotas
