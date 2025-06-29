#შექმენით სიები fruits, colors, numbers. თითოეულზე გამოიყენეთ index, count, sort, sorted, min, max მეთოდები & ფუნქციები და დააკომენტარეთ თითოეული მაგალითი (რას აკეთებს)
fruits = ["banana", "peach", "apple", "strawberry"]
colors = ["red", "green", "blue", "yellow", "black"]
numbers = [1, 5 , 8 ,10, 20, 37]

print(fruits.index("peach"))
print(colors.index("blue"))
print(numbers.index(37))

print(fruits.count("peach"))
print(colors.count("yellow"))
print(numbers.count(37))


numbers1 = numbers.sort
print(numbers1)

print(sorted(numbers))

print(min(numbers))
print(max(numbers))