# მოხმარებელს შემოატანინეთ თავისი გამოცდის ქულა, შემდეგ პირობითი განხცადების საშვალებით შეამოწმეთ ეს ქულა მეტია თუ 50-ზე, თუ მეტია დაუბეჭდეთ რომ გამოცდა ჩააბარა
# bonus დავბეჭდოთ თუ არის მომხმარებლის ქულა ლუწი
qula = int(input("ramdeni qula aige: "))
if qula > 50:
    print("chaabare")
else:
    print("verchaabare")

if qula % 2 == 0:
    print("chaabare")
else:
    print("torti xart")
