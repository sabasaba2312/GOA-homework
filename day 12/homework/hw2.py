#შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები
temperature = 30
cloudy = True
summer = 40
raining = True
short = False
print(temperature < 31 and not cloudy) # false
print(summer > 30 or short) # true
print(raining and not short) # true
print(temperature >= 30 and not cloudy) # false
print(summer <= 40 and cloudy) # true



