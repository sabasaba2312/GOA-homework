#დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მასში ხმოვნების (a, e, i, o, u) რაოდენობას. გამოიყენე ციკლი და if-else
def greet(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for saba in text:
        if saba in vowels:
            count = count + 1
        else:
            count = count + 0
    return count

print(greet("Goa sauketesoa"))
  
        
        

