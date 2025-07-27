def digitize(n):
    result = str(n)
    result1 = list(result)
    result2 = result1[::-1]
    numbers = []
    for i in result2:
        result3 = int(i)
        numbers.append(result3)
    return numbers