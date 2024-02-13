class Programmer:
    rates = {'Junior': 10,
             'Middle': 15,
             'Senior': 20}

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.time = 0
        self.salary = 0

    def work(self, time):
        self.time += time
        salary = time * Programmer.rates[self.position]
        self.salary += salary

    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
        elif self.position == 'Middle':
            self.position = 'Senior'
        elif self.position == 'Senior':
            Programmer.rates['Senior'] += 1

    def info(self):
        return f'{self.name} {self.time}ч. {self.salary}тгр.'
