"""https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python"""


#Isograms


def is_isogram(string):
    saba = string.lower()
    goa = list(saba)
    for i in goa:
        if goa.count(i) > 1:
            return False
    return True