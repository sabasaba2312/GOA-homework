#განხილულ მეთოდებზე: split, join, replace, strip მოიყვანეთ 2-2 მაგალითი. თითოეულს მიუწერეთ კომენტარებით ახსნა თუ როგორ მუშაობს

#split ყოფს სტრიქონს და აბრუნებს დაყოფილად სიის სახით
name_surname = "saba tavartkiladze"
result = name_surname.split()
print(result)

text = "me vswavlob goashi"
result1 = text.split()
print(result1)

#join სიას აერთიანებს სტრიქონთან 
text1 = ["me", "var", "saba", "tavartkiladze"]
result2 = " ".join(text1)
print(result2)

text2 = ["me", "miyvars", "goa"]
result3 = " ".join(text2)
print(result3)

#replace სტრინგში შეგვიძლია ძველოი ნაწილის ჩანაცვლება
text3 = "memiyvars goa"
result4 = text3.replace("goa", "goasakademi")
print(result4)

text4 = "goa best"
result5 = text4.replace("best", "sauketeso")
print(result5)

#strip შეგვიძლია სიცარიელის ან ზედმეტი სიმბოლოების მოცილება 
text5 = "   saba   "
result6 = text5.strip()
print(result6)

text6 = "    goa   "
result7 = text6.strip()
print(result7)