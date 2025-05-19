#შექმენით პროგრამა რომელშიც გექნებათ ხილის სია კალათა (list), 
#შემდეგ მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი (input), 
#დაადეკლარირეთ ცვლადი რომელიც დაადგენს არის თუ არა ხილი 
#კალათაში (variable) fruit_in_basket რომლის მნიშვნელობა თავიდან 
#იქნება False, for ციკლის საშვალებით (for loop) განიხილეთ კალათა 
#და პირობითი განცხადების საშვალებით (if-else) შეადარეთ მომხარებლის 
#საყვარელ ხილს, თუ ისინი ტოლი იქნება fruit_in_basket ცვლადის 
#მნიშვნელობა შეცვალეთ True boolean-ით, საბოლოოდ პირობითი განცხადების 
#საშვალებით (if-else) შეამოწმეთ მომხმარებლის საყვარელი ხილი არის თუ 
#არა კალათაში fruit_in_basket, თუ არის დაუბეჭდეთ 'Good choice' თუ
#არ არის 'Fruit not in basket'

fruits = ["apple", "banana", "watermelon", "pear", "peach", "kiwi", "melon", "strawberry"]
best_fuit = input("enter your favourite fruit: ")
fruit_basket = False

for goa in fruits:
    if goa == best_fuit:
        fruit_basket = True

if fruit_basket:
    print("good choice")
else:
    print("Fruit not in basket")