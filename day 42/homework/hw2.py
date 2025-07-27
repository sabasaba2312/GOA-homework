#შექმენით dictionary სახელად student, დაამატეთ მას მონაცემები: name, hobby, height, weight. შემდეგ გამოიყენეთ .get() მეთოდი name-ის მისაღებად და .pop() მეთოდი height-ის წასაშლელად. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი
student = {
    "name" : "saba",
    "hobby" : "footballer",
    "height" : 1.78,
    "weight": 72
}

get = student.get("name")
pop = student.pop("height")

print(get)
print(pop)
    
print(student)


#get - აბრუნებს მნიშვნელობას გასაღების მიხედვით
#pop - წაშლის მითითებულ გასაღებს და აბრუნებს მის მნიშვნელობას
#clear - წაშლის ყველა ელემენტს
#copy -წაშლის ლექსიკონის ყველა ელემენტს
#items - აბრუნებს წყვილების (key, value) სიას
#keys- აბრუნებს მხოლოდ გასაღებებს
#values - აბრუნებს ყველა მნიშვნელობას
#popitem - წაშლის ბოლო წყვილს
#update - ამატებს ან ანახლებს ლექსიკონს სხვა წყვილების დახმარებით
