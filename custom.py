from flask import redirect, render_template, request, session

""" Helpful custom functions created by your friendly neighborhood P4-Tide """


def apology(message, code=400):
    """Render message as an apology to user when errors occur."""
    return render_template("apology.html", code=code, message=message)


def convert(resultproxy):
    # convert the resultproxy into a dictionary
    d, a = {}, []
    for rowproxy in resultproxy:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)

    try:
        a = a[0]
    except:
        return False
    return a


def convertList(resultproxy):
    # convert the resultproxy into a dictionary
    d, a = {}, []
    for rowproxy in resultproxy:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)

    return a
