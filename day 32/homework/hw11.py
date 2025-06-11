#დაწერე ფუნქცია, რომელიც იღებს რიცხვს 'n' და აბრუნებს სიას 1-დან 'n'-ის ჩათვლით ყველა ლუწი რიცხვით. გამოიყენე for ციკლი და if-else
def number(n):
    goa = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            goa = goa + [i]
        else:
            goa = goa + []
    return goa

print(number(11))