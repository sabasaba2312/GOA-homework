"""https://www.codewars.com/kata/546e2562b03326a88e000020/train/python"""

#Square Every Digit

def square_digits(num):
    number = ""
    for i in str(num): 
        number2 = int(i) * int(i) 
        number += str(number2) 
    return int(number)