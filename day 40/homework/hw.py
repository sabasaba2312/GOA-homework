#შეასრულეთ 3 მაგალითი ყველა მეთოდზე: split, join, replace, strip

#split
name_surname = "saba tavartkiladze"
result = name_surname.split()
print(result)

text = "me vswavlob goashi"
result1 = text.split()
print(result1)

saba = "goa is the best academy ever"
result8 = saba.split()
print(result8)

#join
text1 = ["me", "var", "saba", "tavartkiladze"]
result2 = " ".join(text1)
print(result2)

text2 = ["me", "miyvars", "goa"]
result3 = " ".join(text2)
print(result3)

text7 = ["goa", "aris", "sauketeso", "akademia"]
result9 = " ".join(text7)
print(result9)

#replace
text3 = "memiyvars goa"
result4 = text3.replace("goa", "goasakademi")
print(result4)

text4 = "goa best"
result5 = text4.replace("best", "sauketeso")
print(result5)

text8 = "red blue"
result10 = text8.replace("blue", "green")
print(result10)

#strip
text5 = "   saba   "
result6 = text5.strip()
print(result6)

text6 = "    goa   "
result7 = text6.strip()
print(result7)

text9 = "     laptop      "
result11 = text9.strip()
print(result11)