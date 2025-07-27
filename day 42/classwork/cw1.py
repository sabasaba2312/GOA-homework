# კომენტარებით რა არის dictionary, შემდეგ შექმენით 1 dictionary სახელად person რომელშიც გასაღებები იქნება: name, hobby, height, weight. გამოიყენეთ მეთოდები:

#clear(),
#copy(),
#get(),
#items(),
#keys(),
#values(),
#pop(),
#popitem(),
#update

person = {
    "name" : "saba",
    "hoby" : "footballer",
    "height" : 1.78,
    "weight": 72

}

person_copy = person.copy()
lastitem = person.popitem()
popitem = person.pop("name")
clearitems = person.clear()
keys = person.keys()
values = person.values()
get = person.get("hoby")
update = person.update({
    "height": 1.90
})

print(person)