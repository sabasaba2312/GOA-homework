"""https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/python"""


#Indexed capitalization


def capitalize(s, ind):
    saba = ""
    for i in range(len(s)):
        if i in ind:
            saba = saba + s[i].upper()
        else:
            saba = saba + s[i]
            
    return saba