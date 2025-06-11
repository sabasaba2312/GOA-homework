#დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ შორის უმეტესს
def greet(num1, num2):
    if num1 > num2:
        return(num1)
    else:
        return(num2)

print(greet(10, 30))