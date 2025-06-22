"""https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python"""


#Count of positives / sum of negatives


def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []

    count = 0 
    negative_sum = 0
    for num in arr:
        if num > 0:
            count = count + 1
            
    for number in arr:
        if number < 0:
            negative_sum = negative_sum + number
    return [count, negative_sum]