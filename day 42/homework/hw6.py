#დაწერეთ ფუნქცია, რომელიც იღებს ლექსიკონს და ამატებს ახალ წყვილს ('age': 14) .update() მეთოდით, შემდეგ კი შლის ბოლო ელემენტს .popitem() მეთოდით. დაბეჭდეთ შედეგი და დაუმატეთ კომენტარები
def update_person(person):
    person.update({
        "age": 14
    })
    person.popitem()
    return person



print(update_person({
    "name" : "saba",
    "hoby" : "footballer",
    "height" : 1.78,
    "weight": 72

}))

#popitem - წაშლის ბოლო წყვილს