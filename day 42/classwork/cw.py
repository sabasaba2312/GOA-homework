numbers1 = {5, 10, 20, 50, 89, 105}
result = numbers1.add(159)
result2 = numbers1.add(200)
resul3 = numbers1.remove(50)
resul1 = numbers1.remove(10)

numbers2 = {19,60,37,26,90,50,105}

union = numbers1.union(numbers2)
print(union)

intersection = numbers1.intersection(numbers2)
print(intersection)

diference = numbers1.difference(numbers2)
print(diference)