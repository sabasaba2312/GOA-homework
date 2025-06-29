#შექმენით ფუნქცია manual_count, რომელიც მიიღებს სიას და ელემენტს და დააბრუნებს ელემენტის რაოდენობას სიაში. გამოიყენეთ მხოლოდ loop და if, .count მეთოდის გარეშე

def manual_count(list_1, elemet):
    saba = 0
    for i in list_1:
        if i == elemet:
            saba += 1
    return saba

goa = [1, 3, 5, 9 ,10]
print(manual_count(goa, 3))
    