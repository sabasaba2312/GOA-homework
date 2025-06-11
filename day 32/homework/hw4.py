#დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს
def list(numbers):
    goa = 0
    if len(numbers) > 0:
        goa = sum(numbers) / len(numbers)
    return goa

print(list([10, 40, 30]))
