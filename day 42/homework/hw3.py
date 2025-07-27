#დაწერეთ ფუნქცია, რომელიც იღებს ლექსიკონს და აბრუნებს მის keys-სა და values-ს .keys() და .values() მეთოდებით. დაბეჭდეთ ორივე შედეგი და დაურთეთ კომენტარები
def set(person):
    keys = person.keys()
    values = person.values()
    return keys, values


print(set(person = {
    "name" : "saba",
    "hoby" : "footballer",
    "height" : 1.78,
    "weight": 72

}))

#keys- აბრუნებს მხოლოდ გასაღებებს
#values - აბრუნებს ყველა მნიშვნელობას