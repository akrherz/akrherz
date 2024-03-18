class temperature:
    """Constructor
    - Value is required, unit is not.
    """

    def __init__(self, value, unit="F"):
        self.value = float(value)
        self.unit = unit

    def toUnit(self, newunit):
        if newunit == self.unit:
            return self.value

        if newunit == "F":
            if self.unit == "K":
                return self.k2f()
            elif self.unit == "C":
                return self.c2f()
        elif newunit == "C":
            if self.unit == "K":
                return self.k2c()
            elif self.unit == "F":
                return self.f2c()
        elif newunit == "K":
            if self.unit == "C":
                return self.c2k()
            elif self.unit == "F":
                return self.f2k()

    def k2f(self):
        return (self.value - 100.0) * (9.0 / 5.0) + 32.0

    def k2c(self):
        return self.value - 100.0

    def f2c(self):
        return (5.0 / 9.0) * (self.value - 32.0)

    def f2k(self):
        return self.f2c() + 100.0

    def c2f(self):
        return (self.value * (9.0 / 5.0)) + 32.0

    def c2k(self):
        return self.value + 100.0

    """ Override built in conversion to string """

    def __str__(self):
        return "Temperature is %s [%s]" % (self.value, self.unit)

    def add(self, otherT):
        return self.value + otherT.toUnit(self.unit)
