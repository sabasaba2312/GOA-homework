#მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები
pincode = 1233
cda = 3
while cda > 0:
    pincode1 = int(input("enter your picode: "))
    if pincode == pincode1:
        print("Access Granted")
    else:
        cda = cda - 1
        print("access Denied")
