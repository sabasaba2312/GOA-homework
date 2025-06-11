#დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია
def number(num):
    if num % 2 ==0:
        return(num, "even")
    else:
        return(num, "odd")

print(number(15))