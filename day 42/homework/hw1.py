#დაწერეთ ფუნქცია, რომელიც იღებს set-ს, ამატებს მას 3 ელემენტს add() მეთოდით, შემდეგ შლის ერთ ელემენტს remove() მეთოდით და აბრუნებს საბოლოო შედეგს

def set(numbers):
    result = numbers.add(20)
    result1 = numbers.add(30)
    result2 = numbers.add(40)
    result3 = numbers.remove(30)
    return numbers

print(set({60, 70, 80, 90}))