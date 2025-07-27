#შექმენით ლექსიკონი person და გამოიყენეთ .items() მეთოდი, რათა დაბეჭდოთ ყველა key და value წყვილად. გამოიყენეთ loop და კომენტარი დაუმატეთ შედეგს
person = {
    "name" : "saba",
    "hoby" : "footballer",
    "height" : 1.78,
    "weight": 72

}


result = person.items()
for key,value in result:
    print(f"{key}: {value}")

#items - აბრუნებს წყვილების (key, value) სიას
