"""https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python"""


#Reversed Words


def reverse_words(s):
    saba = s.split(" ")
    goa = saba[::-1]
    result = " ".join(goa)
    return result