#შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა
pincode = 2509
pincode1 = " "
cda = 0 

while pincode != pincode1:
    pincode1  = int(input("enter pincode: "))
    cda += 1
print("sworia" + " " + "shen dagjirda" + " " + str(cda) + " " + "cda")
