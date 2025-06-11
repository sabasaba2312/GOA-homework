#დაწერე ფუნქცია, რომელიც იღებს სიტყვების სიას და აბრუნებს სიის ყველაზე გრძელ სიტყვას. გამოიყენე ციკლი და 'len()' შედარებისთვის
def greet(list):
    goa = ""
    for saba in list:
        if len(saba) > len(goa):
            goa = saba
    return(goa)

print(greet(["saba", "nikolozi", "nika", "beqa"]))
            
