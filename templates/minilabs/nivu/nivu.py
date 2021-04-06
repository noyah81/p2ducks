from flask import Blueprint, render_template


class Exponential:
    def __init__(self, series):
        if series < 1 or series > 20:
            raise ValueError("Series must be between 1 and 20")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.exponential_series()

    def exponential_series(self):
        limit = self._series
        f = [1]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0] * 2]
            limit -= 1

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters """

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


# create the blueprint
nivu = Blueprint('nivu', __name__, url_prefix="/nivu", static_folder="static",
                 template_folder="templates")


@nivu.route('/minilab-nivu', methods=['POST', 'GET'])
def minilabnivu():
    return render_template("/minilabs/nivu/minilab-nivu.html", exponential=Exponential(3))


if __name__ == "__main__":
    n = 3
    exponential = Exponential(n)

    print(f"Exponential number for {n} = {exponential.number}")
    print(f"Exponential series for {n} = {exponential.list}")

    for i in range(n):
        print(f"Exponential sequence {i + 1} = {exponential.get_sequence(i)}")
