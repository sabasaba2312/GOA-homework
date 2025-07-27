#შექმენით ლექსიკონი animal, შექმენით მისი ასლი .copy() მეთოდით, შემდეგ კი გამოიყენეთ .clear() ორივეზე (დასაწყისში და ბოლოს დაბეჭდეთ ორივე ლექსიკონი, კომენტარით)

animals = {
    "frinveli": "arwivi",
    "shinauri": "zagli",
    "gareuli": "datvi",
    "wyalqvesha": "tevzi"
}

copy_animals = animals.copy()

print(animals)
print(copy_animals)


result1 = animals.clear()
result2 = copy_animals.clear()

print(result1)
print(result2)

#clear - წაშლის ყველა ელემენტს