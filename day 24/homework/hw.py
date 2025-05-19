#მომხმარებელს შემოატანინეთ სიტყვა, შემდეგ if-ით შეამოწმეთ ეს სიტყვა თუ თავისი თავის ტოლია როდესაც შემოაბრუნებთ (slicing-ის დახმარებით), თუ ასეა დაბეჭდეთ რომ განსაკუთრებული (ასეთ სიტყვებს palindrome ჰქვია) სიტყვაა, სხვა შემთხვევაში კი დაბეჭდეთ რომ ჩვეულებრივი სიტყვაა.
sityva = input("enter any sityva: ")
worlds = sityva[::-1]
if sityva == worlds:
    print("palindromea")
else:
    print("chveulebrivi sityvaa")