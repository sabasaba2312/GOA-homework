#დაწერეთ ფუნქცია, რომელიც მიიღებს სიას და დაბეჭდავს უნიკალურ ელემენტებს და მათ რაოდენობას სიაში, მაგ: apple - 2, banana - 3... გამოიყენეთ .count მეთოდი

def print_unique_counts(goa):
    unique_elements = []
    for item in goa:
        if item not in unique_elements:
            unique_elements.append(item)
    
    for element in unique_elements:
        count = goa.count(element)
        print(f"{element} - {count}")


fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
print_unique_counts(fruits)