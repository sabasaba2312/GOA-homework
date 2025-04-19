#შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები
number = 0
luwi_raodenoba = 0
kenti_raodenoba = 0
while number >= 0:
    number = int(input("enter number: "))
    if number % 2 == 0:
        luwi_raodenoba = luwi_raodenoba + 1
    elif number % 2 == 1:
        kenti_raodenoba = kenti_raodenoba + 1
        
print("luwebis raodenoba" , luwi_raodenoba)
print("kentebis raodenoba", kenti_raodenoba)

