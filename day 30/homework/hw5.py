#შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს რიცხვს და დააბრუნებს მის ფაქტორიალს. n რიცხვის ფაქტოირალი არის ყველა მთელი დადებითი რიცხვის ნამრავლი 1-იდან n-ის ჩათვლით
def greet(n):
    result = 1
    current = 1

    while current <= n:
        result *= current
        current += 1

    return result

saba = greet(10)
print(saba)


