"""https://www.codewars.com/kata/55b42574ff091733d900002f/train/python"""



# Friend or Foe?


def friend(x):
    result = []
    for i in x:
        if len(i) == 4:
            result.append(i)
    return result
