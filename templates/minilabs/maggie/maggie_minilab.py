"""Minilab """
from flask import Blueprint, render_template, request
import random
import requests
import json


url = "https://www.episodate.com/api/most-popular?page=1"
response = requests.request("GET", url)
#print(type(response))

responseJsonObj = json.loads(response.text)
#print(type(responseJsonObj))


showList1 = []
for data in responseJsonObj['tv_shows']:
    showList1.append(data['name'])
#print(showList1)
n = 1

class Shows:
    """Initializer of class takes series parameter and returns Class Object"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 20:
            raise ValueError("Series must be between 0 and 20")
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
        f = [random.sample((showList1), k=self.series)]  # starting array/list
        #while limit > 0:
        self.set_data(f[0])
        #f = [f[0]]
        #limit = limit - 1

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


# create the blueprint
maggie = Blueprint('maggie', __name__, url_prefix="/maggie", static_folder="static",
                  template_folder="templates")


@maggie.route('/minilab-maggie', methods=["GET", "POST"])
def minilabmaggie():
    if request.method == 'POST':
        n = int(request.form.get("shows"))
        return render_template("/minilabs/maggie/minilab-maggie.html", showrecs=Shows(n))
    else:
        return render_template("/minilabs/maggie/minilab-maggie.html", showrecs=Shows(1))

mylist=[]
def bubbleSort():
    z = len(mylist)
    for x in range(z):
        for y in range(0, z-x-1):
            if mylist[y] > mylist[y+1]:
                mylist[y], mylist[y+1] = mylist[y+1], mylist[y]
    print(mylist)

@maggie.route('/bubblesortmaggie', methods=["GET", "POST"])
def bubblesortmaggie():
    if request.method == 'POST':
        print("1", request.form.get("sort1"))
        print("2", request.form.get("sort2"))
        print("3", request.form.get("sort3"))
        mylist.clear()
        if request.form.get("sort1") == "Submit":
            mylist.append(int(request.form.get("num1")))
            mylist.append(int(request.form.get("num2")))
            mylist.append(int(request.form.get("num3")))
            mylist.append(int(request.form.get("num4")))
            mylist.append(int(request.form.get("num5")))
        if request.form.get("sort2") == "Submit":
            mylist.append(request.form.get("string1"))
            mylist.append(request.form.get("string2"))
            mylist.append(request.form.get("string3"))
            mylist.append(request.form.get("string4"))
            mylist.append(request.form.get("string5"))
        if request.form.get("sort3") == "Submit":
            mylist.append(request.form.get("char1"))
            mylist.append(request.form.get("char2"))
            mylist.append(request.form.get("char3"))
            mylist.append(request.form.get("char4"))
            mylist.append(request.form.get("char5"))
        #print(mylist)
        bubbleSort()
        return render_template("/minilabs/maggie/minilab-maggie.html", mylist=mylist, showrecs=[])
    else:
        print("error")