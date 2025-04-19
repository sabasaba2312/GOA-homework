#მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად, საბოლოოდ დაბეჭდეთ ყველა მიღებული დადებითი რიცხვის ჯამი
ricxvebi = 0
number = 0
while number >= 0:
    number = int(input("enter your number: "))
    if number > 0:
        ricxvebi = ricxvebi + number
    else:
        print("uaryofitia")
print(ricxvebi)

    
