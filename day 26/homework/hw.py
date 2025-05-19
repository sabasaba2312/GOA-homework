# დაწერეთ პროგრამა, რომელიც ითხოვს ორ რიცხვს მომხმარებლისგან. შემოაყვანინეთ მომხმარებელს დაწყების და დასრულების რიცხვი. თუ მეორე რიცხვი ნაკლებია პირველზე, გამოუტანეთ შეტყობინება: არასწორი შუალედი. სხვა შემთხვევაში დაბეჭდეთ ყველა რიცხვი მოცემულ შუალედში ჩათვლით და იპოვეთ ამ რიცხვების ჯამი. გამოიყენეთ for ციკლი, if-else პირობა, input ფუნქცია, და int ტიპში გადაყვანა
number = int(input("enter start number: "))
number1 = int(input("enter end number: "))
if number1 < number:
    print("araswori shualedi")
else:
    goa1 = 0
    for goa in range(number, number1 + 1):
        print(goa)
        goa1 += goa
print(goa1)



