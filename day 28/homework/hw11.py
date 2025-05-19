#შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა input-ით. თუ სიტყვა მოიძებნება find-ით, დაბეჭდეთ პოზიცია, სხვა შემთხვევაში კი დაბეჭდეთ word not found
sityva1 = "GOA aris sauketeso"
sityva = input("saziebeli sityva: ")
if sityva in sityva1:
    print(sityva1.find(sityva))
else:
    print("word not found")