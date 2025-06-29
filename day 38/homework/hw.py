#შექმენით ფუნქცია manual_index, რომელიც მიიღებს სიას და ელემენტს და დააბრუნებს ელემენტის ინდექსს სიაში. გამოიყენეთ მხოლოდ loop და if, .index მეთოდის გარეშე
def manual_index(lst, element):
    index = 0
    for item in lst:
        if item == element:
            return index
        index += 1
    return -1

list_saba = [1,2,3]
print(manual_index(list_saba , 2))
