class Card:
    def __init__(self, value=None, naipe=None):
        self._value = value
        self._naipe = naipe

    def get_naipe(self):
        return self.naipe

    def get_value(self):
        return self.naipe

    def set_naipe(self, np):
        self._naipe = np

    def set_value(self, vl):
        self._value = vl

    def __str__(self):
        return "Naipe: " + str(self._naipe) + ", Valor: " + str(self._value)
