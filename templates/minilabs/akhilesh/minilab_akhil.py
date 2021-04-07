from flask import Blueprint, render_template
import random

movielist = ["The SpongeBob Movie: Sponge on the Run", "Malcolm & Marie", "Tom & Jerry","Raya and the Last Dragon"]

# create the class
class Movies:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 8:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.movie_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def movie_series(self):
        limit = self._series
        f = [random.sample((movielist), k=2)]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= 1

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
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

# create the blueprint
akhil = Blueprint('akhil', __name__, url_prefix="/akhil", static_folder="static",
                  template_folder="templates")

@akhil.route('/minilab-akhil')
def minilabakhil():
    n = 2
    movierecs = Movies(n / n)
    return render_template("minilab-akhil.html", movierecs=Movies)


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 2
    '''Constructor of Class object'''
    movierecs = Movies(n)
    print(f"Here are some movie recomendations = {movierecs.list}")