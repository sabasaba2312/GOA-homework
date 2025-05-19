#შექმენით სიტყვების სია, შემდეგ მის შემობრუნებულ ვერსიას გადაუარეთ for ციკლით, დაბეჭდეთ ყოველი მეორე ელემენტი (რომ გაიგოთ ყოველი მეორე აიღეთ ცვლადი რომელიც თავიდან 0 იქნება, ყოველ გამეორებაზე კი გაზრდით ერთით და შეამოწმეთ ლუწია თუ კენტი)
languages = ["python", "java", "CSS", "C", "rust", "Ruby", "Vala", "Nim", "perl", "Dart"]
word = languages[::-1]
number = 0
for goa in word:
    if number % 2 == 0:
        print(goa)
    number = number + 1

if number % 2 == 0:
    print("luwia")
else:
    print("kentia")