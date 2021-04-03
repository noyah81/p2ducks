"""Minilab """
from flask import Blueprint, render_template
import random

showlist1 = ["wandavision", "falcon and the winter soldier", "stranger things", "the office", "the mandalorian", "the voice", "america's got talent"]

class Shows:
    """Initializer of class takes series parameter and returns Class Object"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 7:
            raise ValueError("Series must be between 0 and 7")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.show_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building sequence, this id called from __init__"""
    def show_series(self):
        limit = self._series
        f = [random.sample((showlist1), k=2)]  # starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit = limit - 1

    """Method/Function to set data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]
'''
def maggie_minilab():
    n = 2
    showrecs = Shows(n/n)
    return showrecs
'''

# create the blueprint
maggie = Blueprint('maggie', __name__, url_prefix="/maggie", static_folder="static",
                  template_folder="templates")


@maggie.route('/minilab-maggie')
def minilabmaggie():
    n = 2
    showrecs = Shows(n / n)
    return render_template("/minilabs/maggie/minilab-maggie.html", showrecs=Shows(2))

# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 2
    '''Constructor of Class object'''
    showrecs = Shows(n/n)
    print(f"Here are some show recommendations = {showrecs.list}")
