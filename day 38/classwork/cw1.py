# შექმენით manual_max ფუნქცია რომელსაც პარამეტრად გადაეცემა სია და აბრუნებს ყველაზე დიდ მნიშვნელობას. ასევე შექმენით manual_len ფუნქცია რომელიც თვლის გადაცემული მიმდევრობის სიგრძეს
def manual_max(goa):
    for i in goa:
        number = goa[0]
        for num in goa:
            if num > number:
                goa = num
    return number

def manual_len(saba):
    count = 0
    for i in saba:
        count += 1
    return count


