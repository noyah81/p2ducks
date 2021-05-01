from flask import Blueprint, render_template, request
import random

# create the class
class AbsoluteValue:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series):
        """Built in validation and exception"""
        self._series = series
        self._value = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.absv_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for find absolute value, this id called from __init__"""
    def absv_series(self):
        y = self._series
        b = 1
        if y > 0:
            b = y
        else:
            b = -y
        self.set_data(b)

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
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

# create the blueprint
akhil = Blueprint('akhil', __name__, url_prefix="/akhil", static_folder="static",
                  template_folder="templates")

@akhil.route('/minilab-akhil', methods=['POST', 'GET'])
def minilabakhil():
    if request.method == 'POST':
        n = int(request.form.get("series"))
        print("post")
        return render_template("/minilabs/akhil/minilab-akhil.html", absolutevalue=AbsoluteValue(n))
    else:
        return render_template("/minilabs/akhil/minilab-akhil.html", absolutevalue=None)


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 7
    '''Constructor of Class object'''
    absolutevalue = AbsoluteValue(n)
    print(f"The Absolute Value for {n} = {absolutevalue.number}")
