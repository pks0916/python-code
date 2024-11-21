class Evenlist():
    def __init__(self, L):
        self._evenlist = [i for i in L if i % 2 == 0]
    def add(self):
        pass
    def remove(self):
        pass
    def numbers(self):
        return sorted(self._evenlist, reverse=True)