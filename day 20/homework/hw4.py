#მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო
numbers = []
numberss = 0
number = int(input("enter number: "))
while -1 != number:
    number = int(input("enter number: "))
    if number == -1:
        numbers = numbers + [number]
        numberss = numberss + 1
avarage = numberss/len(numbers)
print(avarage)



