from flask import Blueprint, render_template

class Factorial:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0:
            raise ValueError("Factorial doesn't exist for negative numbers!")
        self._series = series
        self._value = 0
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Factorial sequence, this id called from __init__"""
    def calc_series(self):
        y = self._series
        b = 1
        for i in range(1, y+1):
            b = i*b
        self.set_data(b)

    def set_data(self, num):
        self._value = num

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def value(self):
        return self._value

    @property
    def number(self):
        return self._value

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 7
    '''Constructor of Class object'''
    factorial = Factorial(n)

    '''Using getters to obtain data from object'''
    print(f"Factorial number for {n} = {factorial.number}")
