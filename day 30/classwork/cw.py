#თითოეულ მეთოდზე: len, append, insert, pop, remove მეთოდებზე გააკეთეთ 3-3 მაგალითი. len ფუნქციაზე მოიყვანეთ string-ის მაგალითიც
goa = [5, 20, 30, 50, 70, 80 , "saba"]

goa.pop(2)
goa.pop(0)
goa.pop(1)

goa.remove(80)
goa.remove(20)
goa.remove(70)

goa.insert(3, 100)
goa.insert(1, 200)
goa.insert(6, "goa")

goa.append(75)
goa.append(105)
goa.append(95)

print(goa)
print(len(goa))