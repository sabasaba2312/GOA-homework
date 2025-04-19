#მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ თუ ეს რიცხვი დადებითია დაბეჭდეთ ეს და კიდევ შეამოწმეთ ლუწია თუ კენტი, ხოლო თუ არაა დადებითი მხოლოდ დაბეჭდეთ რომ უარყოფითია
number = int(input("enter your number: "))
if number > 0:
    print("dadebitia")
    if number % 2 ==0:
        print("luwia")
    else:
        print("kentia")
else:
    print("uaryofitia")