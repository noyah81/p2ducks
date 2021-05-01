
from flask import Blueprint, render_template, request


#Enhance or Define a Class
class Factorial:
    """Initializer of class takes series parameter and returns Class Object"""

    def __init__(self, number):
        """Built in validation and exception"""
        if number < 1 or number > 10:
            raise ValueError("Number must be between 1 and 10")
#Create an Object from a Class in Python
        self._number = number
        self._result = 1
        self.calc_factorial()

    def calc_factorial(self):
        limit = self._number
        while limit > 0:
            self._result = self._result * limit
            self._result = ()
            print(self._result)
            limit -= 1

    #Display data or enhanced data from this Python Object on Project Web Page using "getters"
    @property
    def result(self):
        return self._result


    @property
    def number(self):
        return self._number


# create the blueprint
noya = Blueprint('noya', __name__, url_prefix="/noya", static_folder="static",
                 template_folder="templates")

@noya.route('/factorial', methods=["GET", "POST"])
def factorial():
    # request form is from action button on html
    if request.form:
        return render_template("/minilabs/noya/noya.html", fact=Factorial(int(request.form.get("num"))))
    # first call from menu
    return render_template("/minilabs/noya/noya.html", fact=Factorial(2))


if __name__ == "__main__":
    '''Value for testing'''
    n = 6
    '''Constructor of Class object'''
    fact = Factorial(n)
    print(f"Here is the factorial for {fact.number} = {fact.result}")


