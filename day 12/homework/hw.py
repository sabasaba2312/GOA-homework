#გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი
# > 
print(10 > 5) # true
print(50 > 30) # true
print(100 > 110) # false
print(400 > 401) # false
print(150 > 149) # true

# <
print(500 < 506) # true
print(300 < 301) # true
print(1000 < 200) # false
print(500 < 600) # true
print(200 < 201) # true

# >=
print(400 >= 400) # true
print(300 >= 199) # true
print(500 >= 500) # true
print(100 >= 190) # false
print(700 >= 701) # false

# <=
print(100 <= 900) # true
print(390 <= 400) # true
print(400 <= 400) # true
print(200 <= 199) # false
print(660 <= 900) # true

# ==
print(200 == 200) # true
print(100 == 500) # false
print(100 == 300) # false
print(200 == 199) # false
print(200 == 200) # true

# !=
print(200 != 199) # true
print(300 != 300) # false
print(400 != 400) # false
print(100 != 300) # true
print(777 != 776) # true



