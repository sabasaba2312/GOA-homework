#შექმენით set სახელად numbers, დაამატეთ მას ორი რიცხვი add() მეთოდით და წაშალეთ ორი ელემენტი remove() მეთოდით. შემდეგ შექმენით მეორე set სახელად even_numbers და გამოიყენეთ union(), intersection(), difference() ორივე set-ზე. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი

numbers = {30, 60, 90, 100}
result = numbers.add(200)
result1 = numbers.add(300)
resul2 = numbers.remove(60)
resul3 = numbers.remove(90)

even_numbers = {845 ,848 ,100 ,900}

#union მეთოდი აერთიანებს ორივე set - ის რიცხვებს
result4 = numbers.union(even_numbers)

#intersection მეთოდს გამოაქვს მხოლოდ ერთნაირი რიცხვები set - ებს შორის
result5 = numbers.intersection(even_numbers)

#difernece მეთოდიი თვლის თუ რა რიცხვებია ერთ set ში და მეორეში არა
result6 = numbers.difference(even_numbers)


