#მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)
xmovani = " "
tanxmovani = " "
sityva = input("enter sityva: ")
for i in sityva:
    if sityva == "a":
        xmovani = xmovani + i
    elif sityva == "e":
        xmovani = xmovani + i
    elif sityva == "i":
        xmovani = xmovani + i
    elif sityva == "o":
        xmovani = xmovani + i 
    elif sityva == "u":
        xmovani = xmovani + i
    else:
        tanxmovani = tanxmovani + i
print(len(xmovani))
print(len(tanxmovani))


