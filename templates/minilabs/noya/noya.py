import self as self

class Numbers:
    """Initializer of class takes series parameter and returns Class Object"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 10:
            raise ValueError("Series must be between 1 and 10")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

def number_series(self):
    limit = self._series
    while limit > 0:
        self.set_data(f[0])
        f = [f[0]]
        limit -= 1

def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

@property
def series(self):
    return self._series

@property
def list(self):
    return self._list

@property
def number(self):
    return self._list[self._dictID - 1]
def get_sequence(self, nth):
    return self._dict[nth]
if __name__ == "__main__":
    '''Value for testing'''
    n = 5
    '''Constructor of Class object'''
    numberseries= Numbers(n)
    print("Here is a series of numbers = {numberserieslist}")