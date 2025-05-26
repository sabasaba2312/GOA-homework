# შექმენით ახალი new_greet ფუნქცია რომელსაც ექნება 2 პარამეტრი: first_name და last_name. ამ ფუნქციამ უნდა დაბეჭდოს შემდეგი ტექსტი: "Greetings [firstname] [lastname] ფუნქცია 2-ჯერ გამოიძახეთ და გადაეცით არგუმენტები. კომენტარებით ახსენით რა განსხვავებაა პარამაეტრებსა და არგუმენტებს შორის
def greet(first_name, last_name):
    print("hello" + " " + first_name + " " + last_name)
    print("welcome")


greet("saba" , "tavartkiladze")
greet("beqa", "abuladze")
#პარამეტრი - ცვლადი, რომელიც განსაზღვრულია ფუნქციის აღწერის დროს. მაგ., first_name, last_name ფუნქციის შიგნით.

#არგუმენტი - კონკრეტული მნიშვნელობა, რომელიც ფუნქციის გამოძახებისას გადაეცემა პარამეტრს. მაგ "beqa", "abuladze"